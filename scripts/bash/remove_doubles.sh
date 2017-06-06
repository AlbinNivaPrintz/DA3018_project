FILE=$1
cut -f 1,2 $FILE | awk '{if ($1<$2) print $1"\t"$2; else print $2"\t"$1}' | sort | uniq > no_doubles
