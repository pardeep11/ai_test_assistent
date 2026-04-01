import xml.etree.ElementTree as ET

def extract_failures(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    failures = []

    for test in root.iter('test'):
        for msg in test.iter('msg'):
            if msg.attrib.get('level') == 'FAIL':
                failures.append({
                    "test_name": test.attrib.get('name'),
                    "error": msg.text
                })

    return failures
