#!/bin/bash/
while true
do
  a=$(gnome-screensaver-command -q)
  sleep 1
  b=$(gnome-screensaver-command -q)
  if [ "$a" == "$b" ]
    then
    echo "ok"
  else
    paplay ./desktop-login.oga
  fi
done

