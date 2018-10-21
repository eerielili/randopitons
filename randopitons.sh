#!/bin/bash
# ANSI color codes
RS="\e[0m"    # reset
HC="\e[1m"    # hicolor
UL="\e[4m"    # underline
INV="\e[7m"   # inverse background and foreground
FBLK="\e[30m" # foreground black
FRED="\e[31m" # foreground red
FGRN="\e[32m" # foreground green
FYEL="\e[33m" # foreground yellow
FBLE="\e[34m" # foreground blue
FMAG="\e[35m" # foreground magenta
FCYN="\e[36m" # foreground cyan
FWHT="\e[37m" # foreground white
BBLK="\e[40m" # background black
BRED="\e[41m" # background red
BGRN="\e[42m" # background green
BYEL="\e[43m" # background yellow
BBLE="\e[44m" # background blue
BMAG="\e[45m" # background magenta
BCYN="\e[46m" # background cyan
BWHT="\e[47m" # background white
BLD="\e[1m" # BOLD text
# ANSI color codes

#https://stackoverflow.com/questions/4813092/how-to-read-entire-line-from-bash
#so we don't use a while loop
IFS=$'\n'

tellusage()
{
echo -e "${BLD}PURPOSE:${RS} With this script, you will be able to download gpx,trk and kml traces for hitchiking on the Reunion Isle.\n
${BLD}USAGE$RS: randopitons.sh -u \"username@mymail.com\" -mp maptype. You can supply the -a flag to the previous example to download all regions \n
${BLD}MAPTYPE FORMAT:$RS gpx, trk or kml"

}

credentials()
{
RDPUSER=$1
echo -e "\nYour username is $RDPUSER."
echo -e "\nPassword (for randopitons.re): "
read -s RDPUSERPASS
}


MAPTYPE="gpx"
RDPHOME=$HOME"/Randopitons"
RDPUSER=
RDPUSERPASS=

if [ "$1" = "" ];then
	tellusage
fi

while [ "$1" != "" ]; do

    case $1 in
        -u | --username )  
		shift
                credentials
                ;;

        -mp | --maptype )	
		shift
		MAPTYPE=$1
		echo -e "\nChosen maptype is $1"
		while [ $MAPTYPE != "gpx" -a $MAPTYPE != "trk" -a $MAPTYPE != "kml" ]
		do	
			echo -e $HC$BRED"${FYEL}\nMaptype supplied is not correct$RS"
			echo -e "Which map filetype you want to set : ${BLD}gpx(default),trk or kml ?$RS$RS$RS"
			read -N 3 MAPTYPE
		done
		echo -e $HC$FGRN"\n$MAPTYPE maptype is a valid choice !"$RS
		;;
	-a | --all )
		echo -e "\nThis will download all the hitchiking routes from all regions."
		echo -e "\nIf no maptype is specified (with -mp or --maptype), it will default to .gpx filetype"
		;;

	

#	-h | --help )           tellusage
#                               exit
#                               ;;
        * )                     tellusage
                                exit 1
    esac
    shift
done


# echo -e "\n purz"
