<div class="container h-full flex">
	<Map
		onMapLoaded={onMapLoaded}
		bind:selectedAirport
	/>
	<div class="p-4 w-[30%] h-screen flex flex-col">
		<div class="p-2 space-y-2">
			<label class="label">
				<span>Select airport</span>
				<input bind:this={inputElement} class="input p-2" type="text" placeholder="Input" />
			</label>
			
			<div class="flex justify-center">
				<button type="button" class="btn variant-filled-primary" on:click={() => drawerStore.open()}>
					<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
						<path stroke-linecap="round" stroke-linejoin="round" d="M12 4.5v15m7.5-7.5h-15" />
					</svg>				
				</button>
			</div>
		</div>

		<div class="overflow-y-auto">
			{#each Object.values($comparePlanesStore) as { plane, color }}
				<PlaneItem plane={plane} color={color} />
			{:else}
				<p class="text-xs text-warning-500 text-center">
					You haven't selected any planes yet.<br/>
					Click the button above to select
				</p>
			{/each}
		</div>

	</div>
</div>


<script lang="ts">
	import { getDrawerStore } from "@skeletonlabs/skeleton";
	import { comparePlanesStore } from '$lib/comparePlanes';

	import Map from "../components/Map.svelte";
	import PlaneItem from "../components/PlaneItem.svelte";

	const drawerStore = getDrawerStore();

	

	let inputElement: HTMLInputElement;

	let selectedAirport: google.maps.places.PlaceResult;

	const onMapLoaded = () => {
		let autocomplete = new google.maps.places.Autocomplete(inputElement, {
			types: ["airport"]
		});

		autocomplete.addListener("place_changed", () => {
			selectedAirport = autocomplete.getPlace();
		});
	}

	

</script>