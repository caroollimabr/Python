import base64
# encoded string from first example
b64_str = "UHl0aG9uIGUgdW1hIGV4Y2VsZW50ZSBsaW5ndWFnZW0gZGUgcHJvZ3JhbWFjYW8="
b64_str = b64_str.encode('ascii')
b64_bytes = base64.b64decode(b64_str)
decode_str = b64_bytes.decode('ascii')
print(decode_str)