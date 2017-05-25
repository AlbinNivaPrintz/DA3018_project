import sys

contig_dict = {}

with open(str(sys.argv[1]), 'r') as remove_file:
    for line in remove_file:
        line = line[:-1]
        contig_dict[line] = 1

with open(str(sys.argv[2]), 'a') as result:
    with open(str(sys.argv[3]), 'r') as indata:
        for line in indata:
            line = line.split()
            if line[0] in contig_dict:
                continue
            if line[1] in contig_dict:
                continue
            else:
                result.write(line[0]+'  '+line[1]+'  '+line[2]+'  '+line[3]
                +'  '+line[4]+'  '+line[5]+'  '+line[6]+'  '+line[7]+'  '+
                line[8]+'  '+line[9]+'  '+line[10]+'  '+line[11]+'\n')
