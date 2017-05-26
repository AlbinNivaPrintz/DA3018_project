FILE=$1
n=$2

echo "Initializing preparation of inputfile..."
time bash scripts/bash/over_n_neighbours.sh $FILE $n
time bash scripts/bash/create_new_indata.sh $FILE $n
echo "Finished input preparation."
python scripts/python/read_and_divide.py $n
rm resources/unsocial_contigs_over_$n.txt
