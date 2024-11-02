import csv
import xml.etree.ElementTree as ET


# Read the CSV file and group ayas by sura
def read_csv(filename):
    suras = {}
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            sura_index = row['sura']
            aya_index = row['aya']
            text = row['translation']

            if sura_index not in suras:
                suras[sura_index] = []
            suras[sura_index].append((aya_index, text))
    return suras


# Convert the suras data to XML format
def create_xml(suras):
    root = ET.Element("quran")

    for sura_index, ayas in suras.items():
        sura_elem = ET.SubElement(root, "sura", index=sura_index, name="")

        for aya_index, text in ayas:
            ET.SubElement(sura_elem, "aya", index=aya_index, text=text)

    return root


# Write the XML data to file
def write_xml(root, filename):
    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)


# Main process
if __name__ == "__main__":
    csv_filename = "sinhalese_mahir.csv"  # Replace with your CSV file path
    xml_filename = "output.xml"  # Output XML file path

    suras = read_csv(csv_filename)
    root = create_xml(suras)
    write_xml(root, xml_filename)

    print(f"Data successfully converted to XML format and saved as {xml_filename}")
