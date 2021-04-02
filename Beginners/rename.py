#!/usr/bin/pyhon
import os, glob
os.chdir("/tmp")
for f in glob.glob("*.txt"):
   print(f)
   base = os.path.splitext(f)[0]
   newfile = os.rename(f, base + '.bin')
print(newfile)

