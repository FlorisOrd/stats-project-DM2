from pathlib import Path
import numpy as np

from src.io.xenon_interface import (
    load_spectrum_from_csv,
    make_xenon1t_inference,
    likelihood_scan,
    safe_compute_ul,
)


def main():
    spectrum = load_spectrum_from_csv(
        "data/raw/physical_wimp_50GeV.csv",
        title="physical WIMP 50 GeV"
    )

    inference = make_xenon1t_inference(spectrum)

    x, y = likelihood_scan(inference, run=0, n_points=100)
    ul = safe_compute_ul(inference, cl=0.1, asymptotic=True, run=0)

    outdir = Path("data/processed")
    outdir.mkdir(parents=True, exist_ok=True)

    outpath = outdir / "likelihood_scan.csv"
    np.savetxt(
        outpath,
        np.column_stack([x, y]),
        delimiter=",",
        header="signal_strength,llr",
        comments=""
    )

    print("Saved likelihood scan to:", outpath)
    print("90% UL =", ul)


if __name__ == "__main__":
    main()
