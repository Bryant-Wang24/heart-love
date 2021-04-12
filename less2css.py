import os

LESSC = "./node_modules/.bin/lessc"
if os.name == 'nt':  # 奇葩windows
    LESSC = r"node_modules\.bin\lessc"


if __name__ == "__main__":
    exclude = set(['node_modules', 'miniprogram_npm'])

    for root, directories, files in os.walk("./src"):
        directories[:] = [d for d in directories if d not in exclude]
        for filename in files:
            filepath = os.path.join(root, filename)
            if filename.endswith(".less"):
                print(f"LESS => CSS: {filepath}")
                inFile = filepath
                outFile = filepath.replace(".less", ".css")
                os.system(f'{LESSC} {inFile} {outFile}')

    print("\ndone.")
