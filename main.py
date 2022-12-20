from pathlib import Path
import json
from zipfile import ZipFile


def xmind_to_file(file_path: str | Path, output_file_path: str | Path) -> None:
    '''Parse .xmind file and extract to output_file_path'''
    with ZipFile(file_path) as xmind:
        for file in xmind.namelist():
            if file == "content.json":
                with open(file) as f:
                    with open(output_file_path, 'w') as coba:
                        byte = f.read()
                        dict = json.loads(byte)
                        json_data = json.dumps(
                            dict, separators=(',', ':'), ensure_ascii=False)
                        coba.write(json_data)


def main():
    pass


if __name__ == "__main__":
    main()
