
estadocivil = input("Introduza Estado Civil [S;C;D;V]\n-->")

match estadocivil:
        case "S":
           print("Solteiro")
        case "C":
           print("Casado")
        case "V":
            print("Viuvo")
        case "D":
            print("Divorciado")
        case _:
            print("Estado Civil inválido.")
       
  