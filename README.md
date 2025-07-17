# Box Counting for Fractal Dimension Estimation

This repository provides a fast Python script for the fractal dimension of a binary image using the box-counting method. A sample image (`DLA.png`) is included to demonstrate usage.

## Contents

- `boxcount.py`: Python script that performs the box-counting algorithm
- `DLA.png`: Sample binary image (Diffusion-Limited Aggregation)
- `README.md`: This documentation file

## Requirements

- Python 3.x
- numpy
- matplotlib
- pillow (PIL)

## Usage

```bash
python boxcount.py
```

The script will execute box-countmethod, generate a log-log plot, and estimate the fractal dimension $D$. ($D\approx1.64$ for the sample image.)

## License

This project is released under the MIT License.
