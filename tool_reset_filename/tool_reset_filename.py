## import package
import os
from os import listdir
import shutil


## inital information
def input_information():
    ## global variable
    global target_folder_path,files,file_type,new_filename,new_filename_index_start
    
    ## folder path
    print('Current Path: ',os.getcwd())
    target_folder_path = input("Input folder path (default:'temp/') :")
    
    ## default: temp/
    if target_folder_path:
        files = listdir(target_folder_path)
        print('Current Files: ')
        print(files)
    else:
        target_folder_path = 'temp/'   
        files = listdir(target_folder_path)
        print('Current Files: ')
        print(files)
    
    ## get the file type
    try:
        file_type = files[0].split('.')[1]
        print('file_type: ', file_type)
    except IndexError:
        assert False, "No files in the folder"
    
    ## new file name and order
    new_filename = input("new file name: ")
    new_filename_index_start = input('new files name order you want to start from(default: 0): ')
    


## change the file name
def change_file_name():
    for i,file in enumerate(files):
        ## rename to a temp name (avoiding the duplicate name error)
        temp = os.path.join(target_folder_path,'_temp_'+str(i)+'.'+file_type)
        
        ## tell the user if the folder can't operate without permission
        try:
            os.rename(target_folder_path+'\\'+file, temp)
        except:
            print('Suggestion: put the files in anothor folder with another path')
            assert False, "Permission Problem: you don't have authority to operate this folder"
            
        
        ##rename to your new filename
        os.rename(temp, target_folder_path+'\\'+new_filename+str(i + int(new_filename_index_start))+'.'+file_type)


def automatic():
    ## automatic(help you copy the files to the folder you want)
    automatic = input('Automatic help?(yes/no) :')
    
    if automatic == 'yes':
        automatic_folder_path = input('new folder path: ')
        
        ## copy and move or just move to new folder 
        method = input('you want to cut or copy the files to the new folder(copy/cut) :')
        
        ## copy the files to new folder
        new_files = os.listdir(target_folder_path)
        try:
            for file in new_files:    
                if method == 'copy':
                    shutil.copy(target_folder_path+'\\'+file, automatic_folder_path)
                elif method == 'cut':
                    shutil.move(target_folder_path+'\\'+file, automatic_folder_path)
                else:
                    print('sorry you can only type copy or cut')
        except:
            assert False, "Permission Problem: you don't have authority to operate this folder"
        
    elif automatic == 'no':
        print('Thanks, wish you have a nice day')
        
    else:
        print('sorry you can only type yes or no')



if __name__ == '__main__':
    input_information()
    change_file_name()
    automatic()
 