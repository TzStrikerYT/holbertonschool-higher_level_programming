#!/usr/bin/env bash
#Displays size of the body
curl -sI "$1" | grep Content-Length | cut -d' ' -f2
