#Area de un triangulo

def areatriangulo(base, altura):
    return (base*altura)/2


def areacirculo(radio):
    return (3.14*radio)


baseTriangulo = int(input("Introduce la base del triángulo:"))
alturaTriangulo = int(input("Introduce la altura del triángulo:"))

print("El área del triángulo es ",areatriangulo(baseTriangulo,alturaTriangulo))

radioCirculo = int(input("Introduce el radio del círculo:"))

print("El área del círculo es ",areacirculo(radioCirculo))
