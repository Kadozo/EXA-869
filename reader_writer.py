import os

inputdir = "./Files/inputs"
outputdir = "./Files/outputs"

os.makedirs(outputdir)

filesname = list(os.listdir(inputdir))

for filename in filesname:
    with open(inputdir+'/'+filename, "r") as currentFile:
        content = currentFile.read()
    characters = list(content)
    currentOutputFile = open(outputdir+'/'+filename.split(sep='.')[0]+'-output.txt', "a")
    for character in characters:
        currentOutputFile.write(character+'\n')
    currentOutputFile.close()