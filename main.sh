FILE=$1
n=$2
SKIP=$3

echo "Initializing preparation of inputfile..."
bash scripts/bash/over_n_neighbours.sh $FILE $n $SKIP
bash scripts/bash/create_new_indata.sh $n
echo "Finished input preparation."
python scripts/python/read_and_divide.py $n
rm resources/unsocial_contigs_over_$n.txt
