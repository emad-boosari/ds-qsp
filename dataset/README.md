# PPG Dataset

This directory is intended for storing the photoplethysmography (PPG) signals used in the numerical experiments and hybrid quantum reconstruction examples of the `hybrid-qsp` repository.

The experiments in this repository investigate how transform-domain sparsity can be exploited for hybrid quantum state preparation using classical compression and quantum decompression techniques.

---

## Dataset Source

The PPG signals used in this work are obtained from the publicly available:

**BIDMC PPG and Respiration Dataset**  
available through [PhysioNet](https://physionet.org/content/bidmc/1.0.0/).

This dataset contains physiological recordings extracted from the MIMIC-II matched waveform database and includes:
- photoplethysmogram (PPG) signals,
- electrocardiogram (ECG) signals,
- impedance respiratory signals,
- respiratory annotations,
- and physiological parameters such as heart rate and oxygen saturation.

The recordings were acquired from critically ill patients at the Beth Israel Deaconess Medical Center (Boston, MA, USA). Each recording has a duration of approximately 8 minutes and physiological waveforms are sampled at 125 Hz.

---

## Purpose in This Repository

In this repository, the PPG signals are used to demonstrate:

- Haar packet decomposition of biomedical signals,
- transform-domain sparsification,
- sparse quantum state preparation,
- hybrid quantum reconstruction,
- and compression-fidelity trade-offs in realistic physiological data.

The processing pipeline is:

```text
PPG signal
    ↓
Haar packet transform
    ↓
Thresholding / sparsification
    ↓
Normalization
    ↓
Sparse quantum state preparation
    ↓
Quantum reconstruction
```

---

## Download Instructions

Please download the dataset manually from PhysioNet and place the desired files inside this directory.

Expected structure:

```text
ppg_dataset/
│
├── README.md
├── bidmc01.csv
├── bidmc02.csv
└── ...
```

The dataset is available in:
- WFDB format,
- CSV format,
- and MATLAB format.

For this repository, CSV or MATLAB formats are recommended for easier preprocessing in Python.

---

## Citation

If you use this dataset, please cite both the original dataset publication and PhysioNet.

### BIDMC Dataset

Pimentel, M. A. F., Johnson, A. E. W., Charlton, P. H., & Clifton, D. A.  
*Towards a Robust Estimation of Respiratory Rate from Pulse Oximeters.*  
IEEE Transactions on Biomedical Engineering, 64(8), 1914–1923, 2017.

DOI:  
https://doi.org/10.1109/TBME.2016.2613124

---

### PhysioNet

Goldberger, A. L., Amaral, L. A. N., Glass, L., et al.  
*PhysioBank, PhysioToolkit, and PhysioNet: Components of a New Research Resource for Complex Physiologic Signals.*  
Circulation, 101(23), e215–e220, 2000.

PhysioNet: [https://physionet.org/](https://physionet.org/)