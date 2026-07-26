"""
Discrete Cosine Transform (DCT)
===============================

This module implements orthonormal one-dimensional and
two-dimensional DCT transforms suitable for hybrid
quantum state preparation.

The implementation follows the DCT-II convention with
orthonormal normalization, making the transform unitary:

    D @ D.T = I

The inverse transform is therefore simply the transpose
of the DCT matrix.
"""

import numpy as np


# ============================================================
# Orthonormal DCT-II matrix
# ============================================================

def dct_matrix(N):
    """
    Construct the NxN orthonormal DCT-II matrix.

    Parameters
    ----------
    N : int
        Transform size.

    Returns
    -------
    np.ndarray
        Orthonormal DCT matrix.
    """

    U = np.zeros((N, N), dtype=float)

    for u in range(N):

        alpha = np.sqrt(1 / N) if u == 0 else np.sqrt(2 / N)

        for x in range(N):

            U[u, x] = (
                alpha
                * np.cos(np.pi * (2 * x + 1) * u / (2 * N))
            )

    return U


# ============================================================
# 1D DCT
# ============================================================

def dct(x):
    """
    Compute the orthonormal DCT-II of a one-dimensional signal.

    Parameters
    ----------
    x : np.ndarray
        Input vector.

    Returns
    -------
    np.ndarray
        DCT coefficients.
    """

    x = np.asarray(x)

    U = dct_matrix(len(x))

    return U @ x


# ============================================================
# 1D inverse DCT
# ============================================================

def idct(X):
    """
    Compute the inverse orthonormal DCT.

    Parameters
    ----------
    X : np.ndarray
        DCT coefficients.

    Returns
    -------
    np.ndarray
        Reconstructed signal.
    """

    X = np.asarray(X)

    U = dct_matrix(len(X))

    return U.T @ X


# ============================================================
# 2D DCT
# ============================================================

def dct2(A):
    """
    Compute the orthonormal two-dimensional DCT.

    Parameters
    ----------
    A : np.ndarray
        Two-dimensional input array.

    Returns
    -------
    np.ndarray
        Two-dimensional DCT coefficients.
    """

    A = np.asarray(A)

    if A.ndim != 2:
        raise ValueError("Input must be a 2D array.")

    m, n = A.shape

    Um = dct_matrix(m)
    Un = dct_matrix(n)

    return Um @ A @ Un.T


# ============================================================
# 2D inverse DCT
# ============================================================

def idct2(B):
    """
    Compute the inverse orthonormal two-dimensional DCT.

    Parameters
    ----------
    B : np.ndarray
        Two-dimensional DCT coefficients.

    Returns
    -------
    np.ndarray
        Reconstructed array.
    """

    B = np.asarray(B)

    if B.ndim != 2:
        raise ValueError("Input must be a 2D array.")

    m, n = B.shape

    Um = dct_matrix(m)
    Un = dct_matrix(n)

    return Um.T @ B @ Un