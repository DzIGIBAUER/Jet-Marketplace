

<div class="p-4">
    
    <Paginator
        bind:settings={paginationSettings}
    />

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

    $: if(planesResult && paginationSettings.size != planesResult.count) paginationSettings.size = planesResult.count;

    $: if (paginationSettings) fetchPlanes();

    $: if (planes && planesChanged) planesChanged(planes);

    const fetchPlanes = async () => {
        loading = true;
        
        const apiUrl = new URL("http://127.0.0.1:8000/api/planes/");
        apiUrl.searchParams.append("limit", paginationSettings.limit.toString());
        apiUrl.searchParams.append("page", (paginationSettings.page + 1).toString());
        
        const data = await fetch(apiUrl.href);
        planesResult = await data.json();
        
        loading = false;
    }

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