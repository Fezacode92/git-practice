def suma(a, b):
    """Returns the sum of two numbers."""
    return a + b
resultado = suma(3,4)
print(resultado * 2)

def miles_a_kilometers(miles):
    """Converts miles to kilometers."""
    return miles * 1.60934

kilometers = miles_a_kilometers(5)
print(kilometers)

def pounds_a_kilograms(pounds):
    """Converts pounds to kilograms."""
    return pounds * 0.453592
kilograms = pounds_a_kilograms(10)
print(kilograms)


def es_mayor_de_edad(edad):
    """Checks if a person is an adult (18 years or older)."""
    return edad >= 18
mayor_de_edad = es_mayor_de_edad(15)
print(mayor_de_edad)

persona = {"nombre": "Felix", "edad": 25, "ciudad": "Buenos Aires"}
print(persona["nombre"])
print(persona["edad"])
print(persona["ciudad"])

libro = {"titulo": "Crimen y Castigo", "autor": "Fyodor Dostoevsky", "año": 1866, "genero": "Novela"}
print(libro["titulo"])
print(libro["autor"])
print(libro["año"])
print(libro["genero"])