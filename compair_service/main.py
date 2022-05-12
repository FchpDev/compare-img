import compair_service as cm
import cv2 as cv
import shutil, glob

target = r'img_folder\target\\'                     # ocr folder
folder_backup = r'img_folder\folder_backup\\'       # backup
og_23ea = r'img_folder\og_23ea\\'                   # og_23ea
folder = r'img_folder\folder\\'                     # folder
folder_all = r'img_folder\all\\'                    # all_folder
file_test = r'img_folder\all\1090_2.jpg'            # 1090_2

# while True:
#     if check == cm.lasted_file(folder_backup):
#         continue
#     elif check != cm.lasted_file(folder_backup):
#         file_now = cm.lasted_file(folder_backup)
#         print('file_now: ', file_now.rsplit('\\', 1)[-1])
#         cm.dhash_image_while(file_now, folder_backup, target)
#         check = file_now

folder_list = glob.glob(folder_all + '*.jpg')
check = ''

# for img in folder_list:
#     if check == cm.lasted_file(folder_backup):
#             continue
#     elif check != cm.lasted_file(folder_backup):
#         file_now = cm.lasted_file(folder_backup)
#         print('file_now: ', file_now.rsplit('\\', 1)[-1])
#         cm.dhash_image_while(file_now, folder_backup, target)
#         check = file_now
#     print(f'image: {img}')
#     shutil.copy(img, folder_backup)

# cm.pare_10(file_test, folder_backup, target)
# for img in folder_list:
#     if check == cm.lasted_file(folder_backup):
#             continue
#     elif check != cm.lasted_file(folder_backup):
#         file_now = cm.lasted_file(folder_backup)
#         print('file_now: ', file_now.rsplit('\\', 1)[-1])
#         cm.pare_10(file_now, folder_backup, target)
#         check = file_now
#     print(f'image: {img}')
#     shutil.copy(img, folder_backup)

# while True:
#     current = cm.lasted_file(folder_backup)
#     if check == current:
#         continue
#     elif check != current:
#         print(f'current: {current}')
#         cm.pare_10(current, folder_backup, target)
#         check = current
#     print(f'---------------------------------\n')

jpg_list = glob.glob(folder_all + '*.jpg')
for j in jpg_list:
    current = cm.lasted_file(folder_backup)
    if check == current:
        continue
    elif check != current:
        print(f'current: {current}')
        cm.pare_10(current, folder_backup, target)
        check = current
    print(f'---------------------------------\n')
    shutil.copy(j, folder_backup)

# cm.delete(target)