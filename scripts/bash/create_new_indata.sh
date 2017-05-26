rm ../../resources/unsocial_contigs.txt
split -l 16014193 ../../resources/Spruce_fingerprint_2017-03-10_16.48.olp.m4
parallel python ../python/social_contig_remover.py ../../resources/over_19_neighbours.txt ../../resources/unsocial_contigs.txt ::: xaa xab xac xad
rm xa*
