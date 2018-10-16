import os
import inputs
import mapsparsing
import colorcode as clc
import foldercreating as fdc

foldernames=["Cirque de Cilaos","Cirque de Mafate","Cirque de Salazie","Est","Nord","Ouest","Sud","Volcan","Ailleurs","All"]
randonb=[]
basicfilename=""
print clc.bold+"\n\nWelcome ! \nWith this script, you will be able to download gpx,trk and kml traces for hitchiking on the Reunion Isle."+clc.endc

loginmail()
logipass()

filetype=mapfileinput()
zonechoice=regioninput()

if filetype==1:
    basicfilename="f.gpx"
elif filetype==2:
    basicfilename="f.trk"
else filetype==3:
    basicfilename="f.kml"

mapparsing(filetype,basicfilename)
mkfolder(filetype,zonechoice)

payload = {
    'mail': MAIL,
    'password': PSW
}

randoweb()










