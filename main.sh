FILE=$1
n=$2

time bash scripts/bash/over_n_neighbours.sh $FILE $n
time bash scripts/bash/create_new_indata.sh $FILE $n
echo "New indata created."
python scripts/python/graph_class/__init__.py $n
