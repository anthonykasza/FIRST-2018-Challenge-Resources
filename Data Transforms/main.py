import sys
sys.path.insert(0, './')
from aux import *

def main(key, iv):
  fh = open('input', 'rb')
  data = fh.read()
  fh.close()
  with open('output', 'wb') as f:
    for ch in chunk(data, 16):
      t = add(ch, 5)
      z = xor(t, 44)
      e = enc(z, key, iv)
      f.write(e)

if __name__ == '__main__':
  key = 'KEY1234567890123'
  iv = 'IV34567890123456'
  main(key, iv)
