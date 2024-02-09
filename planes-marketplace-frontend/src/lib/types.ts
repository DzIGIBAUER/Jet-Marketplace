
export type PaginatedResponse<T> = {
    count: number
    previous?: string
    next?: string
    results: T[]
}

export type Category = {
    id: number
    self: string
    name: string
    slug: string
}

export type Producer = {
    id: number
    self: string
    name: string
    slug: string
}

export type Plane = {
    id: number
    self: string
    name: string
    slug: string
    image: string
    
    category: Category
    producer: Producer

    cabin_height: number
    cabin_width: number
    cabin_length: number
    luggage_volume: number

    max_persons: number
    range: number
    speed: number
}
