import hashlib, uuid
salt = uuid.uuid4().hex
hashed_password = hashlib.sha512(bytes("123456", 'utf-8')).hexdigest()
print(hashed_password)
print(len(hashed_password))