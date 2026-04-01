from pathlib import Path
import pandas as pd

from src.io.xenon_interface import (
    make_test_spectrum,
    make_xenon1t_inference,
    safe_compute_ul,
)

def main():
    masses = [50]

    results = []

    for mass in masses:
        print(f"Processing mass = {mass} GeV")

        spectrum = make_test_spectrum(mass=mass)
        inference = make_xenon1t_inference(spectrum)

        ul = safe_compute_ul(inference, cl=0.1, asymptotic=True, run=0)

        print(f" -> UL = {ul}")

        results.append({
            "mass_GeV": mass,
            "upper_limit": float(ul),
        })

    outdir = Path("data/processed")
    outdir.mkdir(parents=True, exist_ok=True)

    outpath = outdir / "limit_curve.csv"
    pd.DataFrame(results).to_csv(outpath, index=False)

    print("Saved to:", outpath)


if __name__ == "__main__":
    main()