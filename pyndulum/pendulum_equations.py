"""Module implementing pendulum equations."""

import numpy as np

G = 9.81  # Acceleration due to gravity [m/s^2]
SECONDS_IN_MINUTE = 60.0  # Number of seconds in a minute


def get_period(length: float) -> float:
    """
    Calculate the period of a pendulum.

    Parameters
    ----------
    length : float
        length of the pendulum [m]

    Returns
    -------
    float
        period [s] for a swing of the pendulum
    """
    return 2.0 * np.pi * np.sqrt(length / G)


def max_height(length: float, theta: float) -> float:
    """
    Calculate the maximum height reached by a pendulum.

    Parameters
    ----------
    length : float
        length of the pendulum [m]
    theta : float
        maximum angle of displacment of the pendulum [radians]

    Returns
    -------
    float
        maximum vertical height [m] of the pendulum
    """
    return length * np.cos(theta)


def max_speed(length: float, theta: float) -> float:
    """
    Calculate the maximum speed of a pendulum.

    Parameters
    ----------
    length : float
        length of the pendulum [m]
    theta : float
        maximum angle of displacment of the pendulum [radians]

    Returns
    -------
    float
        maximum speed [m/s] of the pendulum
    """
    return np.sqrt(2.0 * G * max_height(length, theta))


def check_small_angle(theta: float) -> bool:
    """
    Check small angle approximation is valid.

    Parameters
    ----------
    theta : float
        maximum angle of displacment of the pendulum [radians]

    Returns
    -------
    bool
        is the small angle approximation valid for the input theta?
    """
    if theta <= np.pi / 1800.0:
        return True
    return False


def bpm(length: float) -> float:
    """
    Calculate pendulum frequency in beats per minute.

    Parameters
    ----------
    length : float
        length of the pendulum [m]

    Returns
    -------
    float
        pendulum frequency in beats per minute [1 / min]
    """
    return SECONDS_IN_MINUTE / get_period(length)


def calc_energy(mass: float, theta: float, length: float) -> float:
    """
    Calculate the total mechanical energy of a pendulum.

    Parameters
    ----------
    mass : float
        mass of the pendulum [kg]
    theta : float
        maximum angle of displacment of the pendulum [radians]
    length : float
        length of the pendulum [m]

    Returns
    -------
    float
        total mechanical energy [J] of the pendulum
    """
    return 0.5 * mass * max_speed(length, theta) ** 2
