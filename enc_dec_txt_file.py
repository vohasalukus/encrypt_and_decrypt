def encrypt(text, shift):
    encrypted_text = ''
    for char in text:
        if char.isalpha():
            shifted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a')) \
                if char.islower() else chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            encrypted_text += shifted_char
        else:
            encrypted_text += char
    return encrypted_text


def decrypt(encrypted_text, shift):
    return encrypt(encrypted_text, -shift)


def encrypt_file(input_filename, output_filename, shift):
    with open(input_filename, 'r', encoding='utf-8') as input_file:
        text = input_file.read()
    encrypted_text = encrypt(text, shift)
    with open(output_filename, 'w', encoding='utf-8') as output_file:
        output_file.write(encrypted_text)


def decrypt_file(input_filename, output_filename, shift):
    with open(input_filename, 'r', encoding='utf-8') as input_file:
        encrypted_text = input_file.read()
    decrypted_text = decrypt(encrypted_text, shift)
    with open(output_filename, 'w', encoding='utf-8') as output_file:
        output_file.write(decrypted_text)


input_filename = ''  # Замените на имя вашего файла
output_filename = 'encrypted_text.txt'
shift = 3  # Сдвиг для шифра Цезаря

# Шифрование
encrypt_file(input_filename, output_filename, shift)
print("Текст успешно зашифрован и записан в файл:", output_filename)

# Дешифрование
decrypted_filename = 'decrypted_text.txt'
decrypt_file(output_filename, decrypted_filename, shift)
print("Текст успешно дешифрован и записан в файл:", decrypted_filename)