import getpass
import colorcode as clc
import errmsg as e


def mapfileinput():
    maptype = 0
    print clc.bold+"\n Which map file extension you would want to download ?"+clc.endc
    print """
    1. gpx (GPS Exchange Format)
    2. trk (CompeGPS Land Track File)
    3. kml (Keyhole Markup Language)\n"""

    while maptype<1 or maptype>3:
        try:
            maptype = input("You must enter a number between 1 and 3. Your choice ? ")
            int(maptype)
        except (KeyboardInterrupt, SystemExit):
            print e.sigkill
            exit()
        except SyntaxError:
            print "Defaulting to gpx. If this isn't what you wanted, you can always interrupt the script by pressing "+clc.bold+clc.okblue+"CTRL+C"+clc.endc
            maptype=1
    return maptype


def regioninput():
    zone = 0
    print clc.bold+"\n Which zone you would want to download ?"+clc.endc
    print """
    1. Cirque de Cilaos (Cilaos Circus)
    2. Cirque de Mafate (Mafate's Circus)
    3. Cirque de Salazie (Salazie's Circus)
    4. Est (East)
    5. Nord (North)
    6. Ouest (West)
    7. Sud (South)
    8. Volcan (Volcano)
    9. Ailleurs (Elsewhere)
    10. All \n"""
    
    while zone < 1 or zone > 10:
        try:
            zone =  input("You must enter a number between 1 and 10.  Your zone [Default is \"All\"]: ")
            int(zone)
        except (KeyboardInterrupt, SystemExit):
            print e.sigkill
            exit()
        except SyntaxError:
            print("\nDefaulting to All. If this isn't what you wanted, you can always interrupt the script by pressing "+clc.bold+clc.okblue+"CTRL+C"+clc.endc)
            zone = 10;
        except NameError:
            print "\nPlease enter a number between 1 and 10."
            zone = 0
    return zone

def loginmail():
    try:
        MAIL=raw_input("Your email to log in to randopitons.re : ")
    except KeyboardInterrupt:
        print e.sigkill
    return MAIL
    
def loginpass():
    try:
        PSW=getpass.getpass(prompt="Your password to log in to randopitons.re: ")
    except KeyboardInterrupt:
        print e.sigkill
    return PSW
