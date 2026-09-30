import xml.etree.ElementTree as ET

def tag_name(xml_text):
    return ET.fromstring(xml_text).tag

print(tag_name("<lamp />"))
