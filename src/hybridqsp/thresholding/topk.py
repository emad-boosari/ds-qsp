import numpy as np

def top_k_threshold(x, k):
    """
    Keep the k largest-magnitude coefficients of an array
    and set all remaining coefficients to zero.

    Parameters
    ----------
    x : np.ndarray
        Input array of arbitrary dimension.
    k : int
        Number of coefficients to retain.

    Returns
    -------
    np.ndarray
        Thresholded array with the same shape as ``x``.
    """

    x = np.asarray(x)

    if k < 0:
        raise ValueError("k must be non-negative.")

    if k == 0:
        return np.zeros_like(x)

    if k >= x.size:
        return x.copy()

    # Flatten for global thresholding
    flat = x.ravel()

    # Find indices of the k largest coefficients
    keep = np.argpartition(np.abs(flat), -k)[-k:]

    y = np.zeros_like(flat)
    y[keep] = flat[keep]

    return y.reshape(x.shape)