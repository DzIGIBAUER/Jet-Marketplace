

<div class="p-4">
    
    <div class="flex flex-col justify-center items-center px-8 gap-8 lg:flex-row">
        
        <div class="flex gap-2 flex-col">

            <div class="input-group input-group-divider grid-cols-[auto_1fr_auto]">
                <div class="input-group-shim">
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-search" viewBox="0 0 16 16">
                        <path d="M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398h-.001q.044.06.098.115l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1 1 0 0 0-.115-.1zM12 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0"/>
                    </svg>
                </div>
                <input type="search" placeholder="Search" bind:value={filters.searchQuery} class="p-1" />
            </div>
            
            <select bind:value={filters.orderBy} class="select">
                <option value="name" selected>Name</option>
                <option value="range">Range</option>
            </select>
            
            <select bind:value={filters.ordering} class="select">
                <option value="ascending" selected>Ascending</option>
                <option value="descending">Descending</option>
            </select>
    
        </div>

        <div>

            <p>Range</p>
            <div class="">
                <!-- not using bind:value={} because we want to refetch planes when value finnaly changes, not while user is typing -->
                <div class="input-group input-group-divider grid-cols-[auto_1fr_auto] w-min">
                    <div class="input-group-shim">
                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-align-start" viewBox="0 0 16 16">
                            <path fill-rule="evenodd" d="M1.5 1a.5.5 0 0 1 .5.5v13a.5.5 0 0 1-1 0v-13a.5.5 0 0 1 .5-.5"/>
                            <path d="M3 7a1 1 0 0 1 1-1h10a1 1 0 0 1 1 1v2a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1z"/>
                        </svg>
                    </div>
                    <input class="input p-1" type="number" placeholder="Min" bind:value={filters.rangeMin} />
                    <p class="p-2">km</p>
                </div>

                <div class="input-group input-group-divider grid-cols-[auto_1fr_auto] w-min">
                    <div class="input-group-shim">
                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-align-end" viewBox="0 0 16 16">
                            <path fill-rule="evenodd" d="M14.5 1a.5.5 0 0 0-.5.5v13a.5.5 0 0 0 1 0v-13a.5.5 0 0 0-.5-.5"/>
                            <path d="M13 7a1 1 0 0 0-1-1H2a1 1 0 0 0-1 1v2a1 1 0 0 0 1 1h10a1 1 0 0 0 1-1z"/>
                        </svg>
                    </div>
                    <input class="input p-1" type="number" placeholder="Max" bind:value={filters.rangeMax} />
                    <p class="p-2">km</p>
                </div>
                
            </div>

        </div>

    </div>

    <div class="flex flex-col px-8 pt-8 gap-8">
        
        <button type="button" disabled={!filtersChanged} class="btn variant-filled w-min" on:click={fetchPlanes}>Apply filters</button>

        <Paginator bind:settings={paginationSettings} />
    </div>

    {#if !planes.length}
        <div class="flex justify-center items-center p-8">
            <p class="text-warning-900">No results</p>
        </div>
    {/if}

    <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 p-4 gap-4">

        {#if loading}
            {#each {length: 8} as i}
                <div class="card rounded-2xl h-fit">
                    <header class="card-header h-[80%]"></header>

                    <section class="p-4 pt-[70%] w-[50%]">
                        <div class="text-lg font-semibold placeholder animate-pulse" />
                    </section>

                    <footer class="card-footer space-y-2">
                        <div class="text-xs text-secondary-500 placeholder animate-pulse" />
                        <div class="text-xs text-secondary-500 placeholder animate-pulse" />
                    </footer>
                </div>
            {/each}
        
        {:else}
            {#each planes as plane}
        
                <div class={`card card-hover rounded-2xl bg-gradient-to-br from-surface-900 ${!(plane.id in $comparePlanesStore) ? 'to-secondary-900' : 'to-primary-900'}`}>
                    <header class="card-header p-0 h-[50%]">
                        <img class="rounded-t-2xl object-cover w-[100%] h-[100%]" src={plane.image} alt={plane.name} />
                    </header>

                    <section class="p-4 flex justify-between">
                        <p class="text-lg font-semibold">{plane.name}</p>
                            {#if !(plane.id in $comparePlanesStore)}
                                <button type="button" class="btn-icon variant-filled-primary self-center" on:click={() => addToCompare(plane)}>
                                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                                        <path stroke-linecap="round" stroke-linejoin="round" d="M12 9v6m3-3H9m12 0a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z" />
                                    </svg>
                                </button>
                            {:else}
                                <button type="button" class="btn-icon variant-filled-secondary self-center" on:click={() => removeFromCompare(plane)}>
                                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                                        <path stroke-linecap="round" stroke-linejoin="round" d="M15 12H9m12 0a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z" />
                                    </svg>
                                </button>
                            {/if}

                    </section>

                    <footer>
                        <div class="card-footer flex justify-between">
                            <div>
                                <p class="text-xs text-secondary-500">
                                    No. of Seats: Up to <span class="font-bold">{plane.max_persons}</span> pax
                                </p>
                                <p class="text-xs text-secondary-500">
                                    Speed: <span class="font-bold">{plane.speed}</span>km/h
                                </p>
                                <p class="text-xs text-secondary-500">
                                    Range: <span class="font-bold">{plane.range}</span>km
                                </p>
                            </div>
                            <div class="flex w-[40%] justify-center">
                                <p class="text-xs text-secondary-500">
                                    Cabin:
                                    <br />
                                    Width: <span class="font-bold">{plane.cabin_width}</span>m
                                    <br />
                                    Height: <span class="font-bold">{plane.cabin_height}</span>m
                                    <br />
                                    Length: <span class="font-bold">{plane.cabin_length}</span>m
                                </p>
                            </div>
                        </div>
                    </footer>
                </div>
            {/each}

        {/if}

    </div>
    
</div>


<script lang="ts">
    import { Paginator, type PaginationSettings } from '@skeletonlabs/skeleton';
	import { comparePlanesStore } from '$lib/comparePlanes';
    import type { Plane, PaginatedResponse } from '$lib';

    import { onMount } from 'svelte';

    import { PUBLIC_BACKEND_API } from '$env/static/public';

    let planesResult: PaginatedResponse<Plane>;
    $: planes = planesResult ? planesResult.results : [];

    export let planesChanged: ((planes: Plane[]) => void) | undefined = undefined;

    let loading = false;

    let paginationSettings = {
        limit: 10,
        page: 0,
        amounts: [10, 14],
        size: 0
    } satisfies PaginationSettings;

    let filters = {
        orderBy: "name",
        ordering: "ascending",
        rangeMin: 0,
        rangeMax: 30000,
        searchQuery: ""
    }

    let filtersChanged = false;

    $: console.log(filters);
    
    $: if(planesResult && paginationSettings.size != planesResult.count) paginationSettings.size = planesResult.count;

    $: if (paginationSettings || filters) filtersChanged = true;

    $: if (planes && planesChanged) planesChanged(planes);

    const fetchPlanes = async () => {
        filtersChanged = false;
        loading = true;
        
        const apiUrl = new URL("/api/planes/", PUBLIC_BACKEND_API);
        apiUrl.searchParams.append("limit", paginationSettings.limit.toString());
        apiUrl.searchParams.append("page", (paginationSettings.page + 1).toString());

        apiUrl.searchParams.append("order_by", `${filters.ordering == "descending" ? '-' : ''}${filters.orderBy}`);
        apiUrl.searchParams.append("range__gt", filters.rangeMin.toString());
        apiUrl.searchParams.append("range__lt", filters.rangeMax.toString());
        apiUrl.searchParams.append("name__contains", filters.searchQuery);
        
        const data = await fetch(apiUrl.href);
        planesResult = await data.json();
        
        loading = false;
    }

    onMount(() => {
        fetchPlanes();
    });

    const addToCompare = (plane: Plane) => {
        $comparePlanesStore = {
            ...$comparePlanesStore,
            [plane.id]: {
                plane,
                color: `#${Math.floor(Math.random()*16777215).toString(16)}`
            }
        };
    }

    const removeFromCompare = (plane: Plane) => {
        delete $comparePlanesStore[plane.id];
        $comparePlanesStore = $comparePlanesStore;
    }

</script>