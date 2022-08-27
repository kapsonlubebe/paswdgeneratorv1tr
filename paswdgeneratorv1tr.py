import random
import string

print("Şifre oluşturucusuna hoşgeldiniz...")

length = int(input('\nŞifre uzunluğunu belirleyiniz :'))

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

all = lower + upper + num + symbols

temp = random.sample(all,length)

password = "".join(temp)

print("Yeni şifren : " , password)
print("\n**************************")
answer = input("-Yeni şifreni beğendin mi? 'E/h' :")

while answer == 'h':
  
  temp = random.sample(all,length)
  password = "".join(temp)
  print("\n**************************")
  print("Yeni şifren : " , password)
  answer = input("-Yeni şifreni beğendin mi? 'E/h' :")
  
  if answer == 'E' and answer == 'e':
    break
  
  elif answer != 'E' and answer != 'e' and answer != 'h':
    print("\n**************************")
    answer = input("Geçerli bir cevap giriniz : 'E/h'")

