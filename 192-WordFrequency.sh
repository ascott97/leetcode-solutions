#!/usr/bin/env bash

for i in $(cat words.txt); do echo $i; done | sort | uniq -c  | sort -nr | awk '{ i = $1; $1 = $2; $2 = i; print}'
