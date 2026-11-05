def erlang_b(channels, offered_erlangs):
    if channels < 0 or offered_erlangs < 0:
        raise ValueError("Inputs must be non-negative")
    b = 1.0
    for c in range(1, channels + 1):
        b = offered_erlangs * b / (c + offered_erlangs * b)
    return b

def channels_for_blocking(offered_erlangs, target_blocking=0.02, max_channels=100000):
    for c in range(max_channels + 1):
        if erlang_b(c, offered_erlangs) <= target_blocking:
            return c
    raise RuntimeError("Required channels exceed max_channels")

def traffic_per_cell(subscribers, cells, erlang_per_subscriber):
    return subscribers * erlang_per_subscriber / max(cells, 1)
