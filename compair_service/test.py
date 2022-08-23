import glob

folder = r'D:\Project\CodingHub\tata\Compare-img\img_folder\hi\\'
folder2 = r'img_folder\Test_result_for_continue_project\\'
files = glob.glob(folder + '*.jpg')

# print file to text
# print(f'files: {files}')

# with open('readme.txt', 'a') as text:
#     for f in files:
#         print(f'f: {f}')
#         text.writelines(f'{f}\n')


# folder name
name = folder2.split("\\")
print(f'name: {name}')