#!/bin/bash

cd /etc

sudo ln -s passwd passfile

mail -s "passtask"  -A passfile "write your email"
 

