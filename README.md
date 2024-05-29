# CVCS - Telemedicine Security Project

## Overview

This project provides a simple implementation of the LZW (Lempel-Ziv-Welch) compression algorithm to compress and decompress images and RSA to encrypt and decrypt the image.

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

1. The first prime number.
2. The second prime number.
3. Path to the input image.
4. Path to save the compressed file.
5. Path to save the encrypted file.
6. Path to save the decrypted file.
7. Path to save the decompressed image.

### Command-Line Arguments

- `p`: The first prime number.
- `q`: The second prime number.
- `image_path`: The path to the input image file that you want to compress.
- `compressed_path`: The path where the compressed file will be saved.
- `encrypted_path`: The path where the encrypted file will be saved.
- `decrypted_path`: The path where the decrypted file will be saved.
- `decompressed_image_path`: The path where the decompressed image will be saved.

### Example Usage

To run the script, use the following command in your terminal:

```bash
python main.py 61 53 ./images/input.bmp ./results/compressed.lzw ./results/encrypted.rsa ./results/decrypted.lzw ./results/decompressed.bmp
```

This command will:

1. Compress the input image using the LZW algorithm.
2. Encrypt the compressed file using the RSA algorithm.
3. Decrypt the encrypted file using the RSA algorithm.
4. Decompress the decrypted file using the LZW algorithm.

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
