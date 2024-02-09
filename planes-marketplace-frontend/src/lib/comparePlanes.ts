import type { Plane } from "$lib";
import { writable } from "svelte/store";



export type ComparedPlane = {
    plane: Plane,
    color: string
}

type ComparePlanes = {
    [id: number]: ComparedPlane
}

export const comparePlanesStore = writable<ComparePlanes>({});
