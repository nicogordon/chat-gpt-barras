from codigo_de_barras import calculate_digit_verifier
import barcode
from barcode.writer import ImageWriter
from PIL import Image, ImageDraw, ImageFont

cuit = input("Ingrese el CUIT: ")
tipo_comprobante = input("Ingrese el Tipo de Comprobante: ")
punto_venta = input("Ingrese el Punto de Venta: ")
cai = input("Ingrese el CAI: ")
year = input("Ingrese el año: ")
month = input("Ingrese el mes: ")
day = input("Ingrese el día: ")

digito_verificador = calculate_digit_verifier(cuit, tipo_comprobante, punto_venta, cai, year, month, day)

codigo_barras = cuit + tipo_comprobante + punto_venta + cai + year + month + day

codigo_barras_final = codigo_barras + str(digito_verificador)

# Generar código de barras
from PIL import Image, ImageDraw

# Definir constantes
ANCHO_DELGADO = 1
ANCHO_GRUESO = 3
MARGEN = 22
ALTURA_BARRAS = 55
DIM_X = 2  # Ancho en píxeles de la barra delgada (ajustar según se desee)

# Definir dimensiones de la imagen
ancho_total = len(codigo_barras_final) * (DIM_X + ANCHO_DELGADO) + MARGEN * 2
dimensiones = (ancho_total, ALTURA_BARRAS + 20)

# Crear imagen en blanco
imagen = Image.new("RGB", dimensiones, color="white")
dibujo = ImageDraw.Draw(imagen)

# Dibujar barras
posicion_x = MARGEN
for digito in codigo_barras_final:
    if digito == "1":
        dibujo.rectangle(
            [(posicion_x, 0), (posicion_x + DIM_X - 1, ALTURA_BARRAS - 1)],
            fill="black",
        )
    posicion_x += DIM_X + ANCHO_DELGADO

# Dibujar número debajo del código de barras
posicion_x = MARGEN
posicion_y = ALTURA_BARRAS + 5
for digito in codigo_barras_final:
    dibujo.text((posicion_x, posicion_y), digito, fill="black")
    posicion_x += DIM_X + ANCHO_DELGADO

# Guardar imagen
imagen.save("codigo_barras.png")
print("El código de barras es:", codigo_barras_final)
