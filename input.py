from pwn import *
ssh = ssh('input2', 'pwnable.kr', 2222, 'guest')

def stage_1():
    argv = [b'_' for _ in range(100)]
    argv[0] = b'./input'
    argv[ord('A')] = b'\x00'
    argv[ord('B')] = b'\x20\x0a\x0d'

    assert len(argv) == 100
    assert argv[ord('A')] == b'\x00'
    assert argv[ord('B')] == b'\x20\x0a\x0d'

    return argv

def stage_2():
    pass

argv = stage_1()
io = ssh.process(argv)
io.interactive()
