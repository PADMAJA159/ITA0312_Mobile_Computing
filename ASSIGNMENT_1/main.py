from config import CONFIG
from cellular_planner.analysis import evaluate_strategies, scaling_rows
from cellular_planner.geometry import cells_required, hex_cell_area
from cellular_planner.simulation import monte_carlo_sir, sir_statistics
from cellular_planner.recurrence import uniform_split, minimum_uniform_rounds
from cellular_planner.event import analyse_event
from cellular_planner.reporting import save_outputs
from cellular_planner.channel_assignment import iterative_cluster_search
from cellular_planner.recommendation import recommendation

def main():
    c=CONFIG
    strategies=evaluate_strategies(c); scaling=scaling_rows(c)
    sir_data={}; sir_stats=[]
    for n in c.cluster_sizes:
        for exponent in c.path_loss_exponents:
            vals=monte_carlo_sir(n,exponent,c.sir_samples,c.random_seed,6)
            key=f"N={n}, n={exponent}"; sir_data[key]=vals
            sir_stats.append({"case":key,**sir_statistics(vals)})
    sites=cells_required(c.township_area_km2,c.cell_radius_km)
    event=analyse_event(c.event_attendees,c.event_erlang_per_attendee,c.event_area_km2,
                        .25,c.channel_pool//4,c.gos_blocking)
    initial_capacity=(c.channel_pool//4)*sites
    demand=c.subscribers[-1]*c.erlang_per_subscriber
    rounds=minimum_uniform_rounds(demand,initial_capacity)
    recurrence=uniform_split(sites,initial_capacity,1.0,min(rounds,6),3.5)
    capacity=[{"N":n,"channels_per_cell":c.channel_pool//n} for n in c.cluster_sizes]
    save_outputs("outputs",strategies,scaling,event,recurrence,sir_data,capacity)
    import pandas as pd
    pd.DataFrame(sir_stats).to_csv("outputs/sir_statistics.csv",index=False)
    print("Hex cell area (km2):",round(hex_cell_area(c.cell_radius_km),4))
    print("Estimated township sites:",sites)
    print("Valid cluster search:",iterative_cluster_search(c.channel_pool))
    print("Scaling cases:",scaling)
    print("Stadium event:",event)
    print("Uniform splitting rounds:",rounds)
    print("Recurrence:",recurrence)
    print("Recommendation:",recommendation())
    print("CSV files and plots saved in outputs/")

if __name__=="__main__":
    main()
