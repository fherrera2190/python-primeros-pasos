import xml.etree.ElementTree as ET
import json

# Parsear el archivo XML
tree = ET.parse("D:/archivo.xml")
root = tree.getroot()

# Función para convertir un elemento XML a un diccionario recursivamente
def xml_to_dict(element):
    # Convertir las etiquetas y los textos del elemento en un diccionario
    data = {element.tag: element.text.strip() if element.text else None}

    # Convertir los atributos del elemento en el diccionario
    if element.attrib:
        data["_attributes"] = element.attrib

    # Convertir los hijos del elemento en el diccionario
    for child in element:
        child_data = xml_to_dict(child)
        if child.tag in data:
            # Si ya existe una entrada con la misma etiqueta, convertirla en una lista
            if not isinstance(data[child.tag], list):
                data[child.tag] = [data[child.tag]]
            data[child.tag].append(child_data)
        else:
            data[child.tag] = child_data
    
    return data

# Convertir la raíz del XML a un diccionario
xml_dict = xml_to_dict(root)

# Función para convertir un diccionario en formato JSON
def convert_to_json(data):
    # Convertir el diccionario a formato JSON
    json_data = json.dumps(data, indent=4)
    return json_data

# Convertir el diccionario a formato JSON
json_data = convert_to_json(xml_dict)

# Imprimir el JSON resultante
print(json_data)
