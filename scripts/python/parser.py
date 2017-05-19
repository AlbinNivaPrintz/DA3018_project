import graph_class as graph
import sys

def parse(filename, n_lines = -1):
    G = Graph()
    fileObject = open(filename, 'rb')
    n = 0
    for line in fileObject:
        if n == n_lines:
            break
        n += 1
        l = line.split()
        nodeA = l[0]
        nodeB = l[1]
        similarity = l[3]
        matchA = (l[5], l[6])
        lengthA = l[7]
        matchB = (l[9], l[10])
        lengthB = l[11]
        G.connect(nodeA, matchA, lengthA,
                  nodeB, matchB, lengthB,
                  similarity)
    return G

if __name__ == "__main__":
    args = tuple(sys.argv[1:])
    graf = parse(args)
    sys.stdout(graf)
