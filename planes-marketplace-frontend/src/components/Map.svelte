<svelte:head>
	<script>
		(g=>{var h,a,k,p="The Google Maps JavaScript API",c="google",l="importLibrary",q="__ib__",m=document,b=window;b=b[c]||(b[c]={});var d=b.maps||(b.maps={}),r=new Set,e=new URLSearchParams,u=()=>h||(h=new Promise(async(f,n)=>{await (a=m.createElement("script"));e.set("libraries",[...r]+"");for(k in g)e.set(k.replace(/[A-Z]/g,t=>"_"+t[0].toLowerCase()),g[k]);e.set("callback",c+".maps."+q);a.src=`https://maps.${c}apis.com/maps/api/js?`+e;d[q]=f;a.onerror=()=>h=n(Error(p+" could not load."));a.nonce=m.querySelector("script[nonce]")?.nonce||"";m.head.append(a)}));d[l]?console.warn(p+" only loads once. Ignoring:",g):d[l]=(f,...n)=>r.add(f)&&u().then(()=>d[l](f,...n))})({
		  key: "AIzaSyC0Xzt7kJSt2eXmc-z4aHAl4QzM-Riyc5Q",
		  v: "weekly",
		  libraries: "places"
		  // Use the 'v' parameter to indicate the version to use (weekly, beta, alpha, etc.).
		  // Add other bootstrap parameters as needed, using camel case.
		});
	</script>	  
</svelte:head>


<div id="map" class="w-screen h-screen"></div>


<script lang="ts">
	import { onMount } from "svelte";

	import { comparePlanesStore } from '$lib/comparePlanes';
	import { mapStyles } from "$lib";

	export let map: google.maps.Map | undefined = undefined;
	export let selectedAirport: google.maps.places.PlaceResult | undefined = undefined;
	export let onMapLoaded: (() => void) | undefined = undefined;

	let airportMarker: google.maps.Marker;
	let rangeCircles: google.maps.Circle[] = [];

	$: if (selectedAirport && map) {
		airportMarker ? airportMarker.setMap(null) : null;
		airportMarker = new google.maps.Marker({
			map,
			position: selectedAirport.geometry?.location
		});
	};

	$: if (selectedAirport && map && $comparePlanesStore) {
		rangeCircles.map(c => c.setMap(null));
		rangeCircles = [];

		Object.values($comparePlanesStore).forEach(compared => {
			rangeCircles.push(new google.maps.Circle({
				map,
				center: selectedAirport?.geometry?.location,
				radius: compared.plane.range * 1000,
				fillColor: compared.color,
				fillOpacity: 0.3,
			}));
		});
	}
	

	onMount(async () => {
		if (map) return;

		const { Map } = await google.maps.importLibrary("maps") as google.maps.MapsLibrary;

		map = new Map(
			document.getElementById('map') as HTMLElement,
			{
				zoom: 4,
				center: { lat: -25.344, lng: 131.031 },
				styles: mapStyles,
			}
		);
		
		onMapLoaded ? map.addListener('tilesloaded', onMapLoaded) : null;
	});

</script>