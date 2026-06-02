# Rough Path & Bernoulli Functionals Engine for ETFs

Applies rough path theory (Lyons 1998) to ETF return series. Computes the p‑variation (quadratic variation for p=2) as a measure of path roughness. The per‑ETF score is the roughness – higher = more erratic/noisy, lower = smoother/trending.

## Features
- Three ETF universes (FI/Commodities, Equity Sectors, Combined)
- Seven rolling windows (63–4536 days)
- p‑variation of return series (default p=2, realised variance)
- Score normalised by length of window
- Two‑tab Streamlit dashboard (auto best, manual)
- Results stored on Hugging Face: `P2SAMAPA/p2-etf-rough-bernoulli-results`

## Usage

1. Set `HF_TOKEN` environment variable.
2. Install dependencies: `pip install -r requirements.txt`
3. Run training: `python train.py` (very fast)
4. Launch dashboard: `streamlit run streamlit_app.py`

## Interpretation

- High roughness → path is irregular, potentially high volatility or noise → avoid or use for mean‑reversion strategies.
- Low roughness → path is smooth, more trending → suitable for momentum strategies.
- This is a novel signal derived from rough path theory.

## Requirements

See `requirements.txt`.
