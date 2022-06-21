import compair_service as cm
import shutil, glob

target = r'img_folder\target\\'                     # ocr folder
folder_backup = r'img_folder\folder_backup\\'       # backup
og_23ea = r'img_folder\og_23ea\\'                   # og_23ea
folder = r'img_folder\folder\\'                     # folder
folder_all = r'img_folder\folder_all\\'             # all_folder
duplicate = r'img_folder\billet_dup_test\\'         # Duplicate
file_test = r'img_folder\all\1090_2.jpg'            # 1090_2

# while True:
#     try:
#         current = cm.lasted_file(folder_backup)
#     except:
#         continue   
#     if check == current:
#         continue
#     elif check != current:
#         print(f'current: {current}')
#         cm.pare_10(current, folder_backup, target)
#         check = current
#     print(f'---------------------------------\n')

check = ''
jpg_list = glob.glob(duplicate + '*.jpg')
txt = open('pare.txt', 'w')
r = 0
# for j in jpg_list:
#     try:
#         current = cm.lasted_file(folder_backup)
#     except Exception as e:
#         print(f'Exception: {e}')
#         shutil.copy(j, folder_backup)
#         continue
#     if check == current:
#         continue
#     elif check != current:
#         print(f'current: {current}')
#         cm.pare_10(current, folder_backup, target, txt)
#         txt.write(f'round: {r}\n')
#         check = current
#         r += 1
#     print('-------------------------------------------\n')
#     shutil.copy(j, folder_backup)

# cm.delete(target)
# cm.delete(folder_backup)
# cm.rename()