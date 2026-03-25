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


def safe_compute_ul(inference, cl=0.1, asymptotic=True, run=0):
    """
    Work around the package's compute_ul issue by forcing xmin to be a scalar.
    """
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

    # Optional debug prints
    print("xmin =", xmin)
    print("xmax =", xmax)
    print("llz(xmin) =", llz(xmin))
    print("llz(xmax) =", llz(xmax))

    return brentq(llz, xmin, xmax)