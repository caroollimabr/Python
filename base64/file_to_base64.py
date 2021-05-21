import base64

# open file in binary read mode
with open("palavrasForca.txt", "rb") as image:
    encoded_image = base64.b64encode(image.read())

print(encoded_image)

