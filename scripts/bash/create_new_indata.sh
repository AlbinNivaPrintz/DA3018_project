n=$1

echo "Initializing writing of new input file"
rm resources/unsocial_contigs_over_$n.txt 2>/dev/null
parallel python scripts/python/social_contig_remover.py resources/more_neighbours_than_$n.txt resources/unsocial_contigs_over_$n.txt ::: xaa xab xac xad
#python scripts/python/social_contig_remover.py resources/more_neighbours_than_$n.txt resources/unsocial_contigs_over_$n.txt no_doubles
