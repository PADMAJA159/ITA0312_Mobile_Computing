import math
from dataclasses import dataclass
from .geometry import reuse_ratio
from .traffic import erlang_b

@dataclass
class StrategyResult:
    name: str
    governing_parameter: str
    channels_per_cell: int
    effective_interferers: int
    theoretical_sir_db: float
    offered_erlangs: float
    blocking_probability: float
    principle: str

def theoretical_sir_db(n, path_loss_n, interferers=6):
    sir = reuse_ratio(n)**path_loss_n / interferers
    return 10 * math.log10(sir)

def fixed_reuse(pool, n, traffic, path_loss_n):
    ch = pool // n
    return StrategyResult("Fixed cluster reuse", "Cluster size N / reuse ratio Q",
        ch, 6, theoretical_sir_db(n, path_loss_n, 6), traffic,
        erlang_b(ch, traffic), "Spatial reuse")

def sectorised_reuse(pool, n, traffic, path_loss_n, sectors=3):
    i0 = 2 if sectors == 3 else 1
    ch = pool // n
    return StrategyResult(f"{sectors}-sector reuse", "N and sector count",
        ch, i0, theoretical_sir_db(n, path_loss_n, i0), traffic,
        erlang_b(ch, traffic), "Spatial filtering")

def dynamic_borrowing(pool, n, traffic, path_loss_n):
    # Simplified group-level trunking: N cells share the complete channel pool.
    ch = pool
    group_load = traffic * n
    return StrategyResult("Dynamic assignment / borrowing", "Shared pool and reuse guard",
        ch, 6, theoretical_sir_db(n, path_loss_n, 6), group_load,
        erlang_b(ch, group_load), "Trunking efficiency")

def hierarchical_split(pool, n, traffic, path_loss_n, rounds=1):
    ch = (pool // n) * (4**rounds)
    return StrategyResult("Macro-micro / cell splitting", "Cell radius and split rounds k",
        ch, 2, theoretical_sir_db(n, path_loss_n, 2), traffic,
        erlang_b(ch, traffic), "Hierarchical spatial reuse")
