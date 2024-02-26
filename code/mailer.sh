#!/bin/sh
printf "Mailer loop has started\n"
while true
do
  MESSAGE=$(nc -l -p 33333)
  msg="{\"Subject\":{\"Data\":\"Mailer Alert\"},\"Body\":{\"Text\":{\"Data\":\"${MESSAGE}\"}}}"
  echo $msg
  sleep 1
done
