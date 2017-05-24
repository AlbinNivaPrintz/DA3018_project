rm unsocial_contigs.txt
time split -l 16014193 ../../resources/Spruce_fingerprint_2017-03-10_16.48.olp.m4
time parallel python ../python/social_contig_remover.py ::: xaa xab xac xad
wc -l unsocial_contigs.txt
rm xa*
