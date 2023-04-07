import random

karakterler ="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

karakterharf =int(input("Şifreniz Kaç Karakterli Olsun"))

password =""
for i in range(karakterharf):

    karakter =random.choice(karakterler)
    password +=karakter

print (password)
