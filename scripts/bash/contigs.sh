FILE=$1
cut -f 1 $FILE >> column_1_occurences.txt
cut -f 2 $FILE >> column_2_occurences.txt
