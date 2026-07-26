import numpy as np

from qibo import Circuit, gates

from hybridqsp.transforms import dct_matrix


# ============================================================
# Quantum DCT
# ============================================================

def qdct(n):
    """
    Construct an n-qubit quantum DCT circuit.

    Parameters
    ----------
    n : int
        Number of qubits.

    Returns
    -------
    Circuit
        Quantum circuit implementing the orthonormal DCT.
    """

    N = 2 ** n

    U = dct_matrix(N)

    circuit = Circuit(n)

    circuit.add(
        gates.Unitary(
            U,
            *range(n)
        )
    )

    return circuit