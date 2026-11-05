from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from .traffic import erlang_b

def save_outputs(out_dir, strategy_rows, scaling, event_result, recurrence, sir_data, capacity_rows):
    out=Path(out_dir); out.mkdir(parents=True,exist_ok=True)
    pd.DataFrame(strategy_rows).to_csv(out/"strategy_summary.csv",index=False)
    pd.DataFrame(scaling).to_csv(out/"subscriber_scaling.csv",index=False)
    pd.DataFrame([event_result]).to_csv(out/"event_analysis.csv",index=False)
    pd.DataFrame(recurrence).to_csv(out/"recurrence.csv",index=False)
    pd.DataFrame(capacity_rows).to_csv(out/"capacity_by_cluster.csv",index=False)
    sir_frame=[]
    for case, vals in sir_data.items():
        sir_frame.extend([{"case":case,"sample":i,"sir_db":float(v)} for i,v in enumerate(vals)])
    pd.DataFrame(sir_frame).to_csv(out/"sir_samples.csv",index=False)

    rep=next(x for x in strategy_rows if x["strategy"]=="Fixed cluster reuse" and x["N"]==4 and x["path_loss_n"]==3.0)
    ch=int(rep["channels_per_cell_or_group"]); loads=np.linspace(0,max(1,ch*1.5),100)
    plt.figure(); plt.plot(loads,[erlang_b(ch,a) for a in loads]); plt.axhline(.02,linestyle="--")
    plt.xlabel("Offered traffic (Erlangs/cell)"); plt.ylabel("Blocking probability")
    plt.title(f"Blocking vs load (N=4, {ch} channels)"); plt.grid(True); plt.tight_layout()
    plt.savefig(out/"blocking_vs_load.png",dpi=160); plt.close()

    cap=pd.DataFrame(capacity_rows)
    plt.figure(); plt.plot(cap.N,cap.channels_per_cell,marker="o")
    plt.xlabel("Cluster size N"); plt.ylabel("Channels per cell group")
    plt.title("Channel allocation vs cluster size"); plt.grid(True); plt.tight_layout()
    plt.savefig(out/"capacity_vs_cluster.png",dpi=160); plt.close()

    plt.figure()
    for case,vals in sir_data.items():
        x=np.sort(np.asarray(vals)); y=np.arange(1,len(x)+1)/len(x); plt.plot(x,y,label=case)
    plt.xlabel("SIR (dB)"); plt.ylabel("Empirical CDF"); plt.title("Monte-Carlo SIR distributions")
    plt.legend(fontsize=7); plt.grid(True); plt.tight_layout()
    plt.savefig(out/"sir_cdf.png",dpi=160); plt.close()

    subset=pd.DataFrame(strategy_rows)
    subset=subset[(subset.N==4)&(subset.path_loss_n==3.0)]
    plt.figure(); plt.bar(subset.strategy,subset.theory_sir_db)
    plt.xticks(rotation=20,ha="right"); plt.ylabel("Approximate SIR (dB)")
    plt.title("Strategy SIR comparison (N=4, n=3)"); plt.tight_layout()
    plt.savefig(out/"strategy_comparison.png",dpi=160); plt.close()
