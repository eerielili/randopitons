#!/usr/bin/env bash
# Bash3 Boilerplate. Copyright (c) 2014, kvz.io
clear

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
  for nbr in $FILENBRS;do
  # you can change the delay for the -w option. I'm not held responsible for any DDoS complaints.
   wget -w 2 --content-disposition --load-cookies ${__dir}/cookiejar.txt "https://randopitons.re/randonnee/${nbr}/trace/${MAPTYPE}"
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

_crearegfile()
{
 echo "Region file doesn't exist or has been modified, we will (re)create it."
 echo -e "Cirque de Cilaos\nCirque de Mafate\nCirque de Salazie\nEst\nNord\nOuest\nSud\nVolcan\nAilleurs\nAll">$REGIONFILE
}


MAPTYPE="gpx"
RDPUSER=
RDPUSERPASS=
LOGINOK=

#Filechecks
echo -e "Cirque de Cilaos\nCirque de Mafate\nCirque de Salazie\nEst\nNord\nOuest\nSud\nVolcan\nAilleurs\nAll">/tmp/regions.txt
_ORIGREGIONMD5=$(md5sum /tmp/regions.txt)
_CURRENTREGIONMD5=$(md5sum $REGIONFILE)
echo $_ORIGREGIONMD5 > /tmp/regionshash.txt
if [ -s $REGIONFILE ];then
	echo "Region file is already there. OK"
elif [ "$_CURRENTREGIONMD5" != "$_ORIGREGIONMD5" ];then
	_crearegfile
else
    _crearegfile
fi


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
			echo -e "\nMaptype supplied is not correct"
			echo -e "Which map filetype you want to set : gpx(default),trk or kml ?"
			read -N 3 MAPTYPE
		done
		echo -e "\nThe $MAPTYPE maptype is a valid choice !"
		;;

	-lr | --list-regions)
		echo -e "Here's a list:\n"
		cat $REGIONFILE
		;;

	-lm | --list-maptypes)
		echo "These are the valid maptypes:gpx\nkml\ntrk"
		;;

	-r | --region )
		shift
		MATCHEDFILE="${__dir}/matched.txt"
		grep -iE "$1" $REGIONFILE > $MATCHEDFILE
		if [ -s  ];then
			echo "Nothing matched or you entered an empty value."
			_help		
		fi

		echo -e "Your region choice was '$1'\n See what matched :"
		cat $MATCHEDFILE
		_download $MATCHEDFILE
		;;

	-a | --all )
		echo -e "\nThis will download all the hitchiking routes from all regions.\nIf no maptype is specified (with -mp or --maptype), it will default to .gpx filetype.\nPausing for 5 seconds before launching it."
		_download $REGIONFILE
		sleep 5	
		;;

	-em | --elevator-music )
		echo "Initiating elevator music"
		mpv --no-audio --really-quiet https://www.youtube.com/watch?v=KfNXGY9O5VY || echo -e "\nmpv is not installed."
		;;

	-h | --help )
		_help
                ;;

	* )
		_help
    esac
    shift
done
