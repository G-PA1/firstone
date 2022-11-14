import csv as c
f = open('exp.csv','w')

c.writer(f).writerows([['id','name','p','c','m'],['1','rae','53','22','12'],['2','xi','33','45','50']])
f.close()

f = open('exp.csv')
print(f.read())
