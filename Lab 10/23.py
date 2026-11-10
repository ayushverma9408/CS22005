import xml.etree.ElementTree as ET

root = ET.Element("students")

s1 = ET.SubElement(root, "student")

n=int(input("Enter number of students: "))

for i in range(n):
    roll = input("Enter roll number: ")
    name = input("Enter name: ")
    dept = input("Enter department: ")

    s1 = ET.SubElement(root, "student")
    ET.SubElement(s1, "roll").text = roll
    ET.SubElement(s1, "name").text = name
    ET.SubElement(s1, "dept").text = dept 

for s in root.findall("student"):
    if s.find("roll").text == "102":
        s.find("name").text = "Rahul Kumar"
 
tree = ET.ElementTree(root)
ET.indent(tree, space="    ")
tree.write("students_updated.xml", encoding="utf-8",
           xml_declaration=True)

print("XML file created and updated.")
 
for s in root.findall("student"):
    print(s.find("roll").text,
          s.find("name").text,
          s.find("dept").text)