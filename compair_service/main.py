import compair_service as cm
import shutil, glob

# img_folder
target = r'img_folder\result\target\\'                      # ocr folder
folder_backup = r'img_folder\result\folder_backup\\'        # backup
og_23ea = r'img_folder\og_23ea\\'                           # og_23ea
folder = r'img_folder\folder\\'                             # folder
folder_all = r'img_folder\folder_all\\'                     # all_folder
duplicate = r'img_folder\billet_dup_test\\'                 # Duplicate
file_test = r'img_folder\all\1090_2.jpg'                    # 1090_2
hot = r'img_folder\hot\\'                                   # hot billet

# from AnyDesk
cold_backup = r'img_folder\from_anyDesk\cold\backup\\'
cold8_backup = r'img_folder\from_anyDesk\cold_hashdif-8\backup\\'

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
jpg_list = glob.glob(cold8_backup + '*.jpg')
txt = open('compare_service.txt', 'w')
r = 0
for j in jpg_list:
    try:
        current = cm.lasted_file(folder_backup)
    except Exception as e:
        print(f'Exception: {e}')
        shutil.copy(j, folder_backup)
        shutil.copy(j, target)
        continue
    if check == current:
        continue
    elif check != current:
        txt.write(f'round: {r}\n')
        print(f'current: {current}')
        cm.pare_10(current, folder_backup, target, txt)
        check = current
        r += 1
    print('-------------------------------------------\n')
    shutil.copy(j, folder_backup)

# cm.delete(target)
# cm.delete(folder_backup)
# cm.rename()