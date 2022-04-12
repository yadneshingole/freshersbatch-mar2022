
import os,shutil,re
def gaps(folder, prefix):
    folder = os.path.abspath(folder)
    os.chdir(folder)
    file_regex = re.compile(r'^%s00(\d).txt$'%prefix)
    number = 1
    for folder, subfolder, files in os.walk(folder):
        for file in files:
            oldname = os.path.basename(file)
            match_obj = file_regex.search(file)
            no = match_obj.group(1)
            no = int(no)
            if no == number:
                number +=1
            else:
                no = number
                newname = prefix + "00" + str(no) + '.txt'
                print(f'Changing {oldname} to {newname}')
                shutil.move(oldname,newname)
gaps("C:\\Users\\yaingole\\OneDrive - Capgemini\\Desktop\\randomfolder",'spam')
