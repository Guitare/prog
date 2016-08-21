#GUITARE PROG
# -*- coding: utf8 -*-
####################################
##### Pour windows dans le PATH ########
#pre-requis : PYTHON 2.7, youtube-dl###
####################################
###############################
###exemple : Nommé la variable environnementale comme vous le souhaitez:
#####puis dans sa valeur entrez sa direction comme l'exemple ci dessous: 
#####C:\Users\usernames\Desktop\youtube-dl.exe
##############################################
####Une fois pret lancé ytdl.py collé votre url la commande se charge du reste le fichier et enregistrer dans le Desktop ...
#################################################################################
################################################################################

import os
global var

def collecturl(): #recepteur/ecouteur url
    global var
    print "YTDL v.0.1.a by guitare"
    print "collez l'url puis tapez entrer..."
    var = raw_input()
    youyou(var)

def youyou (url):
    global var
    var = url
    os.system("youtube-dl "+ url) #os.system(cmd) exécute cmd
    print "Download succees!"
    
    
collecturl()        


          

