#!/bin/bash

if [ -s "./regions.txt" ];then
	"Region file is already there. OK"
else
	echo "Cirque de Cilaos
Cirque de Mafate
Cirque de Salazie
Est
Nord
Ouest
Sud
Volcan
Ailleurs
All">regions.txt
fi