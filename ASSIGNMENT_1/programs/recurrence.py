import math

def uniform_split(initial_cells, initial_capacity, initial_power, rounds, path_loss_n=3.5):
    rows = []
    for k in range(rounds + 1):
        rows.append({"round": k, "cells": initial_cells*4**k,
            "capacity": initial_capacity*4**k,
            "relative_power": initial_power/(2**(path_loss_n*k)),
            "radius_fraction": 0.5**k})
    return rows

def selective_split(initial_cells, initial_capacity, initial_power, rounds,
                    split_fraction=0.25, path_loss_n=3.5):
    rows = []
    cells, capacity, power = float(initial_cells), float(initial_capacity), initial_power
    for k in range(rounds + 1):
        rows.append({"round": k, "cells": cells, "capacity": capacity, "relative_power": power})
        if k < rounds:
            factor = 1 + 3*split_fraction
            cells *= factor
            capacity *= factor
            power /= 2**(path_loss_n*split_fraction)
    return rows

def minimum_uniform_rounds(demand, initial_capacity):
    if demand <= initial_capacity:
        return 0
    return math.ceil(math.log(demand/initial_capacity, 4))

def minimum_selective_rounds(demand, initial_capacity, split_fraction=0.25):
    if demand <= initial_capacity:
        return 0
    return math.ceil(math.log(demand/initial_capacity, 1+3*split_fraction))
