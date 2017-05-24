cat ../../resources/Spruce_fingerprint_2017-03-10_16.48.olp.m4 | awk '{print $1}'  > column_1_occurences.txt
echo 1
cat ../../resources/Spruce_fingerprint_2017-03-10_16.48.olp.m4 | awk '{print $2}'  > column_2_occurences.txt
echo 2
cat column_1_occurences.txt column_2_occurences.txt | sort | uniq -c > contig_occurences.txt
echo 3
rm column_1_occurences.txt
rm column_2_occurences.txt
cat contig_occurences.txt | awk '{if ($1>19) print $2}' > ../../resources/over_19_neighbours.txt
echo 4
rm contig_occurences.txt
