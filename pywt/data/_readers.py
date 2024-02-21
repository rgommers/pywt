import functools
import importlib
import os

import numpy as np


@functools.cache
def ascent():
    """
    Get an 8-bit grayscale bit-depth, 512 x 512 derived image for
    easy use in demos

    The image is derived from accent-to-the-top.jpg at
    http://www.public-domain-image.com/people-public-domain-images-pictures/

    Parameters
    ----------
    None

    Returns
    -------
    ascent : ndarray
       convenient image to use for testing and demonstration

    Examples
    --------
    >>> import pywt.data
    >>> ascent = pywt.data.ascent()
    >>> ascent.shape == (512, 512)
    True
    >>> ascent.max()
    255

    >>> import matplotlib.pyplot as plt
    >>> plt.gray()
    >>> plt.imshow(ascent) # doctest: +ELLIPSIS
    <matplotlib.image.AxesImage object at ...>
    >>> plt.show() # doctest: +SKIP

    """
    _datadir = importlib.resources.files('pywt.data')
    with importlib.resources.as_file(_datadir.joinpath('ascent.npz')) as f:
        ascent = np.load(f)['data']

    return ascent


@functools.cache
def aero():
    """
    Get an 8-bit grayscale bit-depth, 512 x 512 derived image for
    easy use in demos

    Parameters
    ----------
    None

    Returns
    -------
    aero : ndarray
       convenient image to use for testing and demonstration

    Examples
    --------
    >>> import pywt.data
    >>> aero = pywt.data.ascent()
    >>> aero.shape == (512, 512)
    True
    >>> aero.max()
    255

    >>> import matplotlib.pyplot as plt
    >>> plt.gray()
    >>> plt.imshow(aero) # doctest: +ELLIPSIS
    <matplotlib.image.AxesImage object at ...>
    >>> plt.show() # doctest: +SKIP

    """
    _datadir = importlib.resources.files('pywt.data')
    with importlib.resources.as_file(_datadir.joinpath('aero.npz')) as f:
        aero = np.load(f)['data']

    return aero


@functools.cache
def camera():
    """
    Get an 8-bit grayscale bit-depth, 512 x 512 derived image for
    easy use in demos

    Parameters
    ----------
    None

    Returns
    -------
    camera : ndarray
       convenient image to use for testing and demonstration

    Notes
    -----
    No copyright restrictions. CC0 by the photographer (Lav Varshney).

    .. versionchanged:: 0.18
        This image was replaced due to copyright restrictions. For more
        information, please see [1]_, where the same change was made in
        scikit-image.

    References
    ----------
    .. [1] https://github.com/scikit-image/scikit-image/issues/3927

    Examples
    --------
    >>> import pywt.data
    >>> camera = pywt.data.ascent()
    >>> camera.shape == (512, 512)
    True

    >>> import matplotlib.pyplot as plt
    >>> plt.gray()
    >>> plt.imshow(camera) # doctest: +ELLIPSIS
    <matplotlib.image.AxesImage object at ...>
    >>> plt.show() # doctest: +SKIP

    """
    _datadir = importlib.resources.files('pywt.data')
    with importlib.resources.as_file(_datadir.joinpath('camera.npz')) as f:
        camera = np.load(f)['data']

    return camera


@functools.cache
def ecg():
    """
    Get 1024 points of an ECG timeseries.

    Parameters
    ----------
    None

    Returns
    -------
    ecg : ndarray
       convenient timeseries to use for testing and demonstration

    Examples
    --------
    >>> import pywt.data
    >>> ecg = pywt.data.ecg()
    >>> ecg.shape == (1024,)
    True

    >>> import matplotlib.pyplot as plt
    >>> plt.plot(ecg) # doctest: +ELLIPSIS
    [<matplotlib.lines.Line2D object at ...>]
    >>> plt.show() # doctest: +SKIP
    """
    _datadir = importlib.resources.files('pywt.data')
    with importlib.resources.as_file(_datadir.joinpath('ecg.npy')) as f:
        ecg = np.load(f)

    return ecg


@functools.cache
def nino():
    """
    This data contains the averaged monthly sea surface temperature in degrees
    Celsius of the Pacific Ocean, between 0-10 degrees South and 90-80 degrees West, from 1950 to 2016.
    This dataset is in the public domain and was obtained from NOAA.
    National Oceanic and Atmospheric Administration's National Weather Service
    ERSSTv4 dataset, nino 3, http://www.cpc.ncep.noaa.gov/data/indices/

    Parameters
    ----------
    None

    Returns
    -------
    time : ndarray
       convenient timeseries to use for testing and demonstration
    sst : ndarray
       convenient timeseries to use for testing and demonstration

    Examples
    --------
    >>> import pywt.data
    >>> time, sst = pywt.data.nino()
    >>> sst.shape == (264,)
    True

    >>> import matplotlib.pyplot as plt
    >>> plt.plot(time,sst) # doctest: +ELLIPSIS
    [<matplotlib.lines.Line2D object at ...>]
    >>> plt.show() # doctest: +SKIP
    """
    _datadir = importlib.resources.files('pywt.data')
    with importlib.resources.as_file(_datadir.joinpath('sst_nino3.npy')) as f:
        sst_csv = np.load(f)

    # sst_csv = pd.read_csv("http://www.cpc.ncep.noaa.gov/data/indices/ersst4.nino.mth.81-10.ascii", sep=' ', skipinitialspace=True)
    # take only full years
    n = int(np.floor(sst_csv.shape[0]/12.)*12.)
    # Building the mean of three months
    # the 4. column is nino 3
    sst = np.mean(np.reshape(np.array(sst_csv)[:n, 4], (n//3, -1)), axis=1)
    sst = (sst - np.mean(sst)) / np.std(sst, ddof=1)

    dt = 0.25
    time = np.arange(len(sst)) * dt + 1950.0  # construct time array
    return time, sst
