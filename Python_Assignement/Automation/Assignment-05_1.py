import os, shutil

def moveFileType(folder): 
  for root, dirs, files in os.walk(folder): 
               for file in files: 
                   if file.endswith('.jpg'):
                    image_path=os.path.join(root,file)  # get the path location of each jpeg image.
                    print ('location: ',image_path) 
                    shutil.copy(image_path, '/home/anum/Documents/Stackoverflow questions')


moveFileType('/home/anum/Pictures/')
