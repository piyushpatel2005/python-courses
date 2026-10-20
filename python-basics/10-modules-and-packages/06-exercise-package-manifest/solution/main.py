import xml.etree.ElementTree as ET

def is_invoice(xml_text):
    return ET.fromstring(xml_text).tag == "invoice"

print(is_invoice("<invoice><line /></invoice>"))
