import os
import zipfile

print(os.getcwd)
os.chdir(os.path.abspath('C:\\Users\\User\\Downloads'))
print(os.getcwd)
with zipfile.ZipFile('main.zip','r') as zip:
    zip.extractall('main')
arr=[]
for cuurent_dir, dir, files in os.walk('main'):
    if str(files).count('.py'):
        arr.append(cuurent_dir)
arr.sort()
with open ('Упражнение_3.txt','w') as file:
    file.write('\n'.join(arr))
    file.close