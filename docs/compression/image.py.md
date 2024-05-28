# image.py

## Constructor

### `__init__`

```python
def __init__(self, image_path):
    """
    Constructs all the necessary attributes for the Image object.
    """
    self.image_path = image_path
    self.image_size = self.get_dimensions()
```

The constructor method `__init__` initializes an `Image` object with the path to the image file. It sets `self.image_path` to the provided path and calculates the image dimensions by calling `self.get_dimensions()`.

## Instance Methods

### `image_to_string`

```python
def image_to_string(self):
    """
    Convert an image to a string of pixel values.

    Returns:
        str: A string representation of the pixel values in the image.
    """
    image = PILImage.open(self.image_path).convert("L")  # Convert to grayscale
    pixels = list(image.getdata())
    return ''.join(chr(pixel) for pixel in pixels)
```

This method opens the image file, converts it to grayscale, and then converts the pixel values to a string where each pixel value is represented by a character.

### `string_to_image`

```python
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
```

This method takes a string of pixel values and the dimensions of the image, converts the string back into a list of pixel values, and reconstructs the image in grayscale.

### `get_dimensions`

```python
def get_dimensions(self):
    """
    Get the dimensions of an image file.

    Returns:
        tuple: The dimensions of the image (width, height).
    """
    with PILImage.open(self.image_path) as image:
        return image.size
```

This method opens the image file, retrieves its dimensions (width and height), and returns them as a tuple.

### `compress`

```python
def compress(self):
    """
    Compresses an image file using LZW compression algorithm.

    Returns:
        str: A string representation of the pixel values in the image.
    """
    pixel_string = self.image_to_string()
    return pixel_string
```

This method converts the image to a string of pixel values, preparing it for compression. Although it mentions LZW compression in the docstring, it currently returns the string representation of the pixel values without actual compression.

### `decompress`

```python
def decompress(self, input_path):
    """
    Decompresses an image file using LZW compression algorithm.

    Args:
        input_path (str): The path to the compressed input file.

    Returns:
        list: A list of integers representing the compressed data.
    """
    with open(input_path, 'rb') as f:
        compressed = []
        while True:
            bytes_pair = f.read(2)
            if not bytes_pair:
                break
            compressed.append(int.from_bytes(bytes_pair, byteorder='big'))

    return compressed
```

This method reads a file containing compressed data and returns it as a list of integers. The docstring indicates LZW decompression, but the method currently only reads the data without performing actual decompression.
