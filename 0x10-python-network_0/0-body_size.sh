#!/usr/bin/bash env
#Displays size of the body
curl -sI "$1" | grep Content-Length | cut -d' ' -f2
