import numpy as np

# use nansum from bottleneck if it's installed, otherwise use the numpy one
try:
    import bottleneck as bn
    nansum = bn.nansum
except ImportError:
    nansum = np.nansum


def mms_pgs_make_e_spec(data_in):
    """
    Builds an energy spectrogram from a simplified particle data structure.

    Parameters
    ----------
    data_in : dict
        The input data structure.

    Returns
    -------
    outtable : ndarray, shape (ny,)
        The energy bins.
    ave : ndarray, shape (ny,)
        The spectrogram.

    Notes
    -----
    - Each energy bin in the output spectrogram (`ave`) is the weighted average
      of the corresponding bins in the input data (`data_in`).
    - The input data is sanitized by zeroing inactive bins to ensure areas with
      no data are represented as NaN.
    - The function uses the first energy table for rebinning the data.
    """
    data = data_in.copy()

    # zero inactive bins to ensure areas with no data are represented as NaN
    zero_bins = np.argwhere(data['bins'] == 0)
    if zero_bins.size != 0:
        for item in zero_bins:
            data['data'][item[0], item[1]] = 0.0

    # use the original energy table for now
    outtable = data['orig_energy']
    outbins = np.zeros([len(data['data'][:, 0]), len(data['data'][0, :])])

    # energy range to accept (this is questionable, but matches IDL)
    # TODO: Take a closer look at this logic.  Should we be comparing to the energy bin _center_ values?
    # The IDL version accepts an 'energy' parameter to define energy limits; that feature may no longer be used though?

    erange = [np.min(data['energy']), np.max(data['energy'])]

    # rebin the data to the original energy table
    for ang_idx in range(0, len(data['data'][0, :])):
        etable = data['energy'][:, ang_idx]
        for binidx in range(0, len(outtable)):
            if data['data'][binidx, ang_idx] != 0.0:
                this_en = find_nearest_neighbor(outtable, [etable[binidx]])
                whereen = np.argwhere(outtable == this_en)
                outbins[whereen, ang_idx] += data['data'][binidx, ang_idx]

    # check for out of range values (questionable but matches IDL)
    where_out_of_erange = np.argwhere((outtable < erange[0]) | (outtable > erange[1]))
    if where_out_of_erange.size != 0:
        outbins[where_out_of_erange] = np.nan

    # If we want to use NaN as a marker for unused bins, we need to use sum rather than nansum here.

    if len(data['data'][0, :]) > 1:
        ave = np.sum(outbins, axis=1)/np.sum(data['bins'], axis=1)
    else:
        ave = outbins/data['bins']

    return outtable, ave


def find_nearest_neighbor(table, item):
    table = np.array(table)
    return min(table, key=lambda p: sum((p - item)**2))
