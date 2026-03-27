# Dark Matter Project 2: XENON1T Approximate Nuclear-Recoil Likelihood

## Team members
- Floris Ordelmans - S5693705 (Data lead)
- Cristian Ioniță — S5299837
- Gianny Capitein - S4498313
- Yuval Rochman - S5411505
- Ivan Iturralde - S5325986 (Model Lead)

## Repository structure
- `data/` input data and processed data
- `src/` reusable analysis code
- `notebooks/` exploratory notebooks
- `plots/` generated figures

## Public data / external package
This project uses the public XENON1T approximate nuclear-recoil likelihood release.

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

### 3. Activate the virtual environment in VS Code PowerShell
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

### 4. Install project requirements
```powershell
python -m pip install --upgrade pip setuptools wheel
python -m pip install -r requirements.txt
```

### 5. Install the official XENON1T likelihood package
Clone the official package outside this repository, then install it into the active environment:

```powershell
cd ..
git clone https://github.com/XENON1T/xenon1t_approximate_nuclear_recoil_likelihood.git
cd xenon1t_approximate_nuclear_recoil_likelihood
python -m pip install .
cd ..\stats-project-DM2
```

## Input data format
Custom spectra for the likelihood pipeline are stored as CSV files in `data/raw/`.

Expected format:
- two numeric columns
- column 1: recoil energy
- column 2: differential rate

Current example input:
- `data/raw/test_spectrum.csv`

## Current reusable code
Main Data lead interface:
- `src/io/xenon_interface.py`

Current scripts:
- `test_custom_csv_pipeline.py`
- `src/io/run_likelihood_scan.py`

## How to run the current pipeline

### Test the custom spectrum pipeline
```powershell
python .\test_custom_csv_pipeline.py
```

This should:
- load `data/raw/test_spectrum.csv`
- build a `Spectrum`
- build a `BinwiseInference` object
- compute a 90% upper limit

### Run the reusable likelihood scan
```powershell
python .\src\io\run_likelihood_scan.py
```

This should:
- read the custom spectrum CSV
- build the XENON1T likelihood object
- evaluate the likelihood-ratio scan
- save the scan output to `data/processed/likelihood_scan.csv`
- print a 90% upper limit

## Output files
Main generated output:
- `data/processed/likelihood_scan.csv`

## Current project pipeline
1. Read a custom spectrum from `data/raw/`
2. Convert it into a `Spectrum` object
3. Build the XENON1T likelihood with `BinwiseInference.from_xenon1t_sr(...)`
4. Evaluate likelihood quantities
5. Save processed results to `data/processed/`
