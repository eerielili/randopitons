import xml.etree.ElementTree as xmlp
import re
import errmsg as reeee
import os
def mapparsing(maptype,basicfilename):
    try:
        tree=xmlp.parse(basicfilename)
        root=tree.getroot()
        if maptype==1:
            filename=root[1][0].text+".gpx"
        elif maptype==2:
            thefile=open(basicfilename)
            for i in range(3):
                thefile.readline()
            filename=re.findall(r'\|(.*?)\|', thefile.readline())[0]+".trk"
        elif maptype==3:
            filename= root[0][10][1][0].text+".kml"  
        os.rename(basicfilename,filename)
    except OSError, e:
        print reeee.os
    except xmlp.ParseError, er:
        print reeee.formaterr
        print format(er)
        os.remove(basicfilename)
        pass
    
        
