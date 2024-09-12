Please refer to the youtube video for setup information.

How to debug using GDB without pwntools:
```
qemu-amd64 -g 1234 ./myfile
gdb-multiarch ./myfile -ex 'target remote localhost:1234'
```
