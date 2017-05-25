
cut -f 1 ../../resources/Spruce_fingerprint_2017-03-10_16.48.olp.m4 > column_1_occurences.txt
echo "First column added."
cut -f 2 ../../resources/Spruce_fingerprint_2017-03-10_16.48.olp.m4 > column_2_occurences.txt
echo "Second column added."
cat column_1_occurences.txt column_2_occurences.txt | sort | uniq -c > contig_occurences.txt
echo "Sorted."
rm column_1_occurences.txt
rm column_2_occurences.txt
cat contig_occurences.txt | awk '{if ($1>19) print $2}' > ../../resources/over_19_neighbours.txt
echo "Social nodes found."
rm contig_occurences.txt
