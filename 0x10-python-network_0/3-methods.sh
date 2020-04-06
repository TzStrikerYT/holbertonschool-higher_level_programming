#!/usr/bin/env bash
#Displays all methods http
curl -sI "$1" | grep Allow | cut -d" " -f2-
