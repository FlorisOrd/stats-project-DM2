# Dark Matter Project 2: XENON1T Approximate Nuclear-Recoil Likelihood

A first-pass recast of the XENON1T approximate nuclear-recoil likelihood for a simplified spin-independent elastic WIMP model, producing a mass-dependent 90% upper-limit curve from 5 to 200 GeV.

## Team members
| Name | Student ID | Role |
|---|---|---|
| Floris Ordelmans | S5693705 | Data lead |
| Cristian Ioniță | S5299837 | Inference lead |
| Gianny Capitein | S4498313 | Plot/diagnostics lead |
| Yuval Rochman | S5411505 | Integration/writing lead |
| Ivan Iturralde | S5325986 | Model lead |

## Repository structure
| Folder | Contents |
|---|---|
| `data/raw/` | Benchmark recoil-spectrum CSVs and toy test spectrum |
| `data/processed/` | Output limit curve CSV |
| `src/` | Reusable analysis code |
| `plot_check/` | Diagnostic and development plotting scripts |
| `plots/` | Generated figures |
| `notebooks/` | Exploratory notebooks |

## Public data / external package
This project uses the public [XENON1T approximate nuclear-recoil likelihood release](https://github.com/XENON1T/xenon1t_approximate_nuclear_recoil_likelihood).

---

## Environment setup

### 1. Clone this repository
```powershell
git clone https://github.com/FlorisOrd/stats-project-DM2.git
cd stats-project-DM2
```

### 2. Create a virtual environment
```powershell
python -m venv .venv
```

### 3. Activate the virtual environment

**Windows (PowerShell):**
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```
**Linux / macOS:**
```bash
source .venv/bin/activate
```

### 4. Install project requirements
```powershell
python -m pip install --upgrade pip setuptools wheel
python -m pip install -r requirements.txt
```

### 5. Install the official XENON1T likelihood package
```powershell
cd ..
git clone https://github.com/XENON1T/xenon1t_approximate_nuclear_recoil_likelihood.git
cd xenon1t_approximate_nuclear_recoil_likelihood
python -m pip install .
cd ..\stats-project-DM2
```

---

## How to reproduce the final result

Run these two steps in order from the repository root:

**Step 1 — Generate benchmark recoil spectra**
```powershell
python .\make_physical_model_csvs.py
```
Generates SI elastic WIMP recoil-spectrum CSVs in `data/raw/` for benchmark masses: 5, 10, 20, 30, 40, 50, 70, 100, 150, 200 GeV.

**Step 2 — Run the likelihood workflow**

Run the likelihood workflow used in the project to evaluate the modeled spectra and produce:
- `data/processed/limit_curve.csv`

> Note: the reusable script `src/io/run_likelihood_scan.py` currently runs the single-spectrum toy example and writes `data/processed/likelihood_scan.csv`. The final `limit_curve.csv` was produced from the multi-mass project workflow.

---

## Output files

| File | Description |
|---|---|
| `data/processed/limit_curve.csv` | Benchmark masses and 90% upper limits — **final result** |
| `plots/limit_curve.png` | Mass-dependent limit curve — **final report figure** |

> **Note:** `data/processed/likelihood_scan.csv` and `data/raw/test_spectrum.csv` are development/diagnostic artefacts only and are not part of the final analysis.

---

## Diagnostic scripts (development only)
- `test_custom_csv_pipeline.py` — early pipeline test on the toy spectrum
- `plot_check/plot_likelihood_scan_annotated.py` — annotated likelihood-scan diagnostic plot
