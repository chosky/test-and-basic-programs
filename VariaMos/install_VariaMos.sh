#!/bin/bash

#
# Created: 11/10/17
# User: Jose David Henao Ocampo (Monitor of EDS - EAFIT)
#
# 
# Purpose: This program do an automatical instalation of VariaMos and SWI-Prolog
#          with his necesary dependeces an configuration of envairoment variables
#          for Linux.
#
# Modifications:
# 

function append_to_file {
    echo $1 >> $2
}

declare osInfo;
if [ -f /etc/redhat-release ]; then
    osInfo="yum"
elif [ -f /etc/arch-release ]; then
    osInfo="pacman"
elif [ -f /etc/debian_version ]; then
    osInfo="apt-get"
fi

if [ -a /usr/bin/java ]; then
    echo "Java is installed"
else
    if [ $osInfo = 'yum' ]; then
	echo "Not yet"
    elif [ $osInfo = 'pacman' ]; then
	echo "Not yet"
    elif [ $osInfo = 'apt-get' ]; then
	sudo apt-get update
	sudo apt-get install openjdk-8-jdk
    fi
fi
if [ -a /usr/bin/swipl ]; then
    echo "SWI-Prolog is installed"
else
    if [ $osInfo = 'yum' ]; then
	echo "Not yet"
    elif [ $osInfo = 'pacman' ]; then
	echo "Not yet"
    elif [ $osInfo = 'apt-get' ]; then
	sudo apt-get update
	sudo apt-get install default-jre
	sudo apt-add-repository ppa:swi-prolog/stable
	sudo apt-get update
	sudo apt-get install swi-prolog swi-prolog-java
    fi
fi
append_to_file "export SWI_HOME_DIR=/usr/lib/swi-prolog" $HOME/.bashrc
append_to_file "export PATH=$PATH:$SWI_HOME_DIR/lib/:$SWI_HOME_DIR/lib/jpl.jar" $HOME/.bashrc

echo "The last step is download VariaMos in this link (PLEASE DOWNLOAD THE LAST VERSION): "
echo "https://variamos.com/home/variamos/downloads/" 
echo "Can you opend VariaMos ever you want with only one click or executing: "
echo "    java -jar variamos-<<version of VariaMos>>.jar "
echo "ENJOY IT :) "
