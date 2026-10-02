import xml.etree.ElementTree as ET

def is_atlas(xml_text):
    return ET.fromstring(xml_text).tag == "atlas"

print(is_atlas("<atlas><beacon /></atlas>"))
