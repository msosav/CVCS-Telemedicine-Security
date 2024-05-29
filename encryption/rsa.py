import random
import os
from PIL import Image

def is_prime(n):
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

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(e, phi):
    def egcd(a, b):
        if a == 0:
            return b, 0, 1
        g, x1, y1 = egcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return g, x, y

    g, x, y = egcd(e, phi)
    if g != 1:
        raise Exception('El inverso modular no existe.')
    else:
        return x % phi

def generate_keypair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError("Ambos números deben ser primos.")
    
    n = p * q
    phi = (p - 1) * (q - 1)
    
    e = random.randrange(1, phi)
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    d = mod_inverse(e, phi)
    return ((e, n), (d, n))

def encrypt_data(public_key, data):
    e, n = public_key
    encrypted_data = [pow(byte, e, n) for byte in data]
    return encrypted_data

def decrypt_data(private_key, data):
    d, n = private_key
    decrypted_data = [pow(byte, d, n) for byte in data]
    return decrypted_data

def read_file(file_path):
    with open(file_path, 'rb') as file:
        return file.read()

def write_file(file_path, data):
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)
    with open(file_path, 'wb') as file:
        file.write(data)

def encrypt_file(input_path, output_path, public_key):
    image = Image.open(input_path)
    image_data = image.tobytes()
    
    encrypted_data = encrypt_data(public_key, image_data)
    encrypted_hex = ''.join([format(byte, '04x') for byte in encrypted_data])
    
    write_file(output_path, encrypted_hex.encode())

def decrypt_file(input_path, output_path, private_key, mode, size):
    encrypted_hex = read_file(input_path).decode()
    encrypted_data = [int(encrypted_hex[i:i+4], 16) for i in range(0, len(encrypted_hex), 4)]
    
    decrypted_data = decrypt_data(private_key, encrypted_data)
    image_from_bytes = Image.frombytes(mode, size, bytes(decrypted_data))
    image_from_bytes.save(output_path)

# Ejemplo de uso
p = 61  # Un número primo pequeño
q = 53  # Otro número primo pequeño

public_key, private_key = generate_keypair(p, q)
print("Clave pública:", public_key)
print("Clave privada:", private_key)

# Leer imagen BMP
input_image_path = '/home/valeria/CVCS-Telemedicine-Security/images/output.bmp'
encrypted_file_path = '/home/valeria/CVCS-Telemedicine-Security/data/encrypted.bin'
decrypted_image_path = '/home/valeria/CVCS-Telemedicine-Security/images/decrypted.bmp'

image = Image.open(input_image_path)

mode = image.mode
size = image.size

encrypt_file(input_image_path, encrypted_file_path, public_key)
decrypt_file(encrypted_file_path, decrypted_image_path, private_key, mode, size)

print("Encriptación y desencriptación completadas.")
