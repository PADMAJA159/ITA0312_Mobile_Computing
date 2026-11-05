import math
import numpy as np
from .traffic import erlang_b

def monte_carlo_sir(cluster_size, path_loss_n, samples=4000, seed=42, effective_interferers=6):
    rng = np.random.default_rng(seed)
    radius = np.sqrt(rng.random(samples))
    theta = rng.uniform(0, 2*np.pi, samples)
    x, y = radius*np.cos(theta), radius*np.sin(theta)
    desired = np.maximum(np.sqrt(x*x+y*y), 0.03)**(-path_loss_n)
    d = math.sqrt(3*cluster_size)
    angles = np.arange(6)*np.pi/3
    ix, iy = d*np.cos(angles), d*np.sin(angles)
    interference = np.zeros(samples)
    for k in range(min(effective_interferers, 6)):
        dist = np.maximum(np.sqrt((x-ix[k])**2+(y-iy[k])**2), 0.03)
        interference += dist**(-path_loss_n)
    return 10*np.log10(desired/np.maximum(interference, 1e-30))

def sir_statistics(values):
    return {"mean_sir_db": float(np.mean(values)),
            "p05_sir_db": float(np.percentile(values, 5)),
            "outage_below_12db": float(np.mean(values < 12)),
            "outage_below_18db": float(np.mean(values < 18))}

def best_average_worst_sir(values):
    return {"best_db": float(np.max(values)), "average_db": float(np.mean(values)),
            "worst_db": float(np.min(values))}

def blocking_curve(channels, loads):
    return [erlang_b(channels, float(load)) for load in loads]
