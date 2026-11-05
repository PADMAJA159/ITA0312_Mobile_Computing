# University Township Cellular Network Planner

Educational Python project for the 12-task Mobile Computing assignment. It generates geometry/capacity calculations, simplified SIR and Erlang-B results, recurrence tables, CSV files and plots.

## Run
Python 3.10+:
```bash
python -m pip install -r requirements.txt
python main.py
python -m unittest discover -s tests -v
```
Outputs are saved in `outputs/`.

## Strategies
1. Fixed cluster reuse (spatial reuse).
2. Sectorised reuse (spatial filtering; simplified effective-interferer approximation).
3. Dynamic channel assignment/borrowing (simplified shared trunk pool).
4. Macro-micro cell splitting (hierarchical capacity growth).

## Assignment task map
- Tasks 1–2: `cellular_planner/strategies.py`, `channel_assignment.py`
- Task 3: `geometry.py`, `traffic.py`, `analysis.py`
- Task 4: `simulation.py`, `outputs/sir_samples.csv`
- Task 5: `analysis.py`
- Tasks 6–7: `recurrence.py`
- Task 8: `simulation.py`, `tests/`
- Tasks 9–10: `reporting.py`, generated CSV/plots
- Task 11: `recommendation.py`
- Task 12: `event.py`

## Inputs from assignment
12 km²; 336 duplex traffic channels; subscribers 1,000 / 10,000 / 20,000 / 100,000; 0.025 Erlang/subscriber; 2% blocking target; path-loss exponents 2.5, 3 and 4; N=3, 4, 7, 12; stadium event 25,000 × 0.05 Erlang in 1 km² for four hours.

## Important modelling notes
- Hex cell area = (3√3/2)R²; reuse distance D=R√(3N); reuse ratio Q=√(3N).
- SIR theory uses (Q^n)/i0. Omni approximation uses six first-tier interferers. Sectorised cases use effective i0=2 (120°) or 1 (60°), only as an educational approximation—not a real antenna-pattern model.
- Monte-Carlo users are sampled uniformly inside a circular cell and interferers are placed at approximate first-tier reuse distance.
- Erlang-B assumes a loss system with Poisson arrivals and no waiting.
- Dynamic borrowing and cell splitting are simplified planning models, not vendor-grade radio resource management.
- Site and survey costs are illustrative indices. Replace them with local quotations and measured survey costs.
- The assignment asks for a minimum SIR between 12 and 18 dB. State and justify the selected target in your written report, then compare the generated results against it.
- Check the model's assumptions and explain limitations in your submission; do not present the outputs as field measurements.

## GitHub
Extract the ZIP, create a repository, then upload the extracted folder contents. Or run:
```bash
git init
git add .
git commit -m "Add cellular network planning simulator"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
git push -u origin main
```
