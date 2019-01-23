import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse import linalg


def reconstruction(gx, gy):
    # Reconstruit une image à partir des gradients gx et gy.
    # Ne fonctionne que pour les images à niveaux de gris (pas de couleur).
    #
    # Note:
    #   Les gradients doivent être calculés à partir de la fonction 'diff'
    #   de Matlab. Par exemple:
    #
    #       gx = np.diff(im, 1, 1);
    #       gy = np.diff(im, 1, 0);
    #
    # ----------
    # Jean-Francois Lalonde
    # translation by Jinsong

    assert gx.ndim == 2 and gy.ndim == 2, 'Fonctionne seulement sur un canal à la fois!'
    nrows, _ = gx.shape
    _, ncols = gy.shape

    # gradients en x
    pxInd = np.arange(nrows * ncols).reshape(nrows, ncols)
    pxIndShift = np.roll(pxInd, shift=-1, axis=1)
    pxInd = pxInd[:, 0:-1]
    pxIndShift = pxIndShift[:, 0:-1]

    nrowsx, ncolsx = gx.shape
    gxInd = np.arange(nrowsx * ncolsx).reshape(nrowsx, ncolsx)

    rows_x = np.concatenate([gxInd, gxInd], axis=1)
    cols_x = np.concatenate([pxInd, pxIndShift], axis=1)
    vals_x = np.concatenate([-np.ones(pxInd.shape), np.ones(pxInd.shape)], axis=1)
    rhs_x = gx.flatten()

    # gradients en y
    pxInd = np.arange(nrows * ncols).reshape(nrows, ncols)
    pxIndShift = np.roll(pxInd, shift=-1, axis=0)
    pxInd = pxInd[0:-1, :]
    pxIndShift = pxIndShift[0:-1, :]

    nrowsy, ncolsy = gy.shape
    gyInd = np.arange(nrowsy * ncolsy).reshape(nrowsy, ncolsy)

    rows_y = np.concatenate([gyInd, gyInd], axis=1) + np.max(rows_x.flatten()) + 1
    cols_y = np.concatenate([pxInd, pxIndShift], axis=1)
    vals_y = np.concatenate([-np.ones(pxInd.shape), np.ones(pxInd.shape)], axis=1)
    rhs_y = gy.flatten()

    rows = np.concatenate([rows_x.flatten(), rows_y.flatten()], axis=0)
    cols = np.concatenate([cols_x.flatten(), cols_y.flatten()], axis=0)
    vals = np.concatenate([vals_x.flatten(), vals_y.flatten()], axis=0)

    lhs = csr_matrix((vals.astype('float16'), (rows.flatten(), cols.flatten())), shape=(rows.max() + 1, nrows * ncols))  # +1 (ind starts from 0)
    rhs = np.concatenate([rhs_x, rhs_y], axis=0)

    A = lhs.T * lhs
    b = lhs.T * rhs

    x = linalg.spsolve(A, b)  # much faster than lsqr

    im = x.reshape(nrows, ncols)
    return im
