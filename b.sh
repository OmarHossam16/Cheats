#!/usr/bin/bash

echo Hello World!

NAME="Omar Hossam"
echo "My name is $NAME or ${NAME}"

# USER INPUT and store in var NAME
read -p "Enter your name: " NAME


if [ "$NAME" == "Omar Hossam" ]
then
  echo "Your name is Omar Hossam"
elif [ "$NAME" == "Hossam" ]
then  
  echo "Your name is Hossam"
else 
  echo "Your name is NOT Omar Hossam or Hossam"
fi



########
# -eq  =
# -ne  !=
# -gt  >
# -ge  >=
# -lt  <
# -le  <=
########
######## True If file is
# -d file > Directory
# -f file > File
# -r file > Readable
# -w file > Writable
# -x file > Executable
# -s file > (Size > 0)
# -u file > User id is set on file
# -g file > Group ID is set on file
########

#CASE STATEMENT
read -p "Are you 21 or over? Y/N " ANSWER
case "$ANSWER" in 
  [yY] | [yY][eE][sS])
    echo "Y"
    ;;
  [nN] | [nN][oO])
    echo "N"
    ;;
  *)
    echo "else"
    ;;
esac

for n in $NAME; do
    echo "Hello $n"
done

for ((i = 0 ; i < 100 ; i++)); do
  echo $i
done

while true; do
  ···
done

#FOR LOOP TO RENAME FILES

for FILE in $(ls *.txt)
  do
    echo "Renaming $FILE to new-$FILE"
    mv $FILE $NEW-$FILE
done

#READ LINES
< file.txt | while read line; do
  echo $line
done

# FUNCTION
function hello() {
  echo "Hello"
}
hello

function with_params() {
  echo "Hello, I am $1 and I am $2"
}
with_params "Omar" "20"

#WRITE TO A FILE
echo "Hello World" >> "hello/world.txt"