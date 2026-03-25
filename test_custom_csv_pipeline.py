from src.io.xenon_interface import (
    load_spectrum_from_csv,
    make_xenon1t_inference,
    safe_compute_ul,
)

spectrum = load_spectrum_from_csv(
    "data/raw/test_spectrum.csv",
    title="toy custom spectrum"
)
print("Spectrum OK:", type(spectrum).__name__)

inference = make_xenon1t_inference(spectrum)
print("Inference OK:", type(inference).__name__)
print("Runs available:", inference.run_count)
print("True-energy bins:", len(inference.true_energy_bins))
print("Reco-energy bins:", len(inference.reconstructed_energy_bins))

ul = safe_compute_ul(inference, cl=0.1, asymptotic=True, run=0)
print("Asymptotic 90% UL (signal multiple):", ul)