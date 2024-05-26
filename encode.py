import chardet

def detect_encoding(row):
    # Convertir la cadena a bytes
    byte_data = ''.join(row).encode()
    # Detectar la codificación
    result = chardet.detect(byte_data)
    return result['encoding']
# Ejemplo de uso
data = ['NÃºmero de perfil de selecciÃ³n:', '00000000000000149494', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']

source_encoding = detect_encoding(data)
print("Codificación detectada:", source_encoding)
