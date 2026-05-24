headers = {
    "Content-Type": "application/json"
}

# Creamos la función que recibe el nombre y devuelve el diccionario modificado
def get_user_body(first_name):
    current_body = {
        "firstName": first_name,  # Aquí usamos la variable que recibe la función
        "phone": "+11234567890",
        "address": "123 Elm Street, Hilltop"
    }
    return current_body

product_ids = {
    "ids": [1, 2, 3]
}
