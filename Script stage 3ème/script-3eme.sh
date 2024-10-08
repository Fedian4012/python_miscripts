#! /usr/bin/env bash

# Fait sur (et pour) Debian 12 "Bookworm" avec l'aide de mon père et mon grand-père pour des bouts de code


# packages_log="/tmp/packages_install.log"

################################
#        Fonctions             #
################################

check_package()
{
	package_name=$1
	if [ "$(dpkg -l | grep "$package_name" )" = "" ]
		then
		install_package "$package_name"
	fi
}

install_package()
{
   
    
read -p "Le paquet ""$package_name"" n'est pas installé. Voulez-vous l'installer (O/n) ? " answer
	if [[ "$answer" = [Oo*] ]]
		then
		    sudo apt-get install -y "$package_name"
		    echo "$package_name " >> "/tmp/packages_install.log"
	elif [[ "$answer" = [Nn*] ]]
		then
		echo "Ce paquet étant nécessaire, il est impossible de continuer."
		exit 0
	elif [[ "$answer" = "" ]]
		then
		    sudo apt-get install -y "$package_name"
		     echo "$package_name " >> "/tmp/packages_install.log"
	else
		echo "Veuillez répondre par oui ou non"
		install_package "$package_name"
	fi 
}

write_things()
{
thing_to_write=$1

xdotool type "$thing_to_write"
xdotool key Return
sleep 2
}

remove_created_files()
{
    file_to_remove=$1
if [ -f "$file_to_remove" ]
   then
       rm -f "$file_to_remove"
fi
}

################################
#       Fin des fonctions      #                                               #  
################################

################################
#       Début du script        #                                                #     
################################

# On vérifie la présence de gedit et xdotool, et on installe ce qui manque

check_package mousepad
check_package xdotool

# On supprime les fichiers créés précédemment s'ils sont là
remove_created_files /tmp/stage-fr
remove_created_files /tmp/packages_install.log

   
# On ouvre gedit, on tape le texte qui va bien puis on sauvegarde
echo "Le fichier créé par ce script se trouvera dans /tmp/stage-fr.txt." & sleep 5
mousepad /tmp/stage-fr.txt & sleep 2
write_things "Je m'appelle François Ruau,"
write_things "je suis né le 15/04/2011 à Nantes,"
write_things "et j'habite à Riaillé."
xdotool key Return
xdotool key Return
write_things "Je fais du Linux depuis un an,"
write_things "et je vous ai fait ce petit script"
write_things "pour vous montrer de quoi je suis capable."
write_things "Vous pouvez me contacter à l'adresse francois.ruau@free.fr."
write_things "J'ai aussi un GitHub à l'adresse https://github.com/FrancoisFedian/francois_repo"
xdotool key Control_L+S
killall mousepad

# On désinstalle les paquets installés par le script

if [[ "$(cat "/tmp/packages_install.log")" != "" ]]
then
    exit 0
else
    read -p "Voulez-vous désinstaller les paquets installés par le script ?" answer2
	if [[ "$answer2" = [Oo*] ]]
		then
		    sudo apt-get remove -y $(cat /tmp/packages_install.log)
	elif [[ "$answer2" = [Nn*] ]]
		then
		echo ""
		exit 0
	elif [[ "$answer2" = "" ]]
		then
		    sudo apt-get remove -y $(cat /tmp/packages_install.log")
	else
		echo "Veuillez répondre par oui ou non"
		sudo apt-get remove -y $(cat /tmp/packages_install.log)
	fi
fi

