import xml.etree.ElementTree as xmlp
import re
import errmsg as e

def mapparsing(filetype,basicfilename):
    try:
        root=tree.getroot()
        if filetype==1:
            tree=xmlp.parse(basicfilename)
            filename=root[1][0].text+".gpx"
        else filetype==2:
            tree=xmlp.parse(basicfilename)
            filename= root[0][10][1][0].text+".kml"
        elif filetype==3:
            thefile=open(basicfilename)
            for i in range(3):
                thefile.readline()
            filename=re.findall(r'\|(.*?)\|', thefile.readline())[0]
        os.rename(basicfilename,filename)
    except OSError, e:
        print e.os
    except xml.etree.ElementTree.ParseError, e:
        print e.formaterr
        print format(e)
        os.remove(basicfilename)
        pass
   return filename
        
