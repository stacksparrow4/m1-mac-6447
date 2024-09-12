from pwn import *

context.arch = 'amd64'
context.terminal = ["/opt/pwntools-fake-term.sh"]

# p = process('./program')
# p = gdb.debug('./program')