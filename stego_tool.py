from PIL import Image

END_MARKER = "1111111111111110"

# ===============================
# TOOL STEGANOGRAFI BY Harry
# ===============================

print("=" * 40)
print("   TOOL STEGANOGRAFI BY Harry")
print("=" * 40)

def text_to_binary(text):
    return ''.join(format(ord(i), '08b') for i in text)

def binary_to_text(binary):
    chars = [binary[i:i+8] for i in range(0, len(binary), 8)]
    return ''.join(chr(int(char, 2)) for char in chars)

def encode_image(input_image, secret_text, output_image):
    img = Image.open(input_image)
    img = img.convert("RGB")
    width, height = img.size
    
    binary_text = text_to_binary(secret_text) + END_MARKER
    index = 0
    
    encoded = img.copy()
    
    for y in range(height):
        for x in range(width):
            if index < len(binary_text):
                r, g, b = img.getpixel((x, y))
                r = (r & ~1) | int(binary_text[index])
                index += 1
                encoded.putpixel((x, y), (r, g, b))
            else:
                break
    
    encoded.save(output_image)
    print("\n✅ Pesan berhasil disisipkan!")
    print("Output:", output_image)

def decode_image(image_path):
    img = Image.open(image_path)
    img = img.convert("RGB")
    width, height = img.size
    
    binary_data = ""
    
    for y in range(height):
        for x in range(width):
            r, g, b = img.getpixel((x, y))
            binary_data += str(r & 1)
            
            if END_MARKER in binary_data:
                binary_data = binary_data.replace(END_MARKER, "")
                text = binary_to_text(binary_data)
                print("\n🔓 Pesan ditemukan:")
                print(text)
                return
    
    print("\n❌ Tidak ada pesan ditemukan")

# ===============================
# MENU
# ===============================

print("\n1. Encode")
print("2. Decode")

choice = input("\nPilih (1/2): ")

if choice == "1":
    input_img = input("Masukkan path gambar PNG: ")
    output_img = input("Nama output gambar (PNG): ")
    secret = input("Masukkan pesan rahasia: ")
    encode_image(input_img, secret, output_img)

elif choice == "2":
    img = input("Masukkan path gambar untuk decode: ")
    decode_image(img)

else:
    print("Pilihan tidak valid")
