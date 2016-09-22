import numpy as np


o = open('samples/feature.txt', 'r')
r = o.read()
#lines_skip = f.readlines()[1:]
o.close()
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


save_file = open('feature/feature.txt','w')
fvalue = str(boo)
save_file.write(fvalue)
save_file.close()

