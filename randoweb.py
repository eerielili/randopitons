from requests import session
import inputs
from bs4 import BeautifulSoup as bs




    with session() as c:
        try:
            post('https://randopitons.re/connexion', data=payload)
            region = c.get('https://randopitons.re/randonnees/region/'+region)
            wsite=bs(region)
        except SSLError, sslerr:
            print "SSL Certificate Error. Please check the time on your computer, adjust it accordingly, or wait a bit before retrying the downloads."
            
        

        
        for i in wsite.find_all('tr'):
            randonb.append(i.get("rid"))

        try:
            for i in randonb:
                dwnld = c.get('https://randopitons.re/randonnee/'+i+'/trace/'+maptype)
                gudencoding=dwnld.text.encode('utf-8')
                
                gpxf=open('f.gpx','a+')
                gpxf.write(gudencoding)
                gpxf.close()
                
            print("FINISHED WRITING FILES")
        except OSError, e:
                print("Operating System error: {0}".format(e))
        
        

    print(response.headers)
print(response.text)

