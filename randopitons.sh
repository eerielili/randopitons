#!/usr/bin/env bash
# Bash3 Boilerplate. Copyright (c) 2014, kvz.io

#set -o errexit
#set -o pipefail
#set -o nounset
#set -o xtrace

# Set magic variables for current file & dir
__dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
__file="${__dir}/$(basename "${BASH_SOURCE[0]}")"
__base="$(basename ${__file} .sh)"
__root="$(cd "$(dirname "${__dir}")" && pwd)" # <-- change this as it depends on your app
REGIONS=$(cat ${__dir}/regions.txt)
REGIONFILE="${__dir}/regions.txt"
MAPTYPE="gpx"
RDPUSER=
RDPUSERPASS=
LOGINOK=

#Filechecks
printf "Cirque de Cilaos\nCirque de Mafate\nCirque de Salazie\nEst\nNord\nOuest\nSud\nVolcan\nAilleurs\nAll" > $REGIONFILE

#https://stackoverflow.com/questions/4813092/how-to-read-entire-line-from-bash
#so we don't use a while loop
IFS=$'\n'

_download()
{

    while read linefromfile; do
        mkdir -p ${__dir}/randopfiles/"${linefromfile}"
        cd ${__dir}/randopfiles/"${linefromfile}"
        WEBREGION=$(echo ${linefromfile} | sed 's/ de /\-/g' | tr '[:upper:]' '[:lower:]')
        FILENBRS=$(wget -qO- https://randopitons.re/randonnees/region/${WEBREGION} | grep "<tr rid" | cut -d \" -f2)
        for nbr in $FILENBRS; do
            wget -w 3 --content-disposition --load-cookies ${__dir}/cookiejar.txt "https://randopitons.re/randonnee/${nbr}/trace/${MAPTYPE}"
        done
        cd ..
    done <$1
}

_help()
{

	man ${__dir}/randopitons.7.gz
	exit
}

_credentials()
{

	printf "\nYour username is $RDPUSER. (You can press CTRL+C to cancel the script if this info is incorrect)."
	printf "\nPassword (for randopitons.re): "
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


if [ "$1" = "" ];then
	_help
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
			printf "\nMaptype supplied is not correct"
			printf "Which map filetype you want to set : gpx(default),trk or kml ?"
			read -N 3 MAPTYPE
		done
		printf "\nThe $MAPTYPE maptype is a valid choice !"
		;;

	-lr | --list-regions)
		printf "Here's a list:\n"
		cat $REGIONFILE
		;;

	-lm | --list-maptypes)
		printf "These are the valid maptypes:\ngpx\nkml\ntrk"
		;;

	-r | --region )
		shift
		MATCHEDFILE="${__dir}/matched.txt"
		grep -iE "$1" $REGIONFILE > $MATCHEDFILE

		if [ -s $MATCHEDFILE ];then
			echo "Nothing matched or you entered an empty value."
			_help		
		fi

		printf "Your region choice was '$1'\nMatches are:\n"
		cat $MATCHEDFILE
		_download $MATCHEDFILE
		;;

	-a | --all )
		printf "\nThis will download all the hitchiking routes from all
        regions.\nIf no extension is specified (with -mp or --maptype), it will
        default to gpx.\nPausing for 5 seconds before downloading..."
		sleep 5	
		_download $REGIONFILE
		;;

	-em | --elevator-music )
		echo "Initiating elevator music"
		mpv --no-audio --really-quiet https://www.youtube.com/watch?v=KfNXGY9O5VY || printf "\nmpv is not installed."
		;;

	-h | --help )
		_help
                ;;

	* )
		_help
    esac
    shift
done
