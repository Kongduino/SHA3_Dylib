#!/usr/bin/python3
from ctypes import *
import platform, os, sys, random
from hexdump import hexDump

pl = platform.system()
if pl == 'Darwin':
  sha3 = CDLL('../k_sha3.dylib')
elif pl == 'Linux':
  sha3 = CDLL('../k_sha3.so')

# typedef struct {
#   unsigned int P[16 + 2];
#   unsigned int S[4][256];
# } BLOWFISH_CTX;

buf = bytes(int(512/8))
bufB = cast(buf, POINTER(c_char))
# Size of sha3_context: 224
ctx = bytes(224)
ctxB = cast(ctx, POINTER(c_char))
source = b"abc"
sourceB = cast(source, POINTER(c_char))

sha3.sha3_HashBuffer(256, 1, sourceB, 3, bufB, 200)
hexDump(buf, 32)
print(buf[0:32])
if buf[0:32] != b'N\x03ez\xeaE\xa9O\xc7\xd4{\xa8&\xc8\xd6g\xc0\xd1\xe6\xe3:d\xa06\xecD\xf5\x8f\xa1-lE':
  print("SHA3/256 failed!\n")
else:
  print("SHA3/256 success!\n")

sha3.sha3_HashBuffer(384, 1, sourceB, 3, bufB, 200)
hexDump(buf, 48)
print(buf[0:48])
if buf[0:48] != b'\xf7\xdf\x11e\xf033{\xe0\x98\xe7\xd2\x88\xadj/t@\x9dz`\xb4\x9c6d"\x18\xde\x16\x1b\x1f\x99\xf8\xc6\x81\xe4\xaf\xaf1\xa3M\xb2\x9f\xb7c\xe3\xc2\x8e':
  print("SHA3/384 failed!\n")
else:
  print("SHA3/384 success!\n")

sha3.sha3_HashBuffer(512, 1, sourceB, 3, bufB, 200)
hexDump(buf, 64)
print(buf[0:64])
if buf[0:64] != b'\x18X}\xc2\xea\x10k\x9a\x15c\xe3+3\x12B\x1c\xa1d\xc7\xf1\xf0{\xc9"\xa9\xc8=w\xce\xa3\xa1\xe5\xd0\xc6\x99\x10s\x90%7-\xc1J\xc9d&)7\x95@\xc1~*e\xb1\x9dw\xaaQ\x1a\x9d\x00\xbb\x96':
  print("SHA3/512 failed!\n")
else:
  print("SHA3/512 success!\n")
