def loop_forever():
    f = open ("D:/Anul_3/Lic/stanford/train/dummy-romanian-corpus.tsv", 'r', encoding='utf8')

    data = f.read()
    lines = data.split("\n")
    f.close()

    # print(lines[672].split("\t"))
    to_write = ""
    for idx in range(0, len(lines)):
        # print(len(lines[idx].split('\t')))
        if len(lines[idx].split('\t')) == 1:
            lines[idx] += '\t'
        if lines[idx].split("\t")[1] == '':
            to_write += lines[idx] + lines[idx-1].split("\t")[1] + '\n'
        else: 
            to_write += lines[idx] + '\n'
            # lines[idx] += "\t" + lines[idx-1].split("\t") [1]

    g = open ("D:/Anul_3/Lic/stanford/train/dummy-romanian-corpus.tsv", 'w', encoding='utf8')
    g.write(to_write)

for i in range(0, 500):
    loop_forever()
