import compair_service as cm
import cv2 as cv
import shutil, glob, gc

target = r'img_folder\target\\'                     # ocr folder
folder_backup = r'img_folder\folder_backup\\'       # backup
og_23ea = r'img_folder\og_23ea\\'                   # og_23ea
folder = r'img_folder\folder\\'                     # folder
folder_all = r'img_folder\all\\'                    # all_folder
file_test = r'img_folder\all\1090_2.jpg'            # 1090_2
crop_backup = r'img_folder\billet_crop_backup_2\\'

# folder_all = r'D:\Engineering\Work\Codinghub\compare-img\img_folder\all\\'
# folder_backup = r'D:\Engineering\Work\Codinghub\compare-img\img_folder\folder_backup\\'
# target = r'D:\Engineering\Work\Codinghub\compare-img\img_folder\target\\'
# og_23ea = r'D:\Engineering\Work\Codinghub\compare-img\img_folder\og_23ea\\'

# check = ''
while True:
    try:
        current = cm.lasted_file(folder_backup)
    except Exception as e:
        # print(f'Exception {e}')
        continue
    if check == current:
        continue
    elif check != current:
        print(f'current: {current}')
        cm.pare_10(current, folder_backup, target)
        check = current
    print(f'---------------------------------\n')

    # except KeyboardInterrupt:
    #     del current
    #     del check

# check = ''
# jpg_list = glob.glob(crop_backup + '*.jpg')

# for j in jpg_list:
#     try:
#         current = cm.lasted_file(folder_backup)
#     except Exception as e:
#         print(f'Excepton: {e}')
#         shutil.copy(j, folder_backup)
#         continue
#     # current = cm.lasted_file(folder_backup)
#     if check == current:
#         continue
#     elif check != current:
#         print(f'current: {current}')
#         cm.pare_10(current, folder_backup, target)
#         check = current
#     print(f'---------------------------------\n')
#     shutil.copy(j, folder_backup)

# cm.delete(target)

'''
งาน
- แก้ duplicate บน Ciracore
- ตามเอกสารเตรียมรับงานต่อจาก senior (Yamaha)
'''
