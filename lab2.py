# Функция для шифрования сообщения с помощью алгоритма Цезаря
def caesar_cipher_encrypt(message, key):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            shifted = ord(char) + key
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            encrypted_message += chr(shifted)
        else:
            encrypted_message += char
    return encrypted_message

# Функция для дешифрования сообщения с помощью алгоритма Цезаря
def caesar_cipher_decrypt(encrypted_message, key):
    return caesar_cipher_encrypt(encrypted_message, -key)

# Общий секретный ключ
shared_secret_key = 3

# Сообщение для шифрования
message = "Hello, Alice!"

# Шифрование сообщения на стороне Боба
encrypted_message = caesar_cipher_encrypt(message, shared_secret_key)

# Расшифрование сообщения на стороне Алисы
decrypted_message = caesar_cipher_decrypt(encrypted_message, shared_secret_key)

print("Исходное сообщение:", message)
print("Зашифрованное сообщение:", encrypted_message)
print("Расшифрованное сообщение:", decrypted_message)
