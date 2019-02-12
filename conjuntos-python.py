##PERTINÊNCIA##
a = {1, 2, 3, 4}
print("conjunto A: ",a)
b = {3, 4, 5, 6}
print("conjunto B: ",b)
print("1 pertence a A: ", 1 in a)
print("5 pertence a A: ", 5 in a)

##CONTINÊNCIA##
set1 = {5, 6, 7}
set2 = {4, 'a', 9, 5, 6, 7}
if(set1.issubset(set2)):
    print('set1 está contida em set2')
else:
    print('set1 não está contida em set2')

##SUBCONJUNTO##
x = ([1,4,5,6,4,3,5,7,8,2,3])
y = set([1,2,3])
print(y.issubset(x))

##IGUALDADE##
d = {1, 2, 3, 4}
e = {3, 4, 5, 6}
if d == e:
    print ("d é igual a e")
else:
    print("d não é igual a e")


