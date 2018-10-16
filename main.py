import os
import inputs as io

import colorcode as clc
foldernames=["Cirque de Cilaos","Cirque de Mafate","Cirque de Salazie","Est","Nord","Ouest","Sud","Volcan","Ailleurs","All"]
webregionnames=[]
for i in range(9):
   try:
       leftside=foldernames[i].split(' ')[0].lower()+"-"
       rightside=foldernames[i].split(' ')[2].lower()
       webregionnames.append(leftside+rightside)
   except IndexError,ierr:
       oneside=foldernames[i].split(' ')[0].lower()
       webregionnames.append(oneside)
       pass
import foldercreating as fdc
basicfilename=""
randonb=[]
print clc.bold+"\n\nWelcome ! \nWith this script, you will be able to download gpx,trk and kml traces for hitchiking on the Reunion Isle."+clc.endc
zonechoice=io.regioninput()
zoneptr=zonechoice-1
maptype=io.mapfileinput()
MAIL=io.loginmail()
PSW=io.loginpass()



if maptype==1:
    basicfilename="f.gpx"
elif maptype==2:
    basicfilename="f.trk"
elif maptype==3:
    basicfilename="f.kml"

fdc.mainfolder()
fdc.mkfolder(MAIL,PSW,webregionnames,foldernames,maptype,zoneptr,basicfilename)



if zonechoice == 10:
    fdc.mkallfolder(MAIL,PSW,webregionnames,foldernames,maptype,zoneptr,basicfilename)
