def calculate_digit_verifier(cuit, tipo_comprobante, punto_venta, cai, year, month, day):
    """
    Calcula el dígito verificador del módulo 10 para un código de barras AFIP.
    Los parámetros son:
    cuit -- el CUIT del emisor del comprobante
    tipo_comprobante -- el tipo de comprobante (ejemplo: 001 para factura A)
    punto_venta -- el número de punto de venta
    cai -- el número de CAI (Código de Autorización de Impresión)
    year -- el año de emisión del comprobante (en formato YYYY)
    month -- el mes de emisión del comprobante (en formato MM)
    day -- el día de emisión del comprobante (en formato DD)
    """
    codigo = f"{cuit}{tipo_comprobante}{punto_venta}{cai}{year}{month}{day}"
    suma_impares = sum([int(x) for x in codigo[0::2]])
    suma_pares = sum([int(x) for x in codigo[1::2]])
    suma_total = suma_impares * 3 + suma_pares
    digito_verificador = 10 - suma_total % 10
    if digito_verificador == 10:
        digito_verificador = 0
    return digito_verificador
