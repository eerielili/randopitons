import subprocess
import os
import time
import colorcode as clc
import errmsg as e
import randoweb as rdo
#global foldernames

thehome=os.path.expanduser("~")
defoldername="/Randopitons"
def_folder=thehome+defoldername





def defolder():
    try:
        print "\nCreating default folder "+def_folder+" ..."
        os.mkdir(def_folder)
    except OSError,er:
        print e.os
        print format(er)
        
def mainfolder():
    try:
        a_folder=input("\n\nWhich folder would you want to download the files to [Default to home directory "+def_folder+"]")
        os.mkdir(a_folder)
        print "Folder "+a_folder+" was created successfully"
    except OSError, er:
        #errors out if folder exists else print the error (can be permissions or anything else)
        if e.errno != os.errno.EEXIST:
            raise
        else:
            print e.os
            print format(er)
            pass
        
    except SyntaxError:
        
        os.mkdir(def_folder)
    except KeyboardInterrupt:
        print e.sigkill

def mkfolder(MAIL,PSW,regionnames,foldernames,maptype,ptr,choice,bfn):
    
    try:
        os.mkdir(os.path.join(thehome,foldernames[ptr]))
        rdo.randoweb(MAIL,PSW,regionnames[ptr],filetype,bfn)
    except OSError, er:
        print e.os
        print format(er)
        
        
def mkallfolder(MAIL,PSW,regionnames,foldernames,maptype,bfn):
    i=0
    try:
        for foldernames in foldernames:
            os.mkdir(os.path.join(thehome,str(foldernames)))
            rdo.randoweb(MAIL,PSW,regionnames[i],maptype,bfn)
            i=i+1
            #subprocess.call("rm -d "+fullpath)
        print "All folders were created successfully"
    except OSError, er:
        print e.os
        print format(er)

