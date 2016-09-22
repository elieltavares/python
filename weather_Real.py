import numpy as np

save_file = open('feature/feature.txt','r')
r = save_file.read()
save_file.close()
X = eval(r)
#X = np.array([[1, 85, 85, 2], [1, 80, 90, 1], [2, 83, 86, 2], [3, 70, 96, 2], [3, 68, 80, 2], [3, 65, 70, 1],[2, 64, 65, 1],[1, 72, 95, 2],[1, 69, 70, 2],[3, 75, 80, 2],[1, 75, 70, 1],[2, 72, 90, 1],[2, 81, 75, 2],[3, 71, 91, 1]])
#Y = np.array([2,2,1,1,1,2,1,2,1,1,1,1,1,2])
save_file1 = open('feature/labels.txt','r')
sr = save_file1.read()
Y = eval(sr)

from sklearn.naive_bayes import GaussianNB
clf = GaussianNB()
clf.fit(X, Y)

z1 = int(input('Digite 1 para sol, 2 para nublado e 3 para chuva: '))
z2 = int(input('Digite a temperatura em Fahrenheit: '))
z3 = int(input('Digite a Humidade: '))
z4 = int(input('Digite 1 para vento, 2 para sem vento: '))

z = str(z1) + ',' +str(z2) + ',' +  str(z3)+','+str(z4)
z = eval(z)

der = []
der.append(z)
der = [x for xs in der for x in xs]

result = clf.predict([der])

if result == [1]:
	print "Vai ter jogo"
else:
	print "Nao vai jogo"

print(result)










