"""
Hadamard (Walsh-Hadamard) transforms.

The transform implemented here is exactly H^{⊗n}, where H is the
single-qubit Hadamard matrix. Consequently, the inverse transform is
identical to the forward transform, matching the quantum implementation.
"""

import numpy as np


# ============================================================
# Hadamard matrix
# ============================================================

def hadamard_matrix(nqubits):
    """
    Construct the normalized Hadamard matrix H^{⊗n}.

    Parameters
    ----------
    nqubits : int
        Number of qubits.

    Returns
    -------
    ndarray
        2^n x 2^n orthogonal Hadamard matrix.
    """

    H1 = np.array([[1, 1],
                   [1,-1]], dtype=float) / np.sqrt(2)

    H = H1.copy()

    for _ in range(nqubits - 1):
        H = np.kron(H, H1)

    return H


# ============================================================
# 1D Transform
# ============================================================

def hadamard_transform(x):
    """
    Apply H^{⊗n} to a vector.
    """

    x = np.asarray(x, dtype=float)

    N = len(x)

    nqubits = int(np.log2(N))

    if 2**nqubits != N:
        raise ValueError("Vector length must be a power of two.")

    H = hadamard_matrix(nqubits)

    return H @ x


def inverse_hadamard_transform(x):
    """
    Since H^{⊗n} is self-inverse.
    """

    return hadamard_transform(x)


# ============================================================
# 2D Transform
# ============================================================

def hadamard_transform_2d(image):
    """
    Apply separable 2D Hadamard transform.
    """

    image = np.asarray(image, dtype=float)

    rows, cols = image.shape

    if rows != cols:
        raise ValueError("Image must be square.")

    nqubits = int(np.log2(rows))

    if 2**nqubits != rows:
        raise ValueError("Image dimension must be a power of two.")

    H = hadamard_matrix(nqubits)

    return H @ image @ H


def inverse_hadamard_transform_2d(coeffs):
    """
    Inverse separable Hadamard transform.
    """

    return hadamard_transform_2d(coeffs)