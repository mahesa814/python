
print("maaf bu telat soalnya tidak tau tanggal telat nya,kirain pas masuk pelajaran ibu lagi , Maaf ya bu".center(50).upper())


#penugasan


print("*************".center(50))
print("PENUGASAN".center(50))

nilaiawal = 6
nilaiawal += 6
print("ini adalah hasil pengurangan : " , nilaiawal  )
print("*************".center(50))


#LOGIKA
print("************".center(50))
print("LOGIKA".center(50).upper())
x = 5

print(x > 3 and x < 10)

print("************".center(50))


# variable global

a = ['mahesa','ilham']
b = ['mahesa','ilham']
c = a
# IDENTITAS
print("******************".center(50))
print("IDENTITAS".center(50))
# is
print("IS".center(50))
print(a is c)
print(a is b)
print(a == b)
# is no
print("IS NOT".center(50))
print(a is not c)
print(a is not b)
print(a != b)
print("********************".center(50))



print("********************".center(50))
print("Keanggotaan".center(50).upper())
print("IN")
print("mahesa" in a)

print("IN NOT")
print("ilham" not in a)
print("********************".center(50))


print("********************".center(50))
print("BitWise".center(50).upper())

c = 5
d = 4

e = c << d
print(e)