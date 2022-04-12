import os

pathInput = os.path.abspath(input('Enter the path for the directory to search '))

for folder, subFolders, files in os.walk(pathInput):
    for file in files:
        if not os.path.islink(file):
            
            file = os.path.join(folder, file)
            try:
                if int(os.path.getsize(file)) > 100000000:
                    print('File {fileName} located at {path}'.format(fileName=file, path=folder))
            except FileNotFoundError:
                print('FileNotFoundError: {}'.format(file))
