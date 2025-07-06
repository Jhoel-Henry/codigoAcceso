import random
class codigoAcceso:
    def Entrar (self):
        p_digito=random.randint(1,10)
        s_digito=random.randint(1,10)
        t_digito=random.randint(1,10)
        res= p_digito * s_digito + t_digito
        edad= (int)(input("Ingrese su edad para ingresar: "))
        if 25 >= edad > 17:
            res_user = int(input(f"¿Cuál es el resultado de la siguiente operación?: {p_digito} * {s_digito} + {t_digito} = "))
            if res_user == res :
                print("Acceso correcto! Iniciando sesion...")
            else:
                print("Acceso denegado")
        else:
            print("Acceso denegado ")
acceso = codigoAcceso()
acceso.Entrar()