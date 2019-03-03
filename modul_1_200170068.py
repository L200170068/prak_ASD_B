#no.1

def cetakSiku(x):
    i=1
    while i<=x:
        print("*"*i)
        i+=1
cetakSiku(5)

#no.2

def gambarlahPesegiEmpat(a,b):
    i=1
    print("@"*b)
    while(i<a):
       print("@"+" "*(b-2)+"@")
       i+=1
    print("@"*b)
gambarlahPesegiEmpat(4,5)

#no.3a

def jumlahHurufVokal(x):
	vokal="AIUEOaiueo"
	jmlhuruf=len(x)
	jmlvokal=0
	for karakter in x:
		if karakter in vokal:
			jmlvokal+=1
	return (jmlhuruf, jmlvokal)
k=jumlahHurufVokal("Surakarta")
print(k)

#no.3b

def jumlahHurufVokal(x):
	vokal="AIUEOaiueo"
	jmlhuruf=len(x)
	jmlkonsonan=0
	for karakter in x:
		if karakter not in vokal:
			jmlkonsonan+=1
	return (jmlhuruf, jmlkonsonan)
k=jumlahHurufVokal("Surakarta")
print(k)

#no.4

def rerata(x):
	"""Hitung Rata Rata dari List"""
	jml=0
	banyak=0
	for angka in x:
		jml+=angka
		banyak+=1
	return jml/banyak
print(rerata([1,2,3,4,5]))
g = [3,4,5,4,3,4,5,2,2,10,11,23]
print(rerata(g))

#no.5

from math import sqrt as sq
def apakahPrima(n):
    n=int(n)
    assert n>=0
    primakecil=[2, 3, 5, 7, 11]
    bukanprima=[0, 1, 4, 6, 8, 9, 10]
    if n in primakecil:
        return True
    elif n in bukanprima:
        return False
    else:
        for i in range(2,int(sq(n))+1):
            if(n%i==0):
                return False
    return True
print(apakahPrima(17))
print(apakahPrima(97))
print(apakahPrima(123))

#no.6

def cetakBilanganPrima():
    prima=list()
    for i in range(2,100):
        a = True
        for iter in prima:
            if(i%iter==0):
                a=False
                break
        if(a):
            print(i)
            prima.append(i)
cetakBilanganPrima()

#no.7

def faktorPrima(n):
    prima=list()
    for i in range(2,n):
        a = True
        for iter in prima:
            if(i%iter==0):
                a=False
                break
        if a and n%i==0:
            prima.append(i)
    return prima
print(faktorPrima(10))
print(faktorPrima(120))
print(faktorPrima(19))

#no.8

def apakahTerkandung(a,b):
    return a in b
h = 'do'
k = 'Indonesia tanah air beta'
print(apakahTerkandung(h,k))
print(apakahTerkandung('pusaka',k))

#no.9

def iterasi():
    for i in range(1,100):
        if (i%3)!=0 and (i%5)!=0:
            print(i)
        else:
            if (i%15)==0:
                print("pyton UMS")
            elif (i%3)==0:
                print("python")
            elif (i%5)==0:
                print("UMS")
iterasi()

#no.10

def selesaikanABC(a,b,c):
    a=float(a)
    b=float(b)
    c=float(c)
    D=(b**2)-(4*a*c)
    if D<0:
        return "Determinannya negatif. Persamaan tidak mempunyai akar real"
    return  "Determinannya positif"
print(selesaikanABC(1,2,3))

#no.11

def apakahKabisat(a):
    if(a%400==0):
        return True
    if(a%100==0):
        return False
    if(a%4==0):
        return True
    return False
print(apakahKabisat(2016))

#no.12

import random
def permainan():
    a=random.randrange(0, 100)
    while(True):
        b=int(input("masukan angka: "))
        if(b>a):
            print("terlalu besar, coba lagi")
        elif(b<a):
            print("terlalu kecil, coba lagi")
        else:
            print("benar")
            break
permainan()

#no.13

def katakan(a):
    x={"0":"","1":"Se","2":"Dua ","3":"Tiga ","4":"Empat ","5":"Lima ","6":"Enam ","7":"Tujuh ","8":"Delapan ","9":"Sembilan "}
    y={-1:"",-2:"puluh ",-3:"ratus ",-4:"ribu ",-5:"puluh ",6:"ratus ",7:"juta ",8:"puluhjuta "}
    b=str(a)
    c=""
    i=-1
    while i>= -len(b):
        c=x[b[i]]+y[i]+c
        i-=1
    return c
print(katakan(123))

#no.14

def formatRupiah(a):
    b=str(a)
    c=""
    i = -1
    while i>= -len(b):
        if((i+1)%3==0 and (i+1)!=0):
            c="."+c
        c=b[i]+c
        i-=1
    return "Rp "+c
print(formatRupiah(1500))
print(formatRupiah(2560000))
