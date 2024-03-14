import random

def publicKey(q, pK, p):
    publicKey = (q ** pK) % p
    return publicKey

def sessionKey(pks, ypk, p):
    sKey = (pks ** ypk) % p
    return sKey

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
            elif char.isupper():  # Переместил этот блок на уровень с блоком if, чтобы он выполнялся только для заглавных букв
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            encrypted_message += chr(shifted)
        else:
            encrypted_message += char  # Этот блок должен быть выше (на уровне с блоком if), чтобы выполняться для всех символов
    return encrypted_message

def caesar_cipher_decrypt(encrypted_message, key):
    return caesar_cipher_encrypt(encrypted_message, -key)

p = 13
q = 41

privatekBob = random.randint(1, p - 1)
privatekAlice = random.randint(1, p - 1)

print("Private Key Alice", privatekAlice)
print("Private Key Bob", privatekBob)

pkA = publicKey(q, privatekAlice, p)
pkB = publicKey(q, privatekBob, p)

print(pkA, pkB)

skA = sessionKey(pkB, privatekAlice, p)  # Исправил аргументы функции sessionKey
skB = sessionKey(pkA, privatekBob, p)  # Исправил аргументы функции sessionKey

print("Session key", skA, skB)

message = "Hello Alice!"

# Шифрование сообщения на стороне Боба
encrypted_message = caesar_cipher_encrypt(message, skB)

# Расшифрование сообщения на стороне Алисы
decrypted_message = caesar_cipher_decrypt(encrypted_message, skA)

print("Исходное сообщение:", message)
print("Зашифрованное сообщение:", encrypted_message)
print("Расшифрованное сообщение:", decrypted_message)
