num=int(input("insira um ano:\n ->"))

if (num % 4 == 0 and num % 100 != 0) or num % 400== 0:
    print("o ano é bissexto")
else:
    print("o ano não é bissexto")