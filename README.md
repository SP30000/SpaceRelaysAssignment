# SpaceRelays: Optical Inter-Satellite Communication Analysis

This project analyzes the impact of optical beam output power on inter-satellite communication in outer space.


- `inter_satellite_optical_comm.py` — Python 3 code for beam modeling and BER analysis
- `SpaceRelays_Report.pdf` — Summary of assumptions, equations, plots, and key results
- `tx_vs_rx_power.png` — Transmit Power vs Received Power graph
- `ber_vs_snr.png` — BER vs SNR for OOK modulation


- Wavelength: 1550 nm
- Tx/Rx Aperture: 10 cm
- Distance range: 200 km to 1000 km
- SNR range: -2 dB to 7 dB
- Modulation: On-Off Keying (OOK)

Results
- Beam divergence increases spot size at longer distances, reducing received power
- BER improves as SNR increases, as expected in AWGN channels

-
