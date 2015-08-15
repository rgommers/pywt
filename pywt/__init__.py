# -*- coding: utf-8 -*-
# flake8: noqa

# Copyright (c) 2006-2012 Filip Wasilewski <http://en.ig.ma/>
# See COPYING for license details.

"""
Discrete forward and inverse wavelet transform, stationary wavelet transform,
wavelet packets signal decomposition and reconstruction module.
"""

from __future__ import division, print_function, absolute_import

# Set up metamodule. This has to be before any other imports that
# might touch pywt.
from ._metamodule import install
install(__name__)
del(install)

from ._pywt import *
from ._functions import *
from ._multilevel import *
from ._multidim import *
from ._thresholding import *
from ._wavelet_packets import *


__all__ = [s for s in dir() if not s.startswith('_')]

from pywt.version import version as __version__

from numpy.testing import Tester
test = Tester().test

_MODES_warning = DeprecationWarning("`MODES` has been renamed to `Modes` "
                                    "and will be inaccessible as `MODES` "
                                    "in a future version of pywt.")

__warn_on_access__['MODES'] = (Modes, _MODES_warning)
