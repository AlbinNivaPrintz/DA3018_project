FILE=$1
n=$2
SIZE=`wc -l < $1`
rm column_1_occurences.txt 2>/dev/null
rm column_2_occurences.txt 2>/dev/null
split -l $((SIZE/4+1)) $FILE
parallel bash scripts/bash/contigs.sh ::: xaa xab xac xad
rm column_1_occurences.txt
rm column_2_occurences.txt
cat column_1_occurences.txt column_2_occurences.txt | sort | uniq -c > resources/contig_occurences.txt
echo "Finished search for all nodes."
cat resources/contig_occurences.txt | awk -v var=$n '{if ($1>var) print $2}' > resources/more_neighbours_than_$n.txt
echo "Finished search for all social nodes."
