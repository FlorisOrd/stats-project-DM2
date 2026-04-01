from pathlib import Path
import pandas as pd
from src.io.xenon_interface import (
    load_spectrum_from_csv,
    make_xenon1t_inference,
    safe_compute_ul,
)

def extract_mass(filename):
    name = filename.stem
    return float(name.split("_")[2].replace("GeV", ""))


def main():
    data_dir = Path("data/raw")
    files = sorted(data_dir.glob("physical_wimp_*GeV.csv"))

    results = []

    for file in files:
        mass = extract_mass(file)

        print(f"Processing {file.name} (mass = {mass} GeV)")

        spectrum = load_spectrum_from_csv(file)
        inference = make_xenon1t_inference(spectrum)
        ul = safe_compute_ul(inference, cl=0.1, asymptotic=True, run=0)

        print(f"UL = {ul}")

        results.append({
            "mass_GeV": mass,
            "upper_limit": float(ul),
        })

    results = sorted(results, key=lambda x: x["mass_GeV"])
    outdir = Path("data/processed")
    outdir.mkdir(parents=True, exist_ok=True)
    outpath = outdir / "limit_curve.csv"
    
    pd.DataFrame(results).to_csv(outpath, index=False)
    print("Saved to:", outpath)


if __name__ == "__main__":
    main()
