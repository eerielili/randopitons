import xml.etree.ElementTree as xmlp
import re

def gpxparsing():
    try:
        tree=xmlp.parse('f.gpx')
        root=tree.getroot()
        filename=root[1][0].text+".gpx"
        os.rename('f.gpx',filename)
    except OSError, e:
        print("Operating System error: {0}".format(e))
    except xml.etree.ElementTree.ParseError,e:
        print("Something occured with the formating:{0} . File is not retrievable, passing on next download.".format(e))
        os.remove('f.gpx')
        pass
   return filename

    
def kmlparsing():
    
    try:
        tree=xmlp.parse('f.kml')
        root=tree.getroot()
        filename= root[0][10][1][0].text+".kml"
    except OSError, e:
        print("Operating System error: {0}".format(e))
    except xml.etree.ElementTree.ParseError,e:
        print("Something occured with the formating:{0} . File is not retrievable, passing on next download.".format(e))
        os.remove('f.kml')
        pass
    return filename
    
def trkparsing():
    try:
        tree=xmlp.parse('f.gpx')
        root=tree.getroot()
        filename=root[1][0].text+".gpx"
        os.rename('f.gpx',filename)
    except OSError, e:
        print("Operating System error: {0}".format(e))
    except xml.etree.ElementTree.ParseError,e:
        print("Something occured with the formating:{0} . File is not retrievable, passing on next download.".format(e))
        os.remove('f.gpx')
        pass
    return filename
