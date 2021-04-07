f = open("anneal.csv", 'r')

a_list = []
while True:
    line = f.readline().rstrip()
    if not line:
        break
    line = line.split(',')
    a_list.append(line)
a_list = a_list[1:-3]

for i in range(len(a_list)):
    for j in range(len(a_list[0])):
        if a_list[i][j][0] == "'":
            a_list[i][j] = str(a_list[i][j][1:-1])

#4-1
columns = ['family','product-type','steel','carbon','hardness','temper_rolling','condition','formability','strength','non-ageing','surface-finish','surface-quality','enamelability','bc','bf','bt','bw/me','bl','m','chrom','phos','cbond','marvi','exptl','ferro','corr','blue/bright/varn/clean','lustre','jurofm','s','p','shape','thick','width','len','oil','bore','packing','class']
col1, col2 = input('input two columns(attribute) : ').split()
idx1, idx2 = columns.index(col1), columns.index(col2)

col_list = []
col1_list = []
col2_list = []
for temp in a_list:
    col1_list.append(temp[idx1])
    col2_list.append(temp[idx2])
col_list.append(col1_list)
col_list.append(col2_list)

print(col_list)
f.close()