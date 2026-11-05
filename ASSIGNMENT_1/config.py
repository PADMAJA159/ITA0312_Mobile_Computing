from dataclasses import dataclass

@dataclass
class Config:
    township_area_km2: float = 12.0
    channel_pool: int = 336
    subscribers: tuple = (1000, 10000, 20000, 100000)
    erlang_per_subscriber: float = 0.025
    gos_blocking: float = 0.02
    path_loss_exponents: tuple = (2.5, 3.0, 4.0)
    cluster_sizes: tuple = (3, 4, 7, 12)
    cell_radius_km: float = 0.5
    random_seed: int = 42
    sir_samples: int = 4000
    planning_cost_per_site: float = 10000.0
    survey_cost: float = 25000.0
    event_attendees: int = 25000
    event_erlang_per_attendee: float = 0.05
    event_area_km2: float = 1.0
    event_duration_hours: float = 4.0
    event_frequency_per_month: int = 2

CONFIG = Config()
