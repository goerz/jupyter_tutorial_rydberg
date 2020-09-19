"""Plotting routines."""
import matplotlib.pylab as plt
import numpy as np


GHz = 2 * np.pi
MHz = 1e-3 * GHz
ns = 1


def plot_pulse(func, tlist, args=None, unit='MHz'):
    """Plot the given control function."""
    fig, ax = plt.subplots()
    vals = np.array([func(t, args) for t in tlist])
    if unit == 'MHz':
        vals /= MHz
    elif unit == 'GHz':
        vals /= GHz
    else:
        raise ValueError("Invalid unit")
    ax.plot(tlist, vals, label=func.__name__)
    ax.set_xlabel('time (ns)')
    ax.set_ylabel('amplitude (%s)' % unit)
    ax.legend()
    return fig, ax
