
<div class="card">
    <header class="card-header p-0 h-[50%]">
        <img class="rounded-t-2xl object-cover" src={plane.image} alt={plane.name} />
    </header>
    <section class="p-5">
        <p>{plane.name}</p>

        <div class="grid grid-cols-[auto_1fr] gap-2">
            <input class="input" type="color" bind:value={color} />
            <input class="input" type="text" bind:value={color} readonly tabindex="-1" />
        </div>
    </section>
</div>




<script lang="ts">
    import type { Plane } from "$lib";
    import { comparePlanesStore } from '$lib/comparePlanes';

    export let plane: Plane;
    export let color: string;

    $: if($comparePlanesStore[plane.id].color != color) {
        $comparePlanesStore[plane.id].color = color;
        $comparePlanesStore = $comparePlanesStore;
    };

</script>