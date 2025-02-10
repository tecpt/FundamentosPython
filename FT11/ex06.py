

n_mes = int(input("Introduza o número do mês:\n"))

meses = {1:"Janeiro",2:"Fevereiro",3:"Março",4:"Abril",5:"Maio",6:"Junho",7:"Julho",8:"Agosto",
         9:"Setembro", 10:"Outubro",11:"Novembro",12:"Dezembro"}

def calendario(a1):
    v = meses[a1]
    return v
          
          
a = calendario(n_mes)

print(a)