from .geometry import cells_required
from .traffic import channels_for_blocking, erlang_b

def analyse_event(attendees, erlang_each, area_km2, radius_km, channels_per_cell,
                  target_blocking=0.02):
    total = attendees*erlang_each
    cells = cells_required(area_km2, radius_km)
    load = total/cells
    needed = channels_for_blocking(load, target_blocking)
    blocking = erlang_b(channels_per_cell, load)
    return {"event_total_erlangs": total, "event_area_km2": area_km2,
        "temporary_cells_at_radius": cells, "event_erlangs_per_cell": load,
        "channels_needed_per_cell_for_2pct": needed,
        "available_channels_per_cell": channels_per_cell,
        "estimated_blocking": blocking,
        "capacity_shortfall_channels": max(0, needed-channels_per_cell),
        "decision": "MODIFY: temporary stadium micro-cells / cells-on-wheels"
                    if needed > channels_per_cell else "RETAIN and monitor"}
