from enum import Enum
from os import listdir
from os.path import isfile, join
import ipywidgets
import colorama

class FileNameConv(Enum):
    Foundation = 0,
    BrainBox = 1,
    Cabinet = 2,
    Sas = 3,
    G2S = 4,
    Ip = 5,
    Date = 6

class FindFilesByDate():
    print(FileNameConv.BrainBox)
    print(FileNameConv.BrainBox.value)
    print(FileNameConv.BrainBox.name)

    for fileNameConv in FileNameConv:
        a = fileNameConv
        print(fileNameConv)
        print(fileNameConv.value,fileNameConv.name)

   # onlyfiles = [f for f in listdir('d:\\SkynetData\\SkynetDataNew') if isfile(join('d:\\SkynetData\\SkynetDataNew', f))]
   # print(onlyfiles)

    for f in listdir('d:\\SkynetData\\SkynetDataOne'):
        print(f)
      #  if isfile(join('d:\\SkynetData\\SkynetDataNew')):

