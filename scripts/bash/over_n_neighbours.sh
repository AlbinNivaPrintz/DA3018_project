FILE=$1
n=$2
SKIP=$3
rm column_1_occurences.txt 2>/dev/null
rm column_2_occurences.txt 2>/dev/null
[ -z "$SKIP" ] && bash scripts/bash/remove_doubles.sh $FILE
[ -z "$SKIP" ] && echo "Doubles removed."
[ -z "$SKIP" ] && SIZE=`wc -l < no_doubles`
[ -z "$SKIP" ] && split -l $((SIZE/4+1)) no_doubles && rm no_doubles
[ -z "$SKIP" ] && echo "Indata splitted."
[ -z "$SKIP" ] && parallel bash scripts/bash/contigs.sh ::: xaa xab xac xad
[ -z "$SKIP" ] && cat column_1_occurences.txt column_2_occurences.txt | sort | uniq -c > resources/contig_occurences.txt
[ -z "$SKIP" ] && rm column_1_occurences.txt
[ -z "$SKIP" ] && rm column_2_occurences.txt
[ -z "$SKIP" ] && echo "Finished search for all nodes."
cat resources/contig_occurences.txt | awk -v var=$n '{if ($1>var) print $2}' > resources/more_neighbours_than_$n.txt
echo "Finished search for all social nodes."
