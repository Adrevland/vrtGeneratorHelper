import os
import sys
from argparse import FileType

print(sys.argv)

rootdir = sys.argv[1]
outputFile = sys.argv[2]
filetype = sys.argv[3]

print("RootDir : " + rootdir)
print("OutFile : " + outputFile)
print("FileType : " + filetype)

filesToInclude = []

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        if file.endswith(filetype):
            filesToInclude.append(os.path.join(subdir,file))

writefile = open(outputFile,"w")
for file in filesToInclude:
    writefile.write(file+"\n")

writefile.close()

print("\n---DONE---\nAll " + filetype + " file locations are written to file : " + outputFile)