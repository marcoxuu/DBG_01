import os

import capstone as capstone
from capstone import *

f=open('D:/test.exe','rb')
lines=f.readlines()
for line in lines:
    line=line.strip()
    # print(line)
    CODE =line
    md = Cs(CS_ARCH_X86, CS_MODE_64)
    for i in md.disasm(CODE, 0x1000):
        print("0x%x:\t%s\t%s" % (i.address, i.mnemonic, i.op_str))
