from .geometry import cells_required
from .traffic import channels_for_blocking
from .strategies import fixed_reuse, sectorised_reuse, dynamic_borrowing, hierarchical_split

def evaluate_strategies(cfg):
    rows = []
    sites = cells_required(cfg.township_area_km2, cfg.cell_radius_km)
    load = cfg.subscribers[-1]*cfg.erlang_per_subscriber/sites
    for n in cfg.cluster_sizes:
        for exponent in cfg.path_loss_exponents:
            results = [fixed_reuse(cfg.channel_pool,n,load,exponent),
                sectorised_reuse(cfg.channel_pool,n,load,exponent,3),
                dynamic_borrowing(cfg.channel_pool,n,load,exponent),
                hierarchical_split(cfg.channel_pool,n,load,exponent,1)]
            for r in results:
                rows.append({"strategy":r.name,"N":n,"path_loss_n":exponent,
                    "cell_radius_km":cfg.cell_radius_km,"sites":sites,
                    "channels_per_cell_or_group":r.channels_per_cell,
                    "effective_interferers":r.effective_interferers,
                    "theory_sir_db":r.theoretical_sir_db,
                    "offered_erlangs_modelled":r.offered_erlangs,
                    "blocking_probability":r.blocking_probability,
                    "design_principle":r.principle,
                    "governing_parameter":r.governing_parameter,
                    "illustrative_total_cost":cfg.survey_cost+sites*cfg.planning_cost_per_site})
    return rows

def scaling_rows(cfg):
    rows=[]
    sites=cells_required(cfg.township_area_km2,cfg.cell_radius_km)
    for subs in cfg.subscribers:
        total=subs*cfg.erlang_per_subscriber
        load=total/sites
        rows.append({"subscribers":subs,"total_offered_erlangs":total,"sites_at_fixed_radius":sites,
            "erlangs_per_site":load,
            "channels_required_per_site_for_2pct":channels_for_blocking(load,cfg.gos_blocking),
            "fixed_reuse_channels_per_site_N4":cfg.channel_pool//4})
    return rows
