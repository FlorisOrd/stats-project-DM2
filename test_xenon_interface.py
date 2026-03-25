from src.io.xenon_interface import make_test_spectrum, make_xenon1t_inference

spectrum = make_test_spectrum(mass=50)
print("Spectrum OK:", type(spectrum).__name__)

inference = make_xenon1t_inference(spectrum)
print("Inference OK:", type(inference).__name__)

print("Runs available:", inference.run_count)
print("True-energy bins:", len(inference.true_energy_bins))
print("Reco-energy bins:", len(inference.reconstructed_energy_bins))