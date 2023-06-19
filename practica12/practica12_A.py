import xml.etree.ElementTree as ET
def arxiuXML():
    p = ET.Element('students')
    c0 = ET.SubElement(p, 'student')
    c0.set('becado', 'si')
    n0 = ET.SubElement(c0, 'name')
    n0.text = "Paco"
    s0 = ET.SubElement(c0, 'surname')
    s0.text = "Sanchez"
    e0 = ET.SubElement(c0, 'email')
    e0.text = "paco@gmail.com"
    d0 = ET.SubElement(c0, 'dni')
    d0.text = "67983412J"
    c1 = ET.SubElement(p, 'student')
    c1.set('becado', 'no')
    n1 = ET.SubElement(c1, 'name')
    n1.text = "Pepe"
    s1 = ET.SubElement(c1, 'surname')
    s1.text = "Viyuela"
    e1 = ET.SubElement(c1, 'email')
    e1.text = "pepe@gmail.com"
    d1 = ET.SubElement(c1, 'dni')
    d1.text = "98234726D"
    c2 = ET.SubElement(p, 'student')
    c2.set('becado', 'si')
    n2 = ET.SubElement(c2, 'name')
    n2.text = "Roc"
    s2 = ET.SubElement(c2, 'surname')
    s2.text = "Bigas"
    e2 = ET.SubElement(c2, 'email')
    e2.text = "roc@gmail.com"
    d2 = ET.SubElement(c2, 'dni')
    d2.text = "43123434K"
    c3 = ET.SubElement(p, 'student')
    c3.set('becado', 'no')
    n3 = ET.SubElement(c3, 'name')
    n3.text = "Tese"
    s3 = ET.SubElement(c3, 'surname')
    s3.text = "Orlando"
    e3 = ET.SubElement(c3, 'email')
    e3.text = "tese@gnail.com"
    d3 = ET.SubElement(c3, 'dni')
    d3.text = "34124312L"
    c4 = ET.SubElement(p, 'student')
    c4.set('becado', 'si')
    n4 = ET.SubElement(c4, 'name')
    n4.text = "Jhamel"
    s4 = ET.SubElement(c4, 'surname')
    s4.text = "Funes"
    e4 = ET.SubElement(c4, 'email')
    e4.text = "jhamel@gmail.com"
    d4 = ET.SubElement(c4, 'dni')
    d4.text = "54343213Z"

    ET.indent(p)
    ET.dump(p)

    tree = ET.ElementTree(p)
    tree.write("students.xml")
