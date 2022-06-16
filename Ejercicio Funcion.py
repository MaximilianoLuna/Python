def Calcular_Iva(precio):
   precio_final = precio * 0.19
   return(precio_final)

def calcular_descuento(precio, descuento):
    precio_descuento = precio - descuento
    return precio_descuento

def calcular_imc(peso, estatura):
    imc = peso / (estatura * estatura)
    if(imc < 18.5):
        return "bajo peso"
    if(imc >= 18.5 and imc < 24.9):
        return "adecuado"
    if(imc >= 25 and imc < 29.9):
        return "sobrepeso"
    if(imc >= 30 and imc < 34.9):
        return "Obecidad G1"
    if(imc >= 35 and imc < 39.9):
        return "Obecidad G2"
    if(imc >= 40):
        return "Obecidad G3"

ciclo=0
selec=0
print("elija su opcion")
print("1-calcular iva\n2-descuento\n3-calcular_imc")
selec= int(input())
while ciclo<=3:
    if selec==1:
        print("ingrese el precio del producto")
        precio= int(input())
        res=Calcular_Iva(precio)
        print(res)
        break
    if selec==2:
        print("ingrese el precio")
        precio= int(input())
        print("ingrese el descuento del producto")
        descuento= int(input())
        res=calcular_descuento(precio,descuento)
        print(f"el precio final es: {res}")
        break
    if selec==3:
        print("ingrese su peso")
        peso= int(input())
        print("ingrese su altura")
        estatura= int(input())
        res=calcular_imc(peso,estatura)
        print(f"el precio final es: {calcular_imc}")
        break
