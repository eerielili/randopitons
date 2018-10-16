import subprocess
import os
import time
import colorcode as clc
import errmsg as e
#global foldernames

#(foldernames[0].split(' ')[0]+"-"+foldernames[0].split(' ')[2]).lower()  => cirque-cilaos . ce formating sera pratique lors de la récupération sur site web
thehome=os.path.expanduser("~")
thefolder="/Randopitons"
default_folder=thehome+thefolder   


def mkfolder(maptype,choice):
    folderptr=choice-1
    fullpath=thehome+"/"+foldernames[folderptr]
    try:
        if foldernames[folderptr] == "All":
            for foldernames in totalfolders:
                os.mkdir(os.path.join(thehome,str(foldernames)))
                #subprocess.call("rm -d "+fullpath)
            print "All folders were created successfully"
        else:
            os.mkdir(fullpath)
            print "Folder "+fullpath+"was created successfully"
            
            
        for foldernames in tolimit:
            os.mkdir(os.path.join(thehome,str(foldernames)))    
            
    except OSError, e:
      print e.os
      print format(e)

def mainfolder():
    try:
        chosing_folder=input("\n\nWhich folder would you want to download the files to [Default to home directory "+default_folder+"]")
        print "Folder "+chosing_folder+" was created successfully"
    except OSError, e:
        #errors out if folder exists else print the error (can be permissions or anything else)
        if e.errno == os.errno.EEXIST:
            print e.direxist
        else:
            print e.os
            print format(e)
        pass
    except SyntaxError:
        print "\nCreating default folder "+default_folder+" ..."
    os.mkdir(default_folder)

#print "Program ended."
