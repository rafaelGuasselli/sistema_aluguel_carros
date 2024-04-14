from datetime import datetime, timedelta

data = datetime.strptime("1984-December-30", "%Y-%B-%d")
print(data.strftime("%Y-%B-%d"))

palavra = "aabb"
print("{palavra}")

import hashlib, uuid
salt = uuid.uuid4().hex
hashed_password = hashlib.sha512(bytes("123456", 'utf-8')).hexdigest()
print(hashed_password)
print(len(hashed_password))