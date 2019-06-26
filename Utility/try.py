# import os 

# f = open("../Resources/ronec.conllu", 'r', encoding='utf8').read()

# preprocessed = ""

# for line in f.split('\n'):
#     if len (line) > 1 and '#' not in line:
#         tab = line.split('\t')
#         if len(tab) >= 10:
#             preprocessed += tab[1] + '\t' + tab[10][2:] + '\n'

# print(preprocessed)

h = open(r"D:\Anul_3\Lic\Resources\ORGANIZATION.txt", "r", encoding="utf8").read()
# print(h)
to_write = ""
for line in h.split('\n'):
    # to_write += line.split('\t')[0] + '\n'
    to_write += line.split('\t')[0] + '\n'

h = open(r"D:\Anul_3\Lic\Resources\ORGANIZATION.txt", "w", encoding="utf8").write(to_write)