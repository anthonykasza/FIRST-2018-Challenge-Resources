
import sys
from Crypto.Cipher import AES
import base64
import inspect
import md5
import time

def decrypt(i, self):
  from secret import encrypted_flag
  time.sleep(30)
  if type(i) != int:
    return False
  if (i > 2 ** 32) or (i < 7):
    return False
  s = inspect.getsource(self)
  m = md5.new()
  m.update(s)
  d = m.hexdigest()
  f = 0
  for c in d:
    f += (ord(c) + i)
  secret_key = str(f).rjust(16)

  cipher = AES.new(secret_key, AES.MODE_ECB)
  decrypted_flag = cipher.decrypt(base64.b64decode(encrypted_flag)).strip()
  return decrypted_flag


print "USAGE: decrypt.py [SEED]\nwhere [SEED] is an integer"
seed = int(sys.argv[1])
dec = decrypt(seed, decrypt)
print dec
