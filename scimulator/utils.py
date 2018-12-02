from numpy import ndarray
from typing import Dict
from scipy.stats import gamma


def gamma_reparam(mu: float, sd: float) -> Dict[str, float]:
    """Transforms mean and standard deviation parameters to `scipy.stats.gamma` parameters.

    The following transformation is computed and returned::

    .. math::
        a = \frac{\mu^2}{\sigma^2}\\
        scale = \frac{\sigma^2}{\mu}

    :param mu: mean of desired gamma distribution (>0)
    :param sd: standard deviation of desired gamma distribution (>0)
    :return {a, scale}: shape and scale parameters for `scipy.stats.gamma`
    """
    if not sd > 0:
        raise ValueError("`sd` must be positive! Found: %f" % sd)

    a = mu**2 / sd**2
    scale = sd**2/mu

    return {'a': a, 'scale': scale}


def rgamma(mu: float, sd: float, size: int) -> ndarray:
    """Samples gamma random variable with given moments.

    Provides a mean and standard deviation parameterization interface for `scipy.stats.gamma.rvs`

    :param mu: mean of desired gamma distribution (>0)
    :param sd: standard deviation of desired gamma distribution (>0)
    :param size: number of samples return
    :return: ndarray of samples
    """

    return gamma.rvs(**gamma_reparam(mu, sd), size=size)
