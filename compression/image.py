from PIL import Image as PILImage


class Image():
    """
    A class to represent an image file.
    """

    def __init__(self, image_path):
        """
        Constructs all the necessary attributes for the Image object.
        """
        self.image_path = image_path
        self.image_size = self.get_dimensions()

    def image_to_string(self):
        """
        Convert an image to a string of pixel values.

        Args:
            image_path (str): The path to the image file.

        Returns:
            str: A string representation of the pixel values in the image.
        """
        image = PILImage.open(self.image_path).convert(
            "L")
        pixels = list(image.getdata())
        return ''.join(chr(pixel) for pixel in pixels)

    def string_to_image(self, pixel_string, image_size):
        """
        Convert a string of pixel values back to an image.

        Args:
            pixel_string (str): A string containing pixel values.
            image_size (tuple): The size of the image (width, height).

        Returns:
            PIL.Image.Image: The reconstructed image.
        """
        pixel_values = [ord(char) for char in pixel_string]
        image = PILImage.new("L", image_size)
        image.putdata(pixel_values)
        return image

    def get_dimensions(self):
        """
        Get the dimensions of an image file.

        Args:
            image_path (str): The path to the image file.

        Returns:
            tuple: The dimensions of the image (width, height).
        """
        with PILImage.open(self.image_path) as image:
            return image.size

    def compress(self):
        """
        Compresses an image file using LZW compression algorithm.

        Args:
            image_path (str): The path to the input image file.
            output_path (str): The path to save the compressed output file.

        Returns:
            pixel_string (str): A string representation of the pixel values in the image.
        """
        pixel_string = self.image_to_string()

        return pixel_string

    def decompress(self, input_path):
        """
        Decompresses an image file using LZW compression algorithm.

        Args:
            input_path (str): The path to the compressed input file.
            output_image_path (str): The path to save the decompressed image.
            image_size (tuple): The size of the decompressed image (width, height).

        Returns:
            compressed (list): A list of integers representing the compressed data.
        """
        with open(input_path, 'rb') as f:
            compressed = []
            while True:
                bytes_pair = f.read(2)
                if not bytes_pair:
                    break
                compressed.append(int.from_bytes(bytes_pair, byteorder='big'))

        return compressed
