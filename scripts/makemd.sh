#!/bin/bash

tree -I ~* > ./docparts/02-directories.txt
cat ./docparts/* > ./README.md
