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
a_folder=0




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
    except:
        raise

def mkfolder(MAIL,PSW,regionnames,foldernames,maptype,ptr,bfn):
    
    try:
        if a_folder==0:
            os.mkdir(os.path.join(def_folder,foldernames[ptr]))
        else:
            os.mkdir(os.path.join(a_folder,foldernames[ptr]))
        #rdo.testalakon()
        rdo.randoweb(MAIL,PSW,regionnames[ptr],maptype,bfn,def_folder+a_str)
    except OSError, er:
        print e.os
        print format(er)
        
        
def mkallfolder(MAIL,PSW,regionnames,foldernames,maptype,bfn):
    iii=0
    a_str="str"
    try:
        for a_str in foldernames:
            if a_folder==0:
                os.mkdir(os.path.join(def_folder,a_str))
            else:
                os.mkdir(os.path.join(a_folder,a_str))
                
                
            try:
                print "on attaque par le "+regionnames[iii]
                rdo.randoweb(MAIL,PSW,regionnames[iii],maptype,bfn,def_folder+a_str)
            except:
                raise
            iii=iii+1
            #subprocess.call("rm -d "+fullpath)
        print "All folders were created successfully"
    except OSError, er:
        print e.os
        print format(er)

