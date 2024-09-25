#! /usr/bin/env bash

# Fait sur Debian

# Fonctions

select_random_stuff()
{
    input_file=$1
    
    number_of_lines=$(grep -c -E '^' $input_file)
    
    alea=$(shuf -i 1-$number_of_lines -n 1)
    
    selected=$(head -n $alea $input_file | tail -1)
    selected=$(echo "$selected" | cut -d '/' -f 1)
    selected=$(echo "$selected" | awk '{print $1}')
    
}

# Fin des fonctions

# Début du script

select_random_stuff $HOME/Scripts/Rédac/modes.list
echo "Le mode choisi est "$selected""

select_random_stuff $HOME/Scripts/Rédac/brawlers.list
echo "Et tu devras le jouer avec "$selected""
