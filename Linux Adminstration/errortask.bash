#!/bin/bash

grep -r power /sys/ 2> /dev/null >Errortask
gedit Errortask

mail -s "Error" -A Errortask "Write your email"
