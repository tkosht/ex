#!/bin/sh




sudo echo "deb http://cz.archive.ubuntu.com/ubuntu xenial main universe" \
    | sudo tee -a /etc/apt/sources.list
sudo apt install libjpeg62 -y
sudo apt install r-base r-base-dev -y

#sudo add-apt-repository ppa:marutter/rrutter
#sudo apt-get update
#sudo apt-get install r-base r-base-dev

url_rstudio="https://download1.rstudio.org/rstudio-xenial-1.1.423-amd64.deb"
filename_rstudio=`basename $url_rstudio`
wget $url_rstudio -O ~/Downloads/$filename_rstudio
sudo dpkg -i ~/Downloads/$filename_rstudio

# - to install r packages like lintr, igraph, ...
sudo apt install libssl-dev libcurl4-openssl-dev libxml2-dev -y

