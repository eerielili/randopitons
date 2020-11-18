#!/usr/bin/env bash

#set -o errexit
#set -o pipefail
#set -o nounset
#set -o xtrace
BOLD='\033[01m'
UNDL='\033[04m'
GREEN='\033[32m'
RED='\033[31m'
STYLE_END='\033[0m'


# Set magic variables for current file & dir
MANPATH="/usr/share/man:$HOME/.local/share/man"
DATADIR="$HOME/.local/share/randopitons"
COOKIES_FILE="$DATADIR/cookies.txt"
REGIONFILE="$DATADIR/regions.txt"
S256_REGIONFILE="20eb46831f436bb467b850835c7efde1d51742434fcea9addf4754b9545aae47"
MATCHEDFILE="$(mktemp)"
MAPTYPE="gpx"
RDPUSER=
RDPUSERPASS=

#Filechecks
mkdir -p $DATADIR
if [ ! -w $REGIONFILE  ]; then
    printf "\nRegenerating $REGIONFILE...\n"
    printf "Cirque de Cilaos\nCirque de Mafate\nCirque de Salazie\nEst\nNord\nOuest\nSud\nVolcan\nAilleurs\nAll" > $REGIONFILE
fi

if [ "$S256_REGIONFILE" != "$(sha256sum $REGIONFILE | cut -d' ' -f1)" ]; then
    printf "\n$REGIONFILE sha256sum not matching, regenerating...\n"
    printf "Cirque de Cilaos\nCirque de Mafate\nCirque de Salazie\nEst\nNord\nOuest\nSud\nVolcan\nAilleurs\nAll" > $REGIONFILE
fi

#https://stackoverflow.com/questions/4813092/how-to-read-entire-line-from-bash
#so we don't use a while loop
IFS=$'\n'

_check_connectivity()
{
    ping -c 1 -q -W 3 example.com > /dev/null 2>&1 || (printf "No internet connectivity. Check your network settings and status.\n" && return 1)
}

_download()
{ 
    _check_connectivity || exit 1
    while read linefromfile; do
        if [ ! -s $COOKIES_FILE ]; then
            printf "\nCookie file not detected. Re-login using the -u switch to regenerate it.\n"
            exit 1
        fi

        DOWNLOAD_DIR="${DATADIR}/tracefiles/${linefromfile}/${MAPTYPE}"
        printf "Trace files for the ${WEBREGION} with extension '${MAPTYPE}' will be downloaded to ${BOLD}$DOWNLOAD_DIR${STYLE_END}"

        mkdir -p "$DOWNLOAD_DIR"
        cd "$DOWNLOAD_DIR"
        WEBREGION=$(echo ${linefromfile} | sed 's/ de /\-/g' | tr '[:upper:]' '[:lower:]')
        printf "\nExtracting URL to download geo files from...\n"
        TRACES=$(curl --silent  https://randopitons.re/randonnees/region/${WEBREGION} | grep "<tr rid" | cut -d \" -f2) || (printf "Failed extraction. Aborting.\n" && exit 1)

        for trace in $TRACES; do
            sleep 3
            wget --quiet --no-config --content-disposition --load-cookies $COOKIES_FILE "https://randopitons.re/randonnee/${trace}/trace/${MAPTYPE}" && printf "${GREEN}Succesfully download trace ${trace}${STYLE_END}\n" || (printf "${RED}Failed downloading trace ${trace} ...${STYLE_END}\n")
        done

        cd ..
    done <$1
}

_help()
{

	if ! man randopitons; then
        mkdir -p ~/.local/share/man/man7
        cp randopitons.7.gz ~/.local/share/man/man7/
        man randopitons
    fi
}

_credentials()
{
    while [ -z $RDPUSER ]; do
        printf "No username detected on -u switch. Enter it: "
        read -r RDPUSER
    done
	printf "\nYour username is $RDPUSER. (You can press CTRL+C to cancel the script if this info is incorrect)."
	printf "\nPassword (for randopitons.re): "
	read -s RDPUSERPASS
}

_logincheck()
{
    _check_connectivity || exit 1
	LOGINTEST=$(wget --no-config -qO- --save-cookies $COOKIES_FILE --keep-session-cookies --post-data="mail=${RDPUSER}&password=${RDPUSERPASS}" --delete-after https://randopitons.re/connexion | grep "L'adresse mail ou le mot de passe ne correspondent pas.")
	if [ -z "$LOGINTEST" ];then
		printf "${GREEN}Login is successful.${STYLE_END}\n"
		mkdir -p "$DATADIR/randopfiles"
	else
		echo "${RED}Login is not successful.${STYLE_END}\n"
		rm  $COOKIES_FILE
		exit
	fi
}


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
        
        while true; do
            case $MAPTYPE in
                gpx | trk | kml)
                    break;;
                *)
                    printf "\nThe supplied map extension is not correct\n"
                    printf "Which map filetype you want to set : gpx(default),trk or kml ?"
                    read -r MAPTYPE;;
            esac
        done
		printf "\nThe $MAPTYPE map extension has been selected !\n"
		;;

	-lr | --list-regions)
		printf "\n%s\n" "$(cat $REGIONFILE)"
		;;

	-lm | --list-maptypes)
		printf "These are the valid maptypes:\ngpx\nkml\ntrk\n"
		;;

	-r | --region )
		shift
		

		if ! grep -iE "$1" $REGIONFILE > $MATCHEDFILE; then
			printf "No region matched or you entered an empty value.\n"
            exit 1
		fi
        
		printf "Argument '$1' matched. Proceeding with download...\n"
        if [ "$1" != 'All' ]; then
		    _download $MATCHEDFILE
        else
            _download $REGIONFILE
        fi
		;;

	-a | --all )
		printf "\nThis will download all the hitchiking routes from all
        regions.\nIf no extension is specified (with -mp or --maptype), it will
        default to gpx."
		_download $REGIONFILE
		;;

	-h | --help )
		_help
                ;;
     * )
        _help
        ;;
    esac
    shift
done
