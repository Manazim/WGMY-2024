with open(r"D:\Users\Asus Zephyrus G15\Documents\updated_file.jpeg", 'rb') as f:
    data = f.read()

# Remove the sequence `6d 65 6f 77`
updated_data = data.replace(b'\x6d\x65\x6f\x77', b'')

with open(r"finally_yes.jpeg", 'wb') as f:
    f.write(updated_data)
