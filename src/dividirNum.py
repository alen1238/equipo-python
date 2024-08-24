def dividirNumero(a, b):
    if b == 0:
        return "Error: No se puede dividir por cero"
    else:
        resultado = a / b
        return f"La división de {a} y {b} es: {resultado}"
    
print(dividirNumero(9,3))

