FILE=$1
n=$2

time bash over_n_neighbours.sh $FILE $n
time bash create_new_indata.sh $FILE $n
echo "New indata created."
python ../python/graph_class/__init__.py ../../resources/unsocial_contigs_over_$n.txt $n
