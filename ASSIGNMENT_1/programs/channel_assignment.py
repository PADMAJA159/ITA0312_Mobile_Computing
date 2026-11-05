from .geometry import valid_cluster_sizes, axial_hex_grid

def assign_fixed_channel_groups(pool_size, cluster_size, rings=3):
    groups = {}
    for q, r in axial_hex_grid(rings):
        group = (q*q + q*r + r*r + q + 2*r) % cluster_size
        groups[(q, r)] = group
    per_group = pool_size // cluster_size
    return {cell: list(range(g*per_group, (g+1)*per_group))
            for cell, g in groups.items()}

def iterative_cluster_search(pool_size, max_n=30):
    return [{"N": n, "channels_per_group": pool_size // n}
            for n in valid_cluster_sizes(max_n)]
