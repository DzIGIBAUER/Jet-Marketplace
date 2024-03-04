<script lang="ts">
	import '../app.postcss';
	import { initializeStores } from '@skeletonlabs/skeleton';
	import { Drawer, getDrawerStore } from '@skeletonlabs/skeleton';

	import { dev } from '$app/environment';
	import { inject } from '@vercel/analytics'
	
	import PlanesList from '../components/PlanesList.svelte';
	import type { Plane } from '$lib';

	initializeStores();
	inject({ mode: dev ? 'development' : 'production' });

	const drawerStore = getDrawerStore();

	const onPlanesUpdated = (planes: Plane[]) => {
		drawerStore.update((settings) => ({
			...settings,
			meta: { planes }
		}));
	}
</script>


<slot />
<Drawer
	position="right"
>
	<PlanesList
		planesChanged={onPlanesUpdated}
	/>
</Drawer>