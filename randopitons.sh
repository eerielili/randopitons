#!/usr/bin/env bash
# Bash3 Boilerplate. Copyright (c) 2014, kvz.io


#set -o errexit
#set -o pipefail
#set -o nounset
set -o xtrace

# Set magic variables for current file & dir
__dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
__file="${__dir}/$(basename "${BASH_SOURCE[0]}")"
__base="$(basename ${__file} .sh)"
__root="$(cd "$(dirname "${__dir}")" && pwd)" # <-- change this as it depends on your app


#https://stackoverflow.com/questions/4813092/how-to-read-entire-line-from-bash
#so we don't use a while loop
IFS=$'\n'

_tellusage()
{
	echo -e "${BLD}PURPOSE:${RS} With this script, you will be able to download gpx,trk and kml files for hitchiking on the Reunion Isle.\n
${BLD}USAGE$RS: . ./randopitons.sh option1 option2 option3
The following options are mandatory:
	--username/-u \"your-username-or-email@randopitons.re\": After that, you will be prompted for your password (it won't display it as you type so don't worry, it's for protecting you from curious peoples looking at you screen (a.k.a shouldersurfing).

Facultative:
	--maptype/-mp maptype: Can be used to specify a particular filetype to download between the 3 choices available. See \"-lm\" for more info
	--list-regions/-lr: Display the list of available regions.
	--list-maptype/-lm: Display the list of available maptypes.
	--region/-r \"string\": Will download the matching regions from the string.
	--all/-a: Will download all the files from all regions."

}

_credentials()
{

	echo -e "\nYour username is $RDPUSER. (You can press CTRL+C to cancel the script if this info is incorrect)."
	echo -e "\nPassword (for randopitons.re): "
	read -s RDPUSERPASS
}

_logincheck()
{
	LOGINTEST=$(wget -qO- --save-cookies ${__dir}/cookiejar.txt --keep-session-cookies --post-data="mail=${RDPUSER}&password=${RDPUSERPASS}" --delete-after https://randopitons.re/connexion | grep "L'adresse mail ou le mot de passe ne correspondent pas.")
	if [ -z "$LOGINTEST" ];then
		echo "Login is successful."
		LOGINOK=true
		mkdir ${__dir}/randopfiles
	else
		echo "Login is not successful."
		LOGINOK=false
		rm  ${__dir}/cookiejar.txt
		exit
	fi
}

#Filechecks
if [ -s "${__dir}/regions.txt" ];then
	echo "Region file is already there. OK"
else
	echo "Region file doesn't exist, we will create it."
	echo -e "Cirque de Cilaos\nCirque de Mafate\nCirque de Salazie\nEst\nNord\nOuest\nSud\nVolcan\nAilleurs\nAll">${__dir}/regions.txt
fi

if [ -s "${__dir}/webregions.txt" ];then
	echo "Webegion file is already there. OK"
else
	echo "Webregion file doesn't exist, we will create it."
	echo -e "cirque-cilaos\ncirque-mafate\ncirque-salazie\nest\nnord\nouest\nsud\nvolcan\nailleurs">${__dir}/webregions.txt
	fi

REGIONS=$(cat ${__dir}/regions.txt)
MAPTYPE="gpx"
RDPUSER=
RDPUSERPASS=
LOGINOK=

if [ "$1" = "" ];then
	_tellusage
fi

while [ "$1" != "" ]; do

    case $1 in
        -u | --username )  
		shift
		RDPUSER="$1"
                _credentials
		_logincheck
		
		;;

        -mp | --maptype )	
		shift
		MAPTYPE="$1"
		while [ $MAPTYPE != "gpx" -a $MAPTYPE != "trk" -a $MAPTYPE != "kml" ]
		do	
			echo -e "\nMaptype supplied is not correct"
			echo -e "Which map filetype you want to set : ${BLD}gpx(default),trk or kml ?$RS"
			read -N 3 MAPTYPE
		done
		echo -e $HC$FGRN"\nThe $MAPTYPE maptype is a valid choice !"$RS
		;;
	-lr | --list-regions)
		echo -e "Here's a list:\n$REGIONS"
		;;
	-lm | --list-maptype)
		echo "These are the valid maptypes:gpx\nkml\ntrk"
		;;
	-r | --region )
		shift
		matching=$(grep -iE "$1" ${__dir}/regions.txt)
		if [ "$1" = "" -o "$matching" = "" ];then
			echo "Nothing matched or you entered an empty value."
			_tellusage
		fi

		echo -e "Your region choice was '$1'\n See what matched :"
		echo -e $HC$FCYN"$matching"$RS
		webmatching=$(echo $matching | sed 's/ de /\-/g' | tr '[:upper:]' '[:lower:]')
		FILENBRS=$(wget -qO- https://randopitons.re/randonnees/region/${webmatching} | grep "<tr rid" | cut -d \" -f2)
		for nbr in $FILENBRS;do
			wget --content-disposition --load-cookies ${__dir}/cookiejar.txt "https://randopitons.re/randonnee/${nbr}/trace/${MAPTYPE}"
		done
		;;
	-a | --all )
			echo -e "\nThis will download all the hitchiking routes from all regions.\nIf no maptype is specified (with -mp or --maptype), it will default to .gpx filetype.\n${BLD}Pausing for 5 seconds before launching it.$RS"
			sleep 5	
			while read linefromfile; do
  				mkdir "${linefromfile}"
				cd "${linefromfile}"
				WEBREGION=$(echo ${linefromfile} | sed 's/ de /\-/g' | tr '[:upper:]' '[:lower:]')
				FILENBRS=$(wget -qO- https://randopitons.re/randonnees/region/${WEBREGION} | grep "<tr rid" | cut -d \" -f2)
				for nbr in $FILENBRS;do
					wget --content-disposition --load-cookies ${__dir}/cookiejar.txt "https://randopitons.re/randonnee/${nbr}/trace/${MAPTYPE}"
				done
			done <${__dir}/regions.txt
		
		;;

	-h | --help )           _tellusage
                               ;;
        * )                     _tellusage
    esac
    shift
done
