"""Routines for constructions states and Hamiltonians."""

import qutip
import numpy as np


def ket(labels):
    """Eigenstate of one or more Rydberg atoms.

    Args:
        labels (str): labels

    For example, `ket('i')` describes the state |i⟩ of a single atom and
    `ket('rr')` describes the state |r⟩⊗|r⟩ of two atoms.
    """
    levels = ['0', '1', 'i', 'r']
    states = []
    N = len(levels)
    for label in str(labels):
        states.append(qutip.basis(N, levels.index(label)))
    return qutip.tensor(*states)


def _H0_1q(E1, Δ1, Δ2):
    """Drift Hamiltonian for a single atom."""
    return qutip.Qobj(np.diag([0, E1, Δ1, Δ2]))


def _H_int(u):
    """Interaction Hamiltonian for two-atom system."""
    return u * ket('rr') * ket('rr').dag()


def ryd2_hamiltonian(E1, Δ1, Δ2, u, Ω_B_left, Ω_B_right, Ω_R_left, Ω_R_right):
    """Total Hamiltonian for the two-atom Rydberg system."""
    Id = qutip.identity(4)
    H0_1q = _H0_1q(E1=E1, Δ1=Δ1, Δ2=Δ2)
    H_int = _H_int(u)
    H0 = qutip.tensor(H0_1q, Id) + qutip.tensor(Id, H0_1q) + H_int
    H_1B = ket('0') * ket('i').dag() + ket('i') * ket('0').dag()
    H_1R = ket('i') * ket('r').dag() + ket('r') * ket('i').dag()
    H_B_left = qutip.tensor(H_1B, Id)
    H_B_right = qutip.tensor(Id, H_1B)
    H_R_left = qutip.tensor(H_1R, Id)
    H_R_right = qutip.tensor(Id, H_1R)
    H = [
        H0,
        [H_B_left, Ω_B_left],
        [H_B_right, Ω_B_right],
        [H_R_left, Ω_R_left],
        [H_R_right, Ω_R_left],
    ]
    return H
