# lzw.py

## Constructor

### `__init__`

```python
def __init__(self, image_path):
    """
    Constructs all the necessary attributes for the LZW object.
    """
    self.Image = Image(image_path)
```

The constructor method `__init__` initializes an `LZW` object by creating an instance of the `Image` class with the provided image path.

## Instance Methods

### `compress`

```python
def compress(self, compressed_path):
    """
    Compresses a given string using the LZW compression algorithm.

    Parameters:
        compressed_path (str): The path to save the compressed output file.

    Returns:
        None
    """
    uncompressed_string = self.Image.compress()
    dictionary_size = 256
    dictionary = {chr(i): i for i in range(dictionary_size)}
    current_string = ""
    compressed_data = []
    for symbol in uncompressed_string:
        combined_string = current_string + symbol
        if combined_string in dictionary:
            current_string = combined_string
        else:
            compressed_data.append(dictionary[current_string])
            dictionary[combined_string] = dictionary_size
            dictionary_size += 1
            current_string = symbol
    if current_string:
        compressed_data.append(dictionary[current_string])
    with open(compressed_path, 'wb') as file:
        for value in compressed_data:
            file.write(value.to_bytes(2, 'big'))
```

This method compresses the pixel values of an image (as a string) using the LZW compression algorithm and writes the compressed data to a file. It creates an initial dictionary with single characters, iterates over the input string to build longer sequences, and stores their corresponding codes. The compressed data is then saved to the specified file.

### `decompress`

```python
def decompress(self, compressed_path, output_path):
    """
    Decompresses a string using the LZW algorithm.

    Args:
        compressed_path (str): The path to the file containing the compressed string.
        output_path (str): The path to save the decompressed image.

    Returns:
        None

    Raises:
        ValueError: If the compressed string contains invalid characters.
    """
    compressed = self.Image.decompress(compressed_path)
    dictionary_size = 256
    dictionary = {i: chr(i) for i in range(dictionary_size)}
    compressed_iter = iter(compressed)
    previous_string = decompressed_data = chr(next(compressed_iter))
    for code in compressed_iter:
        if code in dictionary:
            current_string = dictionary[code]
        elif code == dictionary_size:
            current_string = previous_string + previous_string[0]
        else:
            raise ValueError(f'Bad compressed code: {code}')
        decompressed_data += current_string
        dictionary[dictionary_size] = previous_string + current_string[0]
        dictionary_size += 1
        previous_string = current_string
    image = self.Image.string_to_image(
        decompressed_data, self.Image.image_size)
    image.save(output_path)
```

This method decompresses the LZW-compressed data from a file and reconstructs the image. It reads the compressed codes, decodes them using a dictionary, and rebuilds the original string of pixel values. The reconstructed string is then converted back into an image and saved to the specified output path. If an invalid code is encountered, it raises a `ValueError`.
