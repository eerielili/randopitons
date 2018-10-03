from requests import session
import getpass
import xml.etree.ElementTree as xmlp
import os
from bs4 import BeautifulSoup as bs


def main(region,maptype):
    MAIL=raw_input("YUORE E-MAIL TO LOG IN TO RANDOPITONS.RE : ")
    PSW=getpass.getpass(prompt="YUORE PASSWORD TO LOG IN TO RANDOPITONS.RE : ")


    payload = {
        'mail': MAIL,
        'password': PSW
    }

    with session() as c:
        try:
            post('https://randopitons.re/connexion', data=payload)
        except SSLError, sslerr:
            print "Erreur de certificat SSL"
            
        region = c.get('https://randopitons.re/randonnees/region/'+region)
        wsite=bs(region)

        randonb=[]
        for i in wsite.find_all('tr'):
            randonb.append(i.get("rid"))

        try:
            for i in randonb:
                dwnld = c.get('https://randopitons.re/randonnee/'+i+'/trace/'+maptype)
                gudencoding=dwnld.text.encode('utf-8')
                gpxf=open('f.gpx','a+')
                gpxf.write(gudencoding)
                gpxf.close()
                try:
                    tree=xmlp.parse('f.gpx')
                    root=tree.getroot()
                    filename=root[1][0].text+".gpx"
                    os.rename('f.gpx',filename)
                except OSError, e:
                    print("Operating System error: {0}".format(e))
                except xml.etree.ElementTree.ParseError,e:
                print("something occuredwith the formating:{0}".format(e))
                os.remove('f.gpx')
                pass
            
            
            print("FINISHED WRITING FILES")
        except OSError, e:
                print("Operating System error: {0}".format(e))
        
        

    print(response.headers)
print(response.text)

