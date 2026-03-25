from xe_likelihood import BinwiseInference, Spectrum


def make_test_spectrum(mass=50):
    """Return one of the package's built-in demo WIMP spectra."""
    return Spectrum.from_wimp(mass=mass)


def make_xenon1t_inference(spectrum):
    """Build the XENON1T signal-region likelihood object."""
    return BinwiseInference.from_xenon1t_sr(spectrum=spectrum)