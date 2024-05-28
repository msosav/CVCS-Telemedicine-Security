from .image import Image


class LZW:
    """
    LZW compression algorithm implementation.
    """

    def __init__(self, image_path):
        """
        Constructs all the necessary attributes for the LZW object.
        """
        self.Image = Image(image_path)

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
                if dictionary_size >= 65536:
                    dictionary = {chr(i): i for i in range(256)}
                    dictionary_size = 256
                dictionary[combined_string] = dictionary_size
                dictionary_size += 1
                current_string = symbol
        if current_string:
            compressed_data.append(dictionary[current_string])
        with open(compressed_path, 'wb') as file:
            for value in compressed_data:
                file.write(value.to_bytes(2, 'big'))

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
            if dictionary_size >= 65536:
                dictionary = {i: chr(i) for i in range(256)}
                dictionary_size = 256
            dictionary[dictionary_size] = previous_string + current_string[0]
            dictionary_size += 1
            previous_string = current_string
        image = self.Image.string_to_image(
            decompressed_data, self.Image.image_size)
        image.save(output_path)
