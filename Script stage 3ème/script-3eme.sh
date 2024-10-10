#! /usr/bin/env bash

# Fait sur (et pour) Debian 12 "Bookworm" avec l'aide de mon père et mon grand-père

################################
#        Fonctions                                                                       #
################################
check_package()
{
	package_name=$1
	if [[ "$(dpkg -l | grep "$package_name" )" = "" ]]
		then
		install_package "$package_name"
	fi
}

install_package()
{
read -p "Le paquet ""$package_name"" n'est pas installé. Voulez-vous l'installer (O/n) ? " answer
	if [[ "$answer" = [[Oo*]] ]]
		then
		sudo apt-get install -y "$package_name"
	elif [[ "$answer" = [[Nn*]] ]]
		then
		echo "Ce paquet étant nécessaire, il est impossible de continuer."
		exit 0
	elif [[ "$answer" = "" ]]
		then
		sudo apt-get install -y "$package_name"
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
################################
#       Fin des fonctions      #                                               #  
################################

################################
#       Début du script        #                                                #     
################################

# On vérifie si on est bien sous X11
session_type=$(echo $XDG_SESSION_TYPE)


if [[ "$session_type" = "wayland" ]]
then
    echo "Vous n'êtes pas sous Xorg. Il est impossible de continuer. Veuillez vous déconnecter, vous reconnecter sous Xorg et relancer le script."
    exit 1
fi

# On vérifie la présence de gedit et xdotool, et on installe ce qui manque
check_package gedit
check_package xdotool

# On vérifie si le fichier cible existe déjà, et si c'est le cas, on le supprime
if [[ -f /tmp/stage-fr ]]
   then
       rm -f /tmp/stage-fr
fi
   
# On ouvre mousepad, on tape le texte qui va bien puis on sauvegarde
echo "Le fichier créé par ce script se trouvera dans /tmp/stage-fr." & sleep 5
mousepad /tmp/stage-fr & sleep 2
write_things "Je m'appelle François Ruau,"
write_things "je suis né le 15/04/2011 à Nantes,"
write_things "et j'habite à Riaillé."
write_things "Je fais du Linux depuis un an,"
write_things "et je vous ai fait ce petit script"
write_things "pour vous montrer de quoi je suis capable."
write_things "Vous pouvez me contacter à l'adresse francois.ruau@free.fr."
xdotool key Control_L+S
killall mousepad
