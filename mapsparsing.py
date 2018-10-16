import xml.etree.ElementTree as xmlp
import re
import errmsg as e

def mapparsing(maptype,basicfilename):
    try:
        root=tree.getroot()
        if maptype==1:
            tree=xmlp.parse(basicfilename)
            filename=root[1][0].text+".gpx"
        elif maptype==2:
            thefile=open(basicfilename)
            for i in range(3):
                thefile.readline()
            filename=re.findall(r'\|(.*?)\|', thefile.readline())[0]+".trk"
        elif maptype==3:
            tree=xmlp.parse(basicfilename)
            filename= root[0][10][1][0].text+".kml"  
        os.rename(basicfilename,filename)
    except OSError, e:
        print e.os
    except xmlp.ParseError, e:
        print e.formaterr
        print format(e)
        os.remove(basicfilename)
        pass
    return filename
        
