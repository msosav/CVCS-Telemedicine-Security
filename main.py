# python main.py 61 53 ./images/input.bmp ./results/compressed.lzw ./results/encrypted.rsa ./results/decrypted.lzw ./results/decompressed.bmp

import argparse
from compression.lzw import LZW
from encryption.rsa import RSA


def parse_arguments():
    parser = argparse.ArgumentParser(description='CVCS Telemedicine Security')
    parser.add_argument('p', type=int, help='First prime number')
    parser.add_argument('q', type=int, help='Second prime number')
    parser.add_argument('image_path', type=str, help='Path to the input image')
    parser.add_argument('compressed_path', type=str,
                        help='Path to save the compressed file')
    parser.add_argument('encrypted_path', type=str,
                        help='Path to save the encrypted file')
    parser.add_argument('decrypted_path', type=str,
                        help='Path to save the decrypted file')
    parser.add_argument('decompressed_image_path', type=str,
                        help='Path to save the decompressed image')
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_arguments()
    lzw = LZW(args.image_path)
    rsa = RSA(args.p, args.q, args.compressed_path,
              args.encrypted_path, args.decrypted_path)
    lzw.compress(args.compressed_path)
    rsa.encrypt_file(args.compressed_path)
    rsa.decrypt_file()
    lzw.decompress(args.decrypted_path, args.decompressed_image_path)
