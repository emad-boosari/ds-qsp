# DS-QSP: Dense-to-Sparse Quantum State Preparation via Reversible Classical Compression
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

A modular research framework for hybrid quantum state preparation using classical transform-domain compression techniques such as Fourier and Haar packet wavelet sparsification.

---

## Overview

Quantum state preparation is one of the central bottlenecks in many quantum algorithms. This repository explores hybrid quantum-classical strategies in which classical compression methods are applied prior to quantum encoding in order to reduce quantum resource requirements while preserving reconstruction fidelity.

The framework combines:
- classical transform-domain compression,
- sparse quantum state preparation,
- inverse quantum transformations,
- and reconstruction-fidelity analysis.

The current implementation includes Fourier-based and Haar-based hybrid quantum reconstruction workflows using Qibo quantum circuits.

---

## Repository Structure

```text
hybrid-qsp/
│
├── src/
│   └── hybridqsp/
│       ├── transforms/
│       ├── thresholding/
│       ├── metrics/
│       ├── quantum/
│       └── analysis/
│
├── notebooks/
│
├── figures/
│
├── ppg_dataset/
│
├── LICENSE
├── requirements.txt
└── README.md
```

---

## Hybrid-QSP Workflow

A detailed description of the Hybrid Quantum State Preparation (Hybrid-QSP) workflow and the associated numerical demonstrations is provided in the [notebooks documentation](notebooks/README.md).



---

## Included Demonstrations

The repository currently includes examples for:

- Multi-frequency signals
- Piecewise-constant signals
- Sinc signals
- Single-Gaussian signals
- Multi-Gaussian signals
- PPG biomedical signals

These examples demonstrate transform-domain sparsification, sparse quantum state preparation, and inverse quantum reconstruction workflows.

---

## Citation

If you use this repository in academic work, please cite:

```bibtex
@misc{hybridqsp2025,
  title={Hybrid Quantum State Preparation via Classical Compression and Quantum Decompression},
  author={E. Rezaei Fard Boosari, M. Afsary},
  year={2025},
  archivePrefix={arXiv},
  eprint={2512.01798},
  primaryClass={quant-ph}
}
```

---

## Associated Paper

This repository accompanies the following research manuscript:

**Hybrid Quantum State Preparation via Classical Compression and Quantum Decompression**  
https://arxiv.org/abs/2512.01798

---

## License

This project is released under the MIT License.
