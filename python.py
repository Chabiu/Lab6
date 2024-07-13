import sys
import json
import yaml
import xml.etree.ElementTree as ET


def parse_arguments():
    if len(sys.argv) != 3:
        print("Usage: program.exe pathFile1.x pathFile2.y")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    return input_file, output_file


def load_json(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except Exception as e:
        print(f"Error reading JSON file: {e}")
        sys.exit(1)


def save_json(data, file_path):
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
        print(f"Data successfully saved to {file_path}")
    except Exception as e:
        print(f"Error writing JSON file: {e}")
        sys.exit(1)


def load_yaml(file_path):
    try:
        with open(file_path, 'r') as file:
            data = yaml.safe_load(file)
        return data
    except Exception as e:
        print(f"Error reading YAML file: {e}")
        sys.exit(1)


def save_yaml(data, file_path):
    try:
        with open(file_path, 'w') as file:
            yaml.safe_dump(data, file, default_flow_style=False)
        print(f"Data successfully saved to {file_path}")
    except Exception as e:
        print(f"Error writing YAML file: {e}")
        sys.exit(1)


def load_xml(file_path):
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        data = {root.tag: xml_to_dict(root)}
        return data
    except Exception as e:
        print(f"Error reading XML file: {e}")
        sys.exit(1)


def save_xml(data, file_path):
    try:
        root_tag = next(iter(data))
        root = dict_to_xml(root_tag, data[root_tag])
        tree = ET.ElementTree(root)
        tree.write(file_path, encoding='utf-8', xml_declaration=True)
        print(f"Data successfully saved to {file_path}")
    except Exception as e:
        print(f"Error writing XML file: {e}")
        sys.exit(1)


def xml_to_dict(element):
    data = {}
    if element.text and element.text.strip():
        data[element.tag] = element.text.strip()
    for child in element:
        data[child.tag] = xml_to_dict(child)
    return data


def dict_to_xml(tag, data):
    element = ET.Element(tag)
    if isinstance(data, dict):
        for key, val in data.items():
            child = dict_to_xml(key, val)
            element.append(child)
    else:
        element.text = str(data)
    return element


if __name__ == "__main__":
    input_file, output_file = parse_arguments()

    if input_file.endswith('.json'):
        data = load_json(input_file)
    elif input_file.endswith('.yml') or input_file.endswith('.yaml'):
        data = load_yaml(input_file)
    elif input_file.endswith('.xml'):
        data = load_xml(input_file)
    else:
        print("Unsupported input file format")
        sys.exit(1)

    if output_file.endswith('.json'):
        save_json(data, output_file)
    elif output_file.endswith('.yml') or output_file.endswith('.yaml'):
        save_yaml(data, output_file)
    elif output_file.endswith('.xml'):
        save_xml(data, output_file)
    else:
        print("Unsupported output file format")
        sys.exit(1)
