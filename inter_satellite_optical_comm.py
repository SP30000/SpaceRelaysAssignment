"""
Inter-Satellite Optical Communication Analysis
Author: SpaceRelays Assignment

This script performs an analysis to understand the impact of optical beam output power
on inter-satellite communication in outer space.

Assumptions:
- Wavelength: 1550 nm (typical for space optical communication)
- Transmitter and receiver aperture: 10 cm
- Beam divergence: based on diffraction limit
- Free-space (vacuum): no atmospheric attenuation
- SNR range for OOK: -2 dB to 7 dB
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erfc

# Constants
wavelength = 1550e-9  # 1550 nm
beam_diameter = 0.1   # 10 cm transmitter aperture
rx_aperture = 0.1     # 10 cm receiver aperture
tx_power_range = np.arange(0.1, 1.01, 0.01)  # 100 mW to 1 W
distances_km = np.array([200, 400, 600, 800, 1000])  # km
distances_m = distances_km * 1e3
snr_db_range = np.arange(-2, 8, 1)

# Beam divergence (diffraction-limited)
def beam_divergence(wavelength, diameter):
    return 1.22 * wavelength / diameter

theta = beam_divergence(wavelength, beam_diameter)

# Received power using geometric loss
def received_power(tx_power, distance):
    spot_radius = distance * theta / 2
    spot_area = np.pi * spot_radius ** 2
    rx_area = np.pi * (rx_aperture / 2) ** 2
    return tx_power * (rx_area / spot_area)

# BER for OOK modulation in AWGN
def ber_ook(snr_db):
    snr_linear = 10**(snr_db / 10)
    return 0.5 * erfc(np.sqrt(snr_linear / 2))

# Plot 1: Tx Power vs Rx Power
for d in distances_m:
    rx_powers = received_power(tx_power_range, d)
    plt.plot(tx_power_range * 1000, rx_powers * 1e6, label=f"{d/1e3:.0f} km")
plt.xlabel("Transmit Power (mW)")
plt.ylabel("Received Power (µW)")
plt.title("Transmit Power vs Received Power")
plt.legend()
plt.grid(True)
plt.savefig("tx_vs_rx_power.png")
plt.clf()

# Plot 2: BER vs SNR
for d in distances_m:
    ber_vals = ber_ook(snr_db_range)
    plt.semilogy(snr_db_range, ber_vals, label=f"{d/1e3:.0f} km")
plt.xlabel("SNR (dB)")
plt.ylabel("Bit Error Rate (BER)")
plt.title("BER vs SNR for OOK Modulation")
plt.legend()
plt.grid(True, which='both')
plt.savefig("ber_vs_snr.png")
