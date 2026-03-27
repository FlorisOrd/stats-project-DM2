from src.io.xenon_interface import (
    load_spectrum_from_csv,
    make_xenon1t_inference,
    safe_compute_ul,
)

files = {
    5: "data/raw/physical_wimp_5GeV.csv",
    10: "data/raw/physical_wimp_10GeV.csv",
    20: "data/raw/physical_wimp_20GeV.csv",
    30: "data/raw/physical_wimp_30GeV.csv",
    40: "data/raw/physical_wimp_40GeV.csv",
    50: "data/raw/physical_wimp_50GeV.csv",
    70: "data/raw/physical_wimp_70GeV.csv",
    100: "data/raw/physical_wimp_100GeV.csv",
    150: "data/raw/physical_wimp_150GeV.csv",
    200: "data/raw/physical_wimp_200GeV.csv",
}

print("Running CSV model scan...\n")

for mass, path in files.items():
    spectrum = load_spectrum_from_csv(path, title=f"WIMP {mass} GeV")
    print("Spectrum OK:", type(spectrum).__name__)
    print("Using file:", path)

    inference = make_xenon1t_inference(spectrum)
    ul = safe_compute_ul(inference, cl=0.1, asymptotic=True, run=0)

    print(f"Mass = {mass} GeV -> Asymptotic 90% UL = {ul}")
    print("-" * 50)