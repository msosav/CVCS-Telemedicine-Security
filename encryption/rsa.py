import random
import base64

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

def encrypt_block(public_key, block):
    e, n = public_key
    return [pow(byte, e, n) for byte in block]

def decrypt_block(private_key, block):
    d, n = private_key
    return [pow(byte, d, n) for byte in block]

def read_file(file_path):
    with open(file_path, 'rb') as file:
        return file.read()

def write_file(file_path, data):
    with open(file_path, 'wb') as file:
        file.write(data)

def encode_base64(data):
    byte_data = b''.join(num.to_bytes((num.bit_length() + 7) // 8, 'big') for num in data)
    return base64.b64encode(byte_data)

def decode_base64(data, block_size):
    byte_data = base64.b64decode(data)
    num_length = (block_size.bit_length() + 7) // 8
    return [int.from_bytes(byte_data[i:i + num_length], 'big') for i in range(0, len(byte_data), num_length)]

# Funciones para manejar bloques de datos
def split_blocks(data, block_size):
    return [data[i:i + block_size] for i in range(0, len(data), block_size)]

def join_blocks(blocks):
    return b''.join(blocks)

def convert_to_bytes(block):
    return bytes([num % 256 for num in block])

# Ejemplo de uso
p = 61  # Un número primo pequeño
q = 53  # Otro número primo pequeño

public_key, private_key = generate_keypair(p, q)
print("Clave pública:", public_key)
print("Clave privada:", private_key)


# Leer archivo .bmp
input_file_path = '/home/valeria/CVCS-Telemedicine-Security/images/output.bmp'
output_encrypted_path = '/home/valeria/CVCS-Telemedicine-Security/images/encrypted.bmp'
output_decrypted_path = '/home/valeria/CVCS-Telemedicine-Security/images/decrypted.bmp'


data = read_file(input_file_path)
header, body = data[:54], data[54:]  # Separa el encabezado BMP y los datos del cuerpo

# Dividir el cuerpo del archivo .bmp en bloques
block_size = 256  # Tamaño del bloque (ajusta según sea necesario, debe ser menor que n)
blocks = split_blocks(body, block_size)

# Encriptar cada bloque del cuerpo del archivo .bmp
encrypted_blocks = [encrypt_block(public_key, block) for block in blocks]
encoded_encrypted_blocks = [encode_base64(block) for block in encrypted_blocks]

# Escribir archivo encriptado
write_file(output_encrypted_path, header + b''.join(encoded_encrypted_blocks))

# Leer y desencriptar el archivo encriptado
encrypted_data = read_file(output_encrypted_path)
encoded_encrypted_blocks = split_blocks(encrypted_data[54:], len(base64.b64encode(b'\x00' * block_size)))
encrypted_blocks = [decode_base64(block, block_size) for block in encoded_encrypted_blocks]
decrypted_blocks = [decrypt_block(private_key, block) for block in encrypted_blocks]

# Convertir los bloques descifrados a bytes
decrypted_bytes = [convert_to_bytes(block) for block in decrypted_blocks]

# Escribir archivo desencriptado
write_file(output_decrypted_path, header + join_blocks(decrypted_bytes))

print("Encriptación y desencriptación completadas.")
