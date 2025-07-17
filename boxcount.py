import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def boxcount(image_point, box_sizes, image_shape):
    """
    Computes the number of non-empty boxes of various sizes
    covering black pixels in the binary image.

    Parameters:
        image_point (ndarray): 2D array of image in point-type format.
        box_sizes (ndarray): 1D array of box sizes (ε values).
        image_shape (tuple): Shape of the binary image (rows, cols).

    Returns:
        list: Result of boxcounting, i.e., number of occupied boxes for each box size.
    """
    N = []
    rows, cols = image_point
    L_col = image_shape[0]
    for epsilon in box_sizes:
        box_row = rows // epsilon
        box_col = cols // epsilon
        serial = box_row - (-L_col//epsilon) * box_col
        N.append(len(np.unique(serial)))
    return N

if __name__ == '__main__':
    # === Parameters ===
    image_path = 'DLA.png'
    binary_threshold = 128

    # === Load and binarize image ===
    # Output: binary matrix where 1 = black, 0 = white
    image_matrix = np.where(
        np.array(Image.open(image_path).convert('L')) < binary_threshold, 1, 0
    )

    # === Image properties ===
    L_col, L_row = image_matrix.shape
    image_point = np.array(np.where(image_matrix == 1))

    # === Define box sizes ===
    max_len = max(L_col, L_row)
    box_sizes = 2 ** np.arange(int(np.ceil(np.log2(max_len))) + 1)

    # === Apply box-counting method ===
    N = boxcount(image_point, box_sizes, (L_col, L_row))

    # === Estimate fractal dimension D via least squares fit ===
    log_eps = -np.log(box_sizes)
    log_N = np.log(N)
    D, intercept = np.polyfit(log_eps, log_N, 1)

    # === Plot ===
    plt.figure()
    plt.scatter(box_sizes, N, label='Count')
    plt.plot(
        box_sizes,
        np.exp(intercept) * box_sizes ** (-D),
        label=f'$D = {D:.4f}$'
    )
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel(r'Box size $\varepsilon$')
    plt.ylabel(r'$N(\varepsilon)$')
    plt.legend()
    plt.title('Box-counting method')
    plt.grid(True, which='both', ls='--')
    plt.tight_layout()
    plt.show()
