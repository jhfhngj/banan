# Banan installer
import platform,gc,shutil
import subprocess,os,sys

p=platform.platform(True, True)
if p.startswith("Windows"):
    p = "win" # 4
else:
    p = "lin" # Win4Lin

python = "py" if p == "win" else "python3"

path = "/usr/bin/" if p == "lin" else "C:\\Program Files\\"
delete = "rm" if p == "lin" else "del"
code = subprocess.run(["git", "version"]).returncode
if code != 0:
    print("Install git bro")
    sys.exit(1)
cd = "-c" if p == "lin" else "-n"
code2 = subprocess.run(["ping", "1.1.1.1", cd, "3"]).returncode
if code != 0:
    print("Connect to the internet bro")
del subprocess # os better
del code, code2
gc.collect()
slash = "/" if p == "lin" else "\\"
print("Welcome to the Banan installer. By answering these questions I will start installing Banan for you.")
print("Number one. Do you want Banan to be installed in PATH, or as a local file? You need to run as root/Administrator if you want to copy to PATH. (1/2)")
a = input("").lower()
while a not in "12":
    print("Try again.")
    a = input("").lower()
a = int(a)
print("Number two. Would you like a minimal installation of Banan (Banan without ClamAV) or a full installation of Banan? Option 2 is recommended for safety. (1/2)")
b = input("").lower()
while b not in "12":
    print("Try again.")
    b = input("").lower()
b = int(b)
print("Number three. Would you also like to install the Banan PKGr or not? (Y/N)")
c = input("").lower()
while c not in "yn":
    print("Try again.")
    c = input("").lower()
print("Thank you for your service. Now installing Banan.")
os.system("git clone https://github.com/jhfhngj/banan.git")
print("Cloned Banan repository")
with open("extractor.py","w", encoding='utf-8') as f:
    f.write(r"""#!/usr/bin/env python3
import json
import sys
import os

def extract_banapkg_to_file(banapkg_path, output_file):
    if not os.path.isfile(banapkg_path):
        print(f'Error: {banapkg_path} does not exist.')
        return

    with open(banapkg_path, 'r') as f:
        pkg = json.load(f)

    code = pkg.get('code', '')

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(code)

    print(f'Extracted {banapkg_path} -> {output_file}')

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: python extractor.py <file.banapkg> <output_file>')
    else:
        extract_banapkg_to_file(sys.argv[1], sys.argv[2])
""")
print("Created extractor script.")
os.system(f"{python} extractor.py .{slash}banan{slash}bananclient.banapkg banani")
ban = """"""
if b == 1:
    print("Modifying Banan to be minimal...")
    with open("banani") as f:
        bna = f.readlines()
    bna[13:25] = ["\treturn True"]
    ban = "".join(bna)
    print(ban)
    with open("banani", "w") as f:
        f.write(ban)
    print("Modified.")
if c == "y":
    os.system(f"{python} extractor.py .{slash}banan{slash}bananpkgr.banapkg bananpkgr")
    print("Extracted Banan PKGr.")
os.system("rm -rf banan" if p == "lin" else "rmdir /s /q banan")
print("Finalizing...")
if a == 1:
    shutil.copy("banani", f"{path}banan")
    if c == "y":
        shutil.copy("bananpkgr", f"{path}bananpkgr")
else:
    shutil.copy("banani", "banan.py")
    os.system(f"{delete} banani")
    if c == "y":
        shutil.copy("bananpkgr", "bananpkgr.py")
        os.system(f"{delete} bananpkgr")
os.system(f"{delete} extractor.py")

print("Banan has been installed.")