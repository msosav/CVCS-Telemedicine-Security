# CVCS - Telemedicine Security Project

## Overview

This project provides a simple implementation of the LZW (Lempel-Ziv-Welch) compression algorithm to compress and decompress images and [ ] to encrypt and decrypt the image.

## Requirements

- Python 3.6+
- PIL (Python Imaging Library)

  ```bash
    pip install pillow
  ```

## Installation

1. Clone the repository:

```bash
git clone https://github.com/msosav/cvcs-telemedicine-security.git
cd cvcs-telemedicine-security
```

## Usage

To use the `main.py` script, you need to provide three command-line arguments:

1. Path to the input image.
2. Path to save the compressed file.
3. Path to save the decompressed image.

### Command-Line Arguments

- `image_path`: The path to the input image file that you want to compress.
- `compressed_path`: The path where the compressed file will be saved.
- `decompressed_image_path`: The path where the decompressed image will be saved.

### Example Usage

To run the script, use the following command in your terminal:

```bash
python main.py path/to/input/image.png path/to/save/compressed_file.lzw path/to/save/decompressed_image.png
```

### Example

```bash
python main.py images/input.png compressed/output.lzw images/output.png
```

This command will:

1. Compress `images/input.png` to `compressed/output.lzw`.
2. Decompress `compressed/output.lzw` back to `images/output.png`.

## Project Structure

```plaintext
├── compression
│   ├── image.py
│   ├── __init__.py
│   └── lzw.py
├── docs
│   └── compression
│       ├── image.py.md
│       └── lzw.py.md
├── main.py
└── README.md
```
