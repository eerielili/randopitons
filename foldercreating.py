import subprocess
import os
import time
import colorcode as clc
import errmsg as e
#global foldernames

#(foldernames[0].split(' ')[0]+"-"+foldernames[0].split(' ')[2]).lower()  => cirque-cilaos . ce formating sera pratique lors de la récupération sur site web
thehome=os.path.expanduser("~")
defoldername="/Randopitons"
def_folder=thehome+defoldername
fullpath=thehome+"/"+foldernames[regionptr]

def mainfolder():
    try:
        a_folder=input("\n\nWhich folder would you want to download the files to [Default to home directory "+def_folder+"]")
        print "Folder "+a_folder+" was created successfully"
    except OSError, e:
        #errors out if folder exists else print the error (can be permissions or anything else)
        if e.errno == os.errno.EEXIST:
            print e.direxist
        else:
            print e.os
            print format(e)
        pass
    except SyntaxError:
        print "\nCreating default folder "+def_folder+" ..."
        os.mkdir(def_folder)

def mkfolder(choice):
    regionptr=choice-1
    try:
        os.mkdir(os.path.join(thehome,foldernames[regionptr]))    
    except OSError, e:
        print e.os
        print format(e)
        
        
def mkallfolder(choice):
    try:
        if choice == 10:
            for foldernames in range(9):
                os.mkdir(os.path.join(thehome,str(foldernames)))
                #subprocess.call("rm -d "+fullpath)
            print "All folders were created successfully"
    except OSError, e:
        print e.os
        print format(e)


#print "Program ended."
