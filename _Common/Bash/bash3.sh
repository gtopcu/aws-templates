#!/bin/bash
#sh bash.sh 1 2 3

typeset -i int=3 #same as declare -> defines integer constant
echo $int

func1 () { echo "1"; }

func2 ()
{
  echo $1 $2 #function arguments
}

func1
func2 10 11

echo "Done"


