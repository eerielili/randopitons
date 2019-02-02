# -*- coding: utf-8 -*-
from requests import session
import inputs
from bs4 import BeautifulSoup as bs
import colorcode as clc
import errmsg as e
import os
import mapsparsing as mpp
randonb=[]
a_str="eh"
baseurl='https://randopitons.re/randonnee/'
    
def filei(dwnld,fpath):
    try:
        f=open(fpath,'a+')
        gudencoding=dwnld.text.encode('utf-8')
        f.write(gudencoding)
        f.close()
    except:
        raise



def testalakon():
    payload = {
        'mail': 'lionel.miquel46@gmail.com',
        'password': 'VEobWylvUdToab8'
    }
    with session() as c:
        try:
            c.post('https://randopitons.re/connexion', data=payload)
            regionpage = c.get('https://randopitons.re/randonnees/region/cirque-cilaos')
            try:
                wsite=bs(regionpage.text, "lxml")
                print "Voici les donnees:"+regionpage.text
            except:
                raise
            try:
                for i in wsite.find_all('tr'):
                    randonb.append(i.get("rid"))
                try:
                    randonb.pop(0)
                    print "POPPED"
                except:
                    raise
                print "Voici les numéros de randos:"
                print randonb
                try:
                    for i in randonb:
                        print clc.okgreen+"Maybe downloading "+baseurl+i+'/trace/gpx'
                        try:
                            dwnld = c.get(baseurl+i+'/trace/gpx')
                        except:
                            raise
                        filei(dwnld,'/home/lili/Randopitons/Cirque de Cilaos/f-'+i+'.gpx')
                except:
                    raise
            except:
                raise
        except:
            raise
    
def randoweb(MAIL,PSW,region,maptype,bfn,folderpath):
    payload = {
        'mail': MAIL,
        'password': PSW
    }
    
    with session() as c:
        
        try:
            c.post('https://randopitons.re/connexion', data=payload)
            regionpage = c.get('https://randopitons.re/randonnees/region/'+region)
            try:
                wsite=bs(regionpage.text, "lxml")
                print "Voici les donnees:"+regionpage.text
            except:
                raise
            try:
                for i in wsite.find_all('tr'):
                    randonb.append(i.get("rid"))
                try:
                    randonb.pop(0)
                    print "POPPED"
                except:
                    raise
                print "Voici les numéros de randos:"
                print randonb
            except:
                raise
            
            
            
            try:
                for i in randonb:
                    if maptype==1:
                        try:
                            print clc.okgreen+"Maybe downloading "+baseurl+i+'/trace/gpx'
                            dwnld = c.get(baseurl+i+'/trace/gpx')
                        except TypeError:
                            pass
                        except:
                            raise
                        filei(dwnld,folderpath+bfn)
                    elif maptype==2:
                        try:
                            print clc.okgreen+"Maybe downloading "+baseurl+i+'/trace/trk'
                            dwnld = c.get(baseurl+i+'/trace/trk')
                        except TypeError:
                            pass
                        except:
                            raise
                        filei(dwnld,folderpath+bfn)
                    else:
                        try:
                            print clc.okgreen+"Maybe downloading "+baseurl+i+'/trace/kml'
                            dwnld = c.get(baseurl+i+'/trace/kml')
                        except TypeError:
                            pass
                        except:
                            raise
                        filei(dwnld,folderpath+bfn)
            except:
                raise   
            try:
                mpp.mapparsing(maptype,folderpath+bfn)
            except:
                raise
            print("Finished writing file.")
        except :
            raise


