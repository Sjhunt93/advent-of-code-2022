#!/usr/bin/env bash

start_index=1
end_index=25
for ((i=start_index; i<=end_index; i++)); do
  # format a dirpath with the 3-digits index
  printf -v dirpath 'solutions/%d/1' $i
  mkdir -p -- "$dirpath"
  printf -v dirpath 'solutions/%d/2' $i
  mkdir -p -- "$dirpath"
  printf -v dirpath 'solutions/%d/notes.md' $i
  touch "$dirpath"
done