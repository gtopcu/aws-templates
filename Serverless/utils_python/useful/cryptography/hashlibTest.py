import hashlib

password = "12asdkjfh32iukjnfjksbfjkdfj284y9812y41yuhrkfjdakhfksdjdbsjkfd456"

md5 = hashlib.md5(password.encode()).hexdigest()  # 32 characters
print(len(md5))

sha256 = hashlib.sha256(password.encode()).hexdigest()  # 64 characters
print(len(sha256))

sha512 = hashlib.sha512(password.encode()).hexdigest()  # 128 characters
print(len(sha512))

sha1 = hashlib.sha1(password.encode()).hexdigest()  # 40 characters
print(len(sha1))
