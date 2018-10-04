import xml.etree.ElementTree as xmlp
import re


def mapparsing(filetype,basicfilename):
    try:
        tree=xmlp.parse(basicfilename)
        root=tree.getroot()
        
        filename=root[1][0].text+".gpx"
        
        
        os.rename(basicfilename,filename)
    except OSError, e:
        print("Operating System error: {0}".format(e))
    except xml.etree.ElementTree.ParseError,e:
        print("Something occured with the formating:{0} . File is not retrievable, passing on next download.".format(e))
        os.remove(basicfilename)
        pass
   return filename
        
        #kml
        filename= root[0][10][1][0].text+".kml"
    
        #gpx
        filename=root[1][0].text+".gpx"
        
        #trk
        thefile=open("f.trk")
        for i in range(3):
            thefile.readline()
        name=thefile.readline()
        re.findall(r'\|(.*?)\|', filename)
