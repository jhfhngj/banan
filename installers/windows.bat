@echo off
REM Make sure to have Git and Python installed!
echo "Installing Banan..."
echo "Cloning Banan Git repo..."
git clone https://github.com/jhfhngj/banan.git
echo "Cloned Banan Git repo."
cd banan
echo "Creating extractor script..."
echo "import json^
import sys^
import os^
^
def extract_banapkg_to_file(banapkg_path: str, output_file: str):^
    # Check the BANAPKG exists^
    if not os.path.isfile(banapkg_path):^
        print(f"Error: {banapkg_path} does not exist.")^
        return^
^
    # Read the .banapkg^
    with open(banapkg_path, "r") as f:^
        try:^
            pkg = json.load(f)^
        except json.JSONDecodeError as e:^
            print(f"Error parsing {banapkg_path}: {e}")^
            return^
^
    # Extract the code^
    code = pkg.get("code", "")^
    ^
    # Write code to the output file^
    with open(output_file, "w") as f:^
        f.write(code)^
^
    print(f"Extracted {banapkg_path} → {output_file}")^
^
# CLI usage^
if __name__ == "__main__":^
    if len(sys.argv) != 3:^
        print("Usage: python extract_banapkg.py <file.banapkg> <output_file>")^
    else:^
        extract_banapkg_to_file(sys.argv[1], sys.argv[2])" > extractor.py
echo "Running extractor script..."
py extractor.py bananclient.banapkg banan.py
echo "Deleting temporary files..."
copy banan.py ..
cd ..
rmdir /s /q banan
echo "Banan has successfully been installed."