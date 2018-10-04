import os
import inputs
foldernames=["Cirque de Cilaos","Cirque de Mafate","Cirque de Salazie","Est","Nord","Ouest","Sud","Volcan","Ailleurs","All"]
totalfolders=foldernames
randonb=[]
basicfilename=""
print "\n\nWelcome ! \nWith this script, you will be able to download gpx,trk and kml traces for hitchiking on the Reunion Isle."

loginmail()
logipass()

filetype=mapfileinput()

if filetype==1:
    basicfilename="f.gpx"
else if filetype==2:
    basicfilename="f.trk"
else:
    basicfilename="f.kml"
    
payload = {
    'mail': MAIL,
    'password': PSW
}










