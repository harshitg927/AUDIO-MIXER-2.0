import numpy as np

from scipy import integrate
from astropy.modeling.models import BlackBody
from astropy import units as u, constants as c

import matplotlib.pyplot as plt

bb = BlackBody(5000. * u.Kelvin)

nu = np.linspace(1., 3000., 1000) * u.THz
bb5000K_nu = bb(nu)
plt.plot(nu, bb5000K_nu)
plt.xlabel(r', [{0:latex_inline}]'.format(nu.unit))
plt.ylabel(r', ' + '[{0:latex_inline}]'.format(bb5000K_nu.unit))
plt.title('Planck Function in frequency')
plt.show()

