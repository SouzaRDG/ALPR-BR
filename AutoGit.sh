#!/bin/bash
#
# It will add the whole folder them make a commit and push
# Just because im kinda lazy and forget to make a commit and push after add


# Checking if git is initialized, else it will initialize git

if [ ! -d "./.git" ]
then
	echo "Initializing Git..."
	git init >/dev/null
else
	echo "Git already initialized, adding archives"
fi


git add * >/dev/null

echo "Arquivos adicionados" 

# Be careful cause it will remove all ignored files 
# (delete them permanently)

git add -u :/ >/dev/null
echo "Removidos arquivos excluídos"

#    First variable is for the commit name

git commit -m $1 >/dev/null

#

git push origin master
