#!/bin/bash

username = # enter username
password = # enter password 
# download lineStrokes
wget --user=$username --password=$password http://www.fki.inf.unibe.ch/DBs/iamOnDB/data/lineStrokes-all.tar.gz
tar -xzvf lineStrokes-all.tar.gz

# download ascii
wget --user=$username --password=$password http://www.fki.inf.unibe.ch/DBs/iamOnDB/data/ascii-all.tar.gz
tar -xzvf ascii-all.tar.gz

# download originals
wget --user=$username --password=$password http://www.fki.inf.unibe.ch/DBs/iamOnDB/data/original-xml-all.tar.gz
tar -xzvf original-xml-all.tar.gz




