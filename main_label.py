# -*- coding: UTF-8 -*-

import numpy as np

#nome = raw_input('Caminho ou So o nome do arquivo: ')
#savexd = raw_input('Digite onde salvar: ')
o = open('samples/labels.txt', 'r')
r = o.read()
#lines_skip = f.readlines()[1:]
o.close()

#r = r[:g] + r[(g+1):]
r = r.split('\n')

a = np.asarray(r)
#a[0].split(',')

i = 0
boo = []

for w in a:
	if w:
		boo.append([int(x) for x in a[i].split(',')])
	else:
		print "Empty in "+ str(i)
	i = i + 1

save_file = open('feature/labels.txt','w')
f = str(boo)
g = len(f)
f = f[1:g-1]
save_file.write(f)
save_file.close()

