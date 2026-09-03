# Dark Matter Project 2: XENON1T Approximate Nuclear-Recoil Likelihood

**A first-pass group-project recast of the public XENON1T approximate nuclear-recoil likelihood for a simplified spin-independent elastic WIMP model.**

## Research question and current result

The project asks how the public [XENON1T approximate nuclear-recoil likelihood](https://github.com/XENON1T/xenon1t_approximate_nuclear_recoil_likelihood) can be used to construct a mass-dependent asymptotic 90% upper-limit curve for simplified WIMP-xenon recoil templates.

The repository currently generates spectra at ten benchmark masses from 5 to 200 GeV, evaluates them with the approximate likelihood package and commits the resulting curve as [`data/processed/limit_curve.csv`](data/processed/limit_curve.csv) with a corresponding [plot](plots/limit_curve.png). This is an academic first-pass analysis, not an official XENON1T result or a precision reproduction of the collaboration's full analysis.

## Methodology

1. `make_physical_model_csvs.py` generates recoil-spectrum templates from 1 to 70 keV for a spin-independent elastic WIMP-xenon model.
2. The model uses the stated Standard Halo Model parameters and a Helm nuclear form factor documented in [`data/README.md`](data/README.md).
3. `run_all_model_csvs.py` loads each spectrum into the public XENON1T approximate likelihood through `BinwiseInference.from_xenon1t_sr`.
4. The code computes an asymptotic 90% upper limit for each benchmark mass and `plot_check/plot_limit_curve.py` renders the committed curve.

The generated spectra include a fixed factor of `1e45` for numerical convenience. They are arbitrarily normalized templates rather than absolute physical recoil rates, so the committed upper-limit values should be interpreted within this repository's chosen normalization.

## Repository structure

| Path | Purpose |
|---|---|
| `make_physical_model_csvs.py` | Generate benchmark WIMP recoil-spectrum CSV files |
| `run_all_model_csvs.py` | Run the approximate likelihood across the mass grid |
| `src/io/` | Reusable spectrum, likelihood-scan and limit-curve interfaces |
| `data/raw/` | Benchmark recoil templates and a diagnostic test spectrum |
| `data/processed/` | Committed likelihood-scan and upper-limit outputs |
| `plot_check/` | Development and final plotting scripts |
| `plots/` | Generated diagnostic and final figures |
| `notebooks/` | Exploratory analysis notebooks |
| [`Project report DM2.pdf`](Project%20report%20DM2.pdf) | Group project report |

## Environment setup

Clone the repository:

```powershell
git clone https://github.com/FlorisOrd/stats-project-DM2.git
cd stats-project-DM2
```

Create and activate a virtual environment:

```powershell
python -m venv .venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

On Linux or macOS, activate it with:

```bash
source .venv/bin/activate
```

Install the project requirements:

```powershell
python -m pip install --upgrade pip setuptools wheel
python -m pip install -r requirements.txt
```

Install the official XENON1T likelihood package:

```powershell
cd ..
git clone https://github.com/XENON1T/xenon1t_approximate_nuclear_recoil_likelihood.git
cd xenon1t_approximate_nuclear_recoil_likelihood
python -m pip install .
cd ..\stats-project-DM2
```

## Reproduce the committed workflow

Generate the benchmark spectra:

```powershell
python .\make_physical_model_csvs.py
```

Run the mass scan:

```powershell
python .\run_all_model_csvs.py
```

Plot the committed limit curve:

```powershell
python .\plot_check\plot_limit_curve.py
```

`run_all_model_csvs.py` prints the upper-limit values but does not write `data/processed/limit_curve.csv` automatically. The committed final CSV was saved manually from the scan output.

## Outputs

| File | Status |
|---|---|
| [`data/processed/limit_curve.csv`](data/processed/limit_curve.csv) | Final ten-mass upper-limit curve used by the project |
| [`plots/limit_curve.png`](plots/limit_curve.png) | Final report figure |
| `data/processed/likelihood_scan.csv` | Development/diagnostic scan |
| `data/raw/test_spectrum.csv` | Development/diagnostic input |
| `plots/likelihood_scan_annotated.png` | Development/diagnostic figure |

## Limitations

- The signal model is simplified and evaluated only on the committed ten-mass grid.
- Spectrum normalization includes a numerical convenience factor and should not be read as an absolute physical recoil rate.
- The final curve CSV is manually transferred from console output rather than generated end to end by the mass-scan script.
- The work uses the public approximate likelihood release and should not be presented as the collaboration's official limit.
- The repository contains exploratory notebooks and diagnostic artefacts alongside the final workflow.

## My role and development approach

This was a five-person group project. I served as data lead.

| Team member | Recorded role |
|---|---|
| Floris Ordelmans | Data lead |
| Cristian Ioniță | Inference lead |
| Gianny Capitein | Plot and diagnostics lead |
| Yuval Rochman | Integration and writing lead |
| Ivan Iturralde | Model lead |
