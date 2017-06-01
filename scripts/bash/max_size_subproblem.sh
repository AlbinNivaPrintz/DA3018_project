FILE=$1
cat $FILE | awk '{print NF}' | sort -r -n | head -1
