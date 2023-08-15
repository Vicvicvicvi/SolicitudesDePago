import requests

# Configuración de la API
api_key = "TU_API_KEY"
api_url = "https://api.ejemplo.com/pagos"

# Datos del pago
datos_pago = {
    "monto": 100.0,
    "moneda": "MXN",
    "descripcion": "Pago de prueba",
    "metodo_pago": "tarjeta",
    "datos_tarjeta": {
        "numero": "4242424242424242",
        "expiracion_mes": "12",
        "expiracion_anio": "2025",
        "cvc": "123"
    }
}

# Realizar la solicitud de pago
response = requests.post(api_url, json=datos_pago, headers={"Authorization": f"Bearer {api_key}"})

# Verificar el resultado
if response.status_code == 200:
    print("Pago realizado con éxito")
else:
    print("Error al realizar el pago:", response.text)
