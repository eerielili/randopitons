from requests import session
import inputs
from bs4 import BeautifulSoup as bs
import colorcode as clc
import errmsg as e


def randoweb():
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
                dwnld = c.get('https://randopitons.re/randonnee/'+i+'/trace/'+maptype)
                gudencoding=dwnld.text.encode('utf-8')
                
                gpxf=open('f.gpx','a+')
                gpxf.write(gudencoding)
                gpxf.close()
                
            print("Finished writing files.")
        except OSError, e:
            print e.os
            print format(e)
        
        

#print(response.headers)
#print(response.text)

