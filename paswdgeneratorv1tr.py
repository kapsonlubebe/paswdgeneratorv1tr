import random
import string
mport colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
print(Fore.CYAN + Style.BRIGHT + "**************************")
print(Fore.RED+ Style.BRIGHT +"Şifre oluşturucusuna hoşgeldiniz...")

length = int(input(Fore.YELLOW + Style.BRIGHT + '\nŞifre uzunluğunu belirleyiniz :'))

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

all = lower + upper + num + symbols

temp = random.sample(all,length)

password = "".join(temp)

print(Fore.GREEN + Style.BRIGHT +"Yeni şifren : " , password)
print(Fore.CYAN + Style.BRIGHT +"\n**************************")
answer = input(Fore.MAGENTA + Style.BRIGHT +"-Yeni şifreni beğendin mi? 'E/h' :")

while answer == 'h':

  temp = random.sample(all,length)
  password = "".join(temp)
  print(Fore.CYAN + Style.BRIGHT +"\n**************************")
  print(Fore.GREEN + Style.BRIGHT +"Yeni şifren : " , password)
  answer = input(Fore.GREEN + Style.BRIGHT +"-Yeni şifreni beğendin mi? 'E/h' :")

  if answer == 'E' and answer == 'e':
    break

  elif answer != 'E' and answer != 'e' and answer != 'h':
    print(Fore.RED+ Style.BRIGHT +"\n**************************")
    answer = input(Fore.RED+ Style.BRIGHT +"Geçerli bir cevap giriniz : 'E/h'")
