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
print('input two columns(attribute) :')
col1, col2 = input().split()



col1_list = []
col2_list = []


f.close()