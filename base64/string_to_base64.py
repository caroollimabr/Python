import base64

str_example = "Python e uma excelente linguagem de programacao"
str_to_bytes = str_example.encode("ascii")  # we have an encoded string
bytes_to_base64 = base64.b64encode(str_to_bytes)  # encoding bytes to base64
print(bytes_to_base64)
# returns decoded string of base64
base64_output = bytes_to_base64.decode('ascii')
print(base64_output)
