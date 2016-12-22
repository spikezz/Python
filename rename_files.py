import os

def rename_files():
    
    #从文件夹取的文件
    file_list=os.listdir(r"C:\Users\Asgard\AppData\Local\Programs\Python\Python35-32\prank\prank")
    print(file_list)
    saved_path=os.getcwd()
    print("Directory:")
    print(saved_path)
    os.chdir(r"C:\Users\Asgard\AppData\Local\Programs\Python\Python35-32\prank\prank")
    #分别对每个文件进行重命名
    for file_name in file_list:
        print("old file name:")
        print(file_name)
        print("new file name:")
        print(file_name.translate(str.maketrans("","","0123456789")))
        os.rename(file_name,file_name.translate(str.maketrans("","","0123456789")))
    os.chdir(saved_path)
rename_files()
