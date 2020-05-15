###########################################################################
##          PROGRAMA PARA SACAR MEDIA DE NOTAS CON PORCENTAJES           ##
##          18/02/2019 - VERSION. 1.3                                    ##
##          Jose Manuel Martin                                           ##
###########################################################################
# BIBLIOTECAS
import msvcrt                                                                                                                                                                                      
# TITULO
def banner():
    print("\n\n")
    print("    ","  _          _              _   _   _          _   _         _ ___             _  _  ___      ")
    print("    "," /   /\  |  /  | | |   /\  | \ / \ |_)  /\    | \ |_   |\ | / \ |  /\    |\/| |_ | \  |   /\   ")
    print("    "," \_ /--\ |_ \_ |_| |_ /--\ |_/ \_/ | \ /--\   |_/ |_   | \| \_/ | /--\   |  | |_ |_/ _|_ /--\  ")
    print("    ","-"*95)
    print("    ","-"*95)
    print("\n\n")
    return
banner()
#INSTRUCCIONES
print ("    -Este programa realizara la media aritmetica entre la evaluación continua y la prueba de sintesis.\n\n")
# VALOR EVALUACIÓN CONTINUA
print("     VALORES NOTA EVALUACIÓN CONTINUA:\n     "+"-"*33)
notacont= str(input("    -Introduce la nota de la evaluación continua:  "))
porcientocont=int(input("    -Introduce el porcentaje del valor de la nota de la evaluación continua:  "))
notacont_comas=notacont.replace(",",".")
notacont=float(notacont_comas)
# NOTA DE CORTE
print("\n")
print("     VALORES NOTA PRUEBA DE SINTESIS:\n     "+"-"*32)
minexam=str(input("    -¿Cual es la nota de corte en la prueba de sintesis que te permite hacer media con la evaluación continua?:  "))
minexam_comas=minexam.replace(",",".")
minexam=float(minexam_comas)
# VALOR PRUEBA DE SINTESIS
notaexam=str(input("    -Introduce la nota de la prueba de sintesis:  "))
notaexam_comas=notaexam.replace(",",".")
notaexam=float(notaexam_comas)
porcientoexam=(100-porcientocont)
# CALCULO DEL VALOR DE LA NOTA DE EVALUACIÓN CONTINUA
valorcontinua=(porcientocont/100)
mediacontinua=(valorcontinua*(notacont))
# CALCULO DEL VALOR DE LA NOTA DE EXAMEN
valorexam=(porcientoexam/100)
mediaexam=(valorexam*(notaexam))
#VALOR FINAL
notafinal=(float(mediacontinua+mediaexam))
# DECICIÓN FINAL
if(minexam<=notaexam):
    print("\n\n"+"   ","*"*131)
    print("\n","    Como obtuviste una nota favorable para realizar media entre la evaluación continua y la prueba de sintesis, tengo que informarte.\n"+"     Que tu nota final es: ", notafinal)
else:
    print("\n\n"+"   ","*"*131)    
    print("\n","    Lo lamento pero la nota de las prueba de sintesis no permite hacer media con la evaluación continua")
    print("\n","    Por lo que su nota final es: ",notaexam)
# FINALIZACIÓN DE PROGRAMA
print("\n\n\n","    Pulse una tecla para salir")
msvcrt.getch()
