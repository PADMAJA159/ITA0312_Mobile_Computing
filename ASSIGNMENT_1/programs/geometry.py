import math

def hex_cell_area(radius_km):
    if radius_km <= 0:
        raise ValueError("Radius must be positive")
    return (3 * math.sqrt(3) / 2) * radius_km**2

def cells_required(area_km2, radius_km):
    return math.ceil(area_km2 / hex_cell_area(radius_km))

def reuse_distance(radius_km, cluster_size):
    if radius_km <= 0 or cluster_size <= 0:
        raise ValueError("Inputs must be positive")
    return radius_km * math.sqrt(3 * cluster_size)

def reuse_ratio(cluster_size):
    return math.sqrt(3 * cluster_size)

def valid_cluster_sizes(max_n=30):
    # Hexagonal cluster sizes follow N=i^2+ij+j^2.
    values = set()
    for i in range(max_n + 1):
        for j in range(max_n + 1):
            n = i*i + i*j + j*j
            if 1 <= n <= max_n:
                values.add(n)
    return sorted(values)

def axial_hex_grid(rings):
    coords = []
    for q in range(-rings, rings + 1):
        for r in range(max(-rings, -q-rings), min(rings, -q+rings) + 1):
            coords.append((q, r))
    return coords
