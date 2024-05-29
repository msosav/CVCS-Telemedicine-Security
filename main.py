import argparse
from compression.lzw import LZW
from encryption import rsa


def parse_arguments():
    parser = argparse.ArgumentParser(description='CVCS Telemedicine Security')
    parser.add_argument('image_path', type=str, help='Path to the input image')
    parser.add_argument('compressed_path', type=str,
                        help='Path to save the compressed file')
    parser.add_argument('decompressed_image_path', type=str,
                        help='Path to save the decompressed image')
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_arguments()
    lzw = LZW(args.image_path)
    #lzw.compress(args.compressed_path)
    #rsa(args.compressed_path)
    lzw.decompress(args.compressed_path, args.decompressed_image_path)
