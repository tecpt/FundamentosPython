Txt="""Python é uma linguagem de programação
de alto nível, interpretada de script, imperativa, orientada a objetos,
funcional, de tipagem dinâmica e forte."""

#alinea a)

Txt=Txt.upper()
print(Txt)



#alinea b)

palavra=input("introduza a palavra a pesquisar:").upper()

if palavra in Txt:
    print("A palavra", palavra, "está no texto")
else:
    print("A palavra", palavra, "não está no texto")


#alinea c)

print("No texto tem ", Txt.count("O"), "letras 'O'")


#alinea d)

print(Txt.replace("P", "_"))


