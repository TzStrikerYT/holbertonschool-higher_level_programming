#!/bin/bash
#Send POST request to url to validate if is a JSON or not
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
