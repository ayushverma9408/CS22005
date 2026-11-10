import xml.etree.ElementTree as ET

tree = ET.parse("22.xml")
root = tree.getroot()

for s in root.findall("student"):
    roll = s.find("roll").text
    name = s.find("name").text
    dept = s.find("dept").text

    print("Roll:", roll)
    print("Name:", name)
    print("Department:", dept)
    print()