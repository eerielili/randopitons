import subprocess
import os
import time

#global foldernames

#(foldernames[0].split(' ')[0]+"-"+foldernames[0].split(' ')[2]).lower()  => cirque-cilaos . ce formating sera pratique pour le site web

foldernames=["Cirque de Cilaos","Cirque de Mafate","Cirque de Salazie","Est","Nord","Ouest","Sud","Volcan","Ailleurs","All"]
totalfolders=foldernames
thehome=os.path.expanduser("~")
thefolder="/Randopitons"
default_folder=thehome+thefolder
choice = 0
maptype = 0

class colrs:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
#def print colrs.FAIL+("Operating System error: {0}".format(e))+colrs.ENDC:
    #print colrs.FAIL+("Operating System error: {0}".format(e))+colrs.ENDC


##def dlmap(maptype,choice):
#  folderptr=choice-1
#  fullpath=thehome+"/"+foldernames[folderptr]
#  try:
#      if foldernames[folderptr] == "All":
#          for foldernames in totalfolders:
#              os.mkdir(os.path.join(thehome,str(foldernames)))
#              #subprocess.call("rm -d "+fullpath)
#          print "All folders were created successfully"
#      else:
#          os.mkdir(fullpath)
#          print "Folder "+fullpath+"was created successfully"
#          
#          
#      for foldernames in tolimit:
#	os.mkdir(os.path.join(thehome,str(foldernames)))    
#          
#  except OSError, e:
#      print colrs.WARNING+("Operating System error: {0}".format(e))+colrs.ENDC


print "\n\nWelcome ! \nWith this script, you will be able to download gpx,trk and kml traces for hitchiking on the Reunion Isle."

#=================CREATING MAIN FOLDER AND OTHERS OR  ALL===================
try:
    chosing_folder=input("\n\nWhich folder would you want to download the files to [Default to home directory "+default_folder+"]")
    print "Folder "+chosing_folder+" was created successfully"
	#dlmap(maptype,choice)
except OSError, e:
    #errors out if folder exists else print the error (can be permissions or anything else)
    if e.errno == os.errno.EEXIST:
        print colrs.WARNING+("The folder already exists !")+colrs.ENDC
    else:
        print colrs.FAIL+("Operating System error: {0}".format(e))+colrs.ENDC
    pass
except SyntaxError:
    print "\nCreating default folder "+default_folder+" ..."
    os.mkdir(default_folder)





print """\n Which zone you would want to download ?
1. Cirque de Cilaos (Cilaos' Circus)
2. Cirque de Mafate (Mafate's Circus)
3. Cirque de Salazie (Salazie's Circus)
4. Est (East)
5. Nord (North)
6. Ouest (West)
7. Sud (South)
8. Volcan (Volcano)
9. Ailleurs (Elsewhere)
10. All \n"""



 ##================CHOSING CHOICE (heh)==============   
while choice < 1 or choice > 10:
    try:
        choice =  input("You must enter a number between 1 and 10.  Your choice [Default is \"All\"]: ")
        int(choice)
    except (KeyboardInterrupt, SystemExit):
        print colrs.WARNING+"\n\nProcess interrupted by CTRL+C or system."+colrs.ENDC
        exit()
    except SyntaxError:
        choice = 10;
    except NameError:
        print "\nPlease enter a number between 1 and 10."
        choice = 0
        
 #================DECLARING  FOLDERNAMES==============       


 #================CHOSING MAPTYPE==============
print """\n Which map type you would want to download ?
1. gpx (GPS Exchange Format)
2. trk (CompeGPS Land Track File)
3. kml (Keyhole Markup Language)\n"""

while maptype<1 or maptype>3:
    try:
        maptype = input("You must enter a number between 1 and 3. Your choice ? ")
        int(maptype)
    except (KeyboardInterrupt, SystemExit):
        print colrs.WARNING+"\n\nProcess interrupted by CTRL+C or system."+colrs.ENDC
        exit()
        

    #    raise   
    #    time.sleep(3)
    
    #pass	
    	





print "Program ended."
