import subprocess
import os
import time

#global foldernames

#(foldernames[0].split(' ')[0]+"-"+foldernames[0].split(' ')[2]).lower()  => cirque-cilaos . ce formating sera pratique pour le site web
thehome=os.path.expanduser("~")
thefolder="/Randopitons"
default_folder=thehome+thefolder   

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






 #================DECLARING  FOLDERNAMES==============       




print "Program ended."
