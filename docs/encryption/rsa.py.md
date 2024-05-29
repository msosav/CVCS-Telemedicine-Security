# rsa.py

## Constructor

### `__init__`

```python
def __init__(self, p, q, compressed_path, encrypted_path, decrypted_path):
    """
    Constructs all the necessary attributes for the RSA object.
    """
    self.public_key, self.private_key = self.generate_keypair(p, q)
    self.compressed_path = compressed_path
    self.encrypted_path = encrypted_path
    self.decrypted_path = decrypted_path
```

The constructor method `__init__` initializes an `RSA` object with prime numbers `p` and `q`, and file paths for the compressed, encrypted, and decrypted files. It generates the public and private keys using these prime numbers and stores the file paths.

## Instance Methods

### `is_prime`

```python
def is_prime(self, n):
    """
    Check if a number is prime.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
```

This method checks if a number `n` is prime. It returns `True` if the number is prime and `False` otherwise.

### `gcd`

```python
def gcd(self, a, b):
    """
    Calculate the greatest common divisor of two numbers.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The greatest common divisor.
    """
    while b != 0:
        a, b = b, a % b
    return a
```

This method calculates the greatest common divisor (GCD) of two numbers `a` and `b` using the Euclidean algorithm.

### `mod_inverse`

```python
def mod_inverse(self, e, phi):
    """
    Calculate the modular inverse of a number.

    Args:
        e (int): The number.
        phi (int): The totient of the number.

    Returns:
        int: The modular inverse.
    """
    def egcd(a, b):
        """
        Calculate the extended Euclidean algorithm.

        Args:
            a (int): The first number.
            b (int): The second number.

        Returns:
            tuple: The greatest common divisor and the coefficients.
        """
        if a == 0:
            return b, 0, 1
        g, x1, y1 = egcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return g, x, y

    g, x, y = egcd(e, phi)
    if g != 1:
        raise Exception('Modular inverse does not exist.')
    else:
        return x % phi
```

This method calculates the modular inverse of `e` modulo `phi` using the extended Euclidean algorithm. If the modular inverse does not exist, it raises an exception.

### `generate_keypair`

```python
def generate_keypair(self, p, q):
    """
    Generate a public and private key pair.

    Args:
        p (int): A prime number.
        q (int): Another prime number.

    Returns:
        tuple: The public and private key pairs.
    """
    if not (self.is_prime(p) and self.is_prime(q)):
        raise ValueError("Both numbers must be prime.")
    n = p * q
    phi = (p - 1) * (q - 1)
    e = random.randrange(1, phi)
    g = self.gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = self.gcd(e, phi)

    d = self.mod_inverse(e, phi)
    return ((e, n), (d, n))
```

This method generates a pair of RSA keys (public and private) using two prime numbers `p` and `q`. It first verifies if the numbers are prime, calculates `n` and `phi`, and then finds a suitable `e` that is coprime with `phi`. It computes `d`, the modular inverse of `e`, and returns the key pair.

### `encrypt_data`

```python
def encrypt_data(self, data):
    """
    Encrypt data using a public key.

    Args:
        data (bytes): The data to encrypt.

    Returns:
        list: The encrypted data.
    """
    e, n = self.public_key
    encrypted_data = [pow(byte, e, n) for byte in data]
    return encrypted_data
```

This method encrypts a byte array `data` using the public key. It applies the RSA encryption formula `c = m^e mod n` to each byte and returns the list of encrypted values.

### `decrypt_data`

```python
def decrypt_data(self, data):
    """
    Decrypt data using a private key.

    Args:
        data (list): The data to decrypt.

    Returns:
        list: The decrypted data.
    """
    d, n = self.private_key
    decrypted_data = [pow(byte, d, n) for byte in data]
    return decrypted_data
```

This method decrypts a list of encrypted values `data` using the private key. It applies the RSA decryption formula `m = c^d mod n` to each value and returns the list of decrypted bytes.

### `read_file`

```python
def read_file(self, file_path):
    """
    Read a file as bytes.

    Args:
        file_path (str): The path to the file.

    Returns:
        bytes: The file data.
    """
    with open(file_path, 'rb') as file:
        return file.read()
```

This method reads the contents of a file specified by `file_path` and returns the data as bytes.

### `write_file`

```python
def write_file(self, file_path, data):
    """
    Write data to a file.

    Args:
        file_path (str): The path to the file.
        data (bytes): The data to write.

    Returns:
        None
    """
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)
    with open(file_path, 'wb') as file:
        file.write(data)
```

This method writes byte data to a file specified by `file_path`. If the directory does not exist, it creates the directory.

### `encrypt_file`

```python
def encrypt_file(self, file_path):
    """
    Encrypt a file using the public key.

    Args:
        file_path (str): The path to the file.

    Returns:
        None
    """
    file_data = self.read_file(file_path)
    encrypted_data = self.encrypt_data(file_data)
    encrypted_hex = ''.join([format(byte, '04x') for byte in encrypted_data])
    self.write_file(self.encrypted_path, encrypted_hex.encode())
```

This method reads the contents of a file, encrypts the data using the public key, converts the encrypted data to a hexadecimal string, and writes the result to the specified encrypted file path.

### `decrypt_file`

```python
def decrypt_file(self):
    """
    Decrypt a file using the private key.

    Returns:
        None
    """
    encrypted_hex = self.read_file(self.encrypted_path).decode()
    encrypted_data = [int(encrypted_hex[i:i+4], 16) for i in range(0, len(encrypted_hex), 4)]
    decrypted_data = self.decrypt_data(encrypted_data)
    self.write_file(self.decrypted_path, bytes(decrypted_data))
```

This method reads the contents of the encrypted file, converts the hexadecimal string back to encrypted data, decrypts the data using the private key, and writes the result to the specified decrypted file path.
