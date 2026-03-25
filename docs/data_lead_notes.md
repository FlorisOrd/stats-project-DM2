# Data lead notes

## Role summary
Understand the XENON1T likelihood interface and data products. Provide project code to read spectra and evaluate the likelihood.

## Main interface used in our repo
- `Spectrum` for signal spectra
- `BinwiseInference.from_xenon1t_sr(...)` for the XENON1T likelihood object

## Current project wrapper
- `src/io/xenon_interface.py`

## Current pipeline
1. Read a custom spectrum CSV from `data/raw/`
2. Build the XENON1T inference object
3. Evaluate the likelihood-ratio curve
4. Save scan output to `data/processed/likelihood_scan.csv`
5. Compute a 90% upper limit with `safe_compute_ul(...)`

## Handoff to group
- Model lead should provide a spectrum in CSV form or equivalent project interface
- Inference lead can use the scan / UL functions
- Plot lead can use `data/processed/likelihood_scan.csv`