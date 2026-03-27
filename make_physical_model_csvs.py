from pathlib import Path
import numpy as np
import pandas as pd
from math import pi
from scipy.special import erf


C_KM_S = 299792.458
M_PROTON_GEV = 0.938272
A_XE = 131
M_NUCLEUS_GEV = A_XE * 0.9315

# Standard Halo Model choices
RHO_CHI = 0.3          # GeV / cm^3
V0 = 220.0             # km/s
VE = 232.0             # km/s
VESC = 544.0           # km/s

# Reference SI cross section
SIGMA_SI_REF = 1e-45   # cm^2


def reduced_mass(m1, m2):
    return (m1 * m2) / (m1 + m2)


def helm_form_factor_sq(E_keV, A=A_XE):
   
    m_nucleus = A * 0.9315  # GeV
    q_GeV = np.sqrt(2.0 * m_nucleus * E_keV * 1e-6)  # keV -> GeV
    q_fm = q_GeV * 5.067731

    s = 0.9
    a = 0.52
    c = 1.23 * A ** (1 / 3) - 0.60
    rn = np.sqrt(c**2 + (7.0 / 3.0) * pi**2 * a**2 - 5.0 * s**2)

    qr = q_fm * rn
    qs = q_fm * s

    F = np.ones_like(E_keV, dtype=float)

    mask = qr != 0
    j1 = np.zeros_like(E_keV, dtype=float)
    j1[mask] = (np.sin(qr[mask]) / qr[mask]**2) - (np.cos(qr[mask]) / qr[mask])

    F[mask] = 3.0 * j1[mask] / qr[mask] * np.exp(-(qs[mask] ** 2) / 2.0)
    F[~mask] = 1.0

    return F**2


def eta_shm(vmin, v0=V0, ve=VE, vesc=VESC):
   
    z = vesc / v0
    N = erf(z) - (2.0 / np.sqrt(np.pi)) * z * np.exp(-z**2)

    x = vmin / v0
    y = ve / v0

    eta = np.zeros_like(vmin, dtype=float)

    region1 = vmin < (vesc - ve)
    region2 = (vmin >= (vesc - ve)) & (vmin < (vesc + ve))

    eta[region1] = (
        erf(x[region1] + y)
        - erf(x[region1] - y)
        - (4.0 / np.sqrt(np.pi)) * y * np.exp(-z**2)
    ) / (2.0 * N * ve)

    eta[region2] = (
        erf(z)
        - erf(x[region2] - y)
        - (2.0 / np.sqrt(np.pi)) * (z - x[region2] + y) * np.exp(-z**2)
    ) / (2.0 * N * ve)

    eta[eta < 0] = 0.0
    return eta


def dRdE_physical(E_keV, mchi_GeV, sigma_si=SIGMA_SI_REF):
  
    mu_p = reduced_mass(mchi_GeV, M_PROTON_GEV)
    mu_A = reduced_mass(mchi_GeV, M_NUCLEUS_GEV)

    # vmin in km/s
    vmin = C_KM_S * np.sqrt((M_NUCLEUS_GEV * E_keV * 1e-6) / (2.0 * mu_A**2))

    F2 = helm_form_factor_sq(E_keV)
    eta = eta_shm(vmin)

    
    prefactor = sigma_si * (A_XE ** 2) * (mu_A**2 / mu_p**2) * RHO_CHI / mchi_GeV

    rate = 1e45 * prefactor * F2 * eta
# Fixed scale factor for numerical convenience only.
# Preserves relative normalization across masses.

    return rate


def save_spectrum_csv(mass_GeV, outdir):
    energies = np.arange(1, 71, 1, dtype=float)  # 1 to 70 keV
    rates = dRdE_physical(energies, mass_GeV)

    df = pd.DataFrame({
        "energy_keV": energies,
        "dRdE": rates
    })

    outfile = outdir / f"physical_wimp_{mass_GeV}GeV.csv"
    df.to_csv(outfile, index=False, header=False)
    print(f"Saved: {outfile}")


def main():
    outdir = Path("data/raw")
    outdir.mkdir(parents=True, exist_ok=True)

    masses = [5, 10, 20, 30, 40, 50, 70, 100, 150, 200]

    for mass in masses:
        save_spectrum_csv(mass, outdir)

    print("\nDone. Physical-model CSV files created in data/raw/")


if __name__ == "__main__":
    main()