from xe_likelihood import BinwiseInference, Spectrum
from scipy.optimize import minimize, brentq
import scipy.stats as sps
import numpy as np


def load_spectrum_from_csv(path, title="custom csv spectrum"):
    return Spectrum.from_csv(path, title=title)


def make_test_spectrum(mass=50):
    return Spectrum.from_wimp(mass=mass)


def make_xenon1t_inference(spectrum):
    return BinwiseInference.from_xenon1t_sr(spectrum=spectrum)


def likelihood_scan(inference, run=0, n_points=100):
    """
    Evaluate the likelihood-ratio function on the package's default x-grid.
    Returns arrays x and llr(x).
    """
    f_llr = inference.compute_likelihood_ratio(run=run)
    x = np.asarray(f_llr.x[:n_points], dtype=float)
    y = np.asarray([float(f_llr(val)) for val in x], dtype=float)
    return x, y


def safe_compute_ul(inference, cl=0.1, asymptotic=True, run=0):
    if asymptotic:
        threshold = lambda x: sps.chi2(1).isf(cl)
    else:
        mutot = inference.sum_spectrum_in_reconstructed_bins
        threshold = lambda x: inference.threshold_function(x * mutot)

    f_llr = inference.compute_likelihood_ratio(run=run)

    fmin = minimize(f_llr, [0.0], method="Powell")
    xmin = float(np.atleast_1d(fmin["x"])[0])
    llmin = float(fmin["fun"])

    def llz(x):
        return float(f_llr(x) - llmin - threshold(x))

    xmax = float(f_llr.x[-1])
    return brentq(llz, xmin, xmax)