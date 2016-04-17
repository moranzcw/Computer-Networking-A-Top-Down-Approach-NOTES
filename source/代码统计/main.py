#! /usr/bin/env python

import os,datetime
from shutil import copy

###
Dir = '/home/moran/'
Year = 2015
Month = 3

filelist = []
cmd = 'cloc '

###
def searchFile(baseDir):
    dirList = os.listdir(baseDir)
    for i in range(0, len(dirList)):
        if not dirList[i].startswith('.'):
            path = os.path.join(baseDir,dirList[i])
            if os.path.isfile(path):
                filelist.append(path)
            elif os.path.isdir(path):
                searchFile(path)


###
tempDir = os.path.join(Dir,'tempPy')
if not os.path.isdir(tempDir):
    os.makedirs(tempDir)

searchFile(Dir)
for i in range(0, len(filelist)):
    path = filelist[i]
    if os.path.isdir(filelist[i]):
        continue
    timestamp = os.path.getmtime(path)
    
    date = datetime.datetime.fromtimestamp(timestamp)
    # print filelist[i],':',date.strftime('%Y-%m-%d %H:%M:%S')
    if(date.year == Year and date.month == Month):
        copy(filelist[i], tempDir)
cmd = 'cloc ' + tempDir
os.system(cmd)

for file in os.listdir(tempDir): 
    targetFile = os.path.join(tempDir,  file) 
    if os.path.isfile(targetFile): 
        os.remove(targetFile)
os.remove(tempDir)