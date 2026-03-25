from xe_likelihood import BinwiseInference, Spectrum

print("Import worked")

spectrum = Spectrum.from_wimp(mass=50)
print("Spectrum created:", type(spectrum).__name__)

inference = BinwiseInference.from_xenon1t_sr(spectrum=spectrum)
print("Inference created:", type(inference).__name__)