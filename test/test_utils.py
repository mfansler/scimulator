from unittest import TestCase
from scimulator.utils import *
import numpy as np
import scipy.stats as st


class TestUtils(TestCase):

    def test_gamma_reparam_moments(self):
        mu, sd = 300, 75
        m, v = st.gamma.stats(**gamma_reparam(mu, sd), moments="mv")
        self.assertAlmostEqual(mu, m)
        self.assertAlmostEqual(sd, np.sqrt(v))

    def test_rgamma_len(self):
        N = 41
        xs = rgamma(300, 75, size=N)
        self.assertEqual(len(xs), N)
