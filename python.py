import sys
import json

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


if __name__ == "__main__":
        input_file, output_file = parse_arguments()
    if input_file.endswith('.json'):
        data = load_json(input_file)
        print(f"Loaded data: {data}")
    else:
        print("Input file is not a .json file")

