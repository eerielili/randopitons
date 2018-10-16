from requests import session
import inputs
from bs4 import BeautifulSoup as bs
import colorcode as clc
import errmsg as e
import mapsparsing as mpp



    
    
def randoweb(MAIL,PSW,region,maptype,bfn):
    payload = {
        'mail': MAIL,
        'password': PSW
    }
    
    with session() as c:
        
        try:
            post('https://randopitons.re/connexion', data=payload)
            region = c.get('https://randopitons.re/randonnees/region/'+region)
            wsite=bs(region)
            for i in wsite.find_all('tr'):
                randonb.append(i.get("rid"))
        except SSLError, sslerr:
            print e.sslerr
                
        try:
            for i in randonb:
                dwnld="all the interwebz"
                if maptype==1:
                    dwnld = c.get('https://randopitons.re/randonnee/'+i+'/trace/gpx')
                    gpxf=open(bfn,'a+')
                elif maptype==2:
                    dwnld = c.get('https://randopitons.re/randonnee/'+i+'/trace/kml')
                    gpxf=open(bfn,'a+')
                else:
                    dwnld = c.get('https://randopitons.re/randonnee/'+i+'/trace/trk')
                    gpxf=open(bfn,'a+')
                    
                gudencoding=dwnld.text.encode('utf-8')
                gpxf.write(gudencoding)
                gpxf.close()
            
            mpp.mapparsing(maptype,bfn)    
            print("Finished writing files.")
        except OSError, er:
            print e.os
            print format(er)
        
        

#print(response.headers)
#print(response.text)

