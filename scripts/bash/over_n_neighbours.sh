FILE=$1
n=$2

cut -f 1 $FILE > column_1_occurences.txt
echo "First column added."
cut -f 2 $FILE > column_2_occurences.txt
echo "Second column added."
cat column_1_occurences.txt column_2_occurences.txt | sort | uniq -c > resources/contig_occurences.txt
echo "Sorted."
rm column_1_occurences.txt
rm column_2_occurences.txt
cat resources/contig_occurences.txt | awk -v var=$n '{if ($1>var) print $2}' > resources/more_neighbours_than_$n.txt
echo "Social nodes found."
