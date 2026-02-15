@echo off

echo Installing Banan...
echo Cloning Banan Git repo...
git clone https://github.com/jhfhngj/banan.git 2>nul
echo Cloned Banan Git repo.

cd banan

echo Creating extractor script...

(
echo import json
echo import sys
echo import os
echo.
echo def extract_banapkg_to_file^(banapkg_path, output_file^):
echo     if not os.path.isfile^(banapkg_path^):
echo         print^("Error: {} does not exist.".format^(banapkg_path^)^)
echo         return
echo.
echo     with open^(banapkg_path, "r"^) as f:
echo         pkg = json.load^(f^)
echo.
echo     code = pkg.get^("code", ""^)
echo.
echo     with open^(output_file, "w"^) as f:
echo         f.write^(code^)
echo.
echo     print^("Extracted {} -> {}".format^(banapkg_path, output_file^)^)
echo.
echo if __name__ == "__main__":
echo     if len^(sys.argv^) != 3:
echo         print^("Usage: python extractor.py ^<file.banapkg^> ^<output_file^>"^)
echo     else:
echo         extract_banapkg_to_file^(sys.argv[1], sys.argv[2]^)
) > extractor.py

echo Running extractor script...
py extractor.py bananclient.banapkg banan.py
echo Extractor script ran successfully.

echo Finishing up...
echo Copying banan.py to ..
copy banan.py ..
cd ..
echo Copied banan.py to ..
echo Cleaning up banan folder...
rmdir /s /q banan
echo Cleaned up banan folder.

echo Banan has successfully been installed.
