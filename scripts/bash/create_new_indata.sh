FILE=$1
n=$2
SIZE=`wc -l < $1`

rm resources/unsocial_contigs_over_$n.txt 2>/dev/null
parallel python scripts/python/social_contig_remover.py resources/more_neighbours_than_$n.txt resources/unsocial_contigs_over_$n.txt ::: xaa xab xac xad
rm xa*
