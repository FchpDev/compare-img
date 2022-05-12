from logging import lastResort
import imagehash, os, glob, shutil
from PIL import Image

target = r'D:\Engineering\Work\Codinghub\5-3-2022\billet_crop_backup_\compair_service\target\\'                    # ocr folder
folder_backup = r'D:\Engineering\Work\Codinghub\5-3-2022\billet_crop_backup_\compair_service\folder_backup\\'      # backup
img_folder = r'D:\Engineering\Work\Codinghub\5-3-2022\billet_crop_backup_\compair_service\img_folder\\'            # img folder
folder = r'D:\Engineering\Work\Codinghub\5-3-2022\billet_crop_backup_\compair_service\folder\\'                    # folder

def delete(folder):
    count = 0
    file_list = glob.glob(folder + '*.*')
    for file_ in file_list:
        if os.path.exists(file_):
            os.remove(file_)
            count = count + 1
    print(f'total delete: {count}')

#delete(target)

# get lasted file
def lasted_file(folder):
    type = r'\*jpg'
    file = glob.glob(folder + type)
    lasted = max(file, key=os.path.getctime)
    return lasted

def dhash_image_while(file_, folder, target):
    flag = False
    # open image1 and hash
    img = Image.open(file_)
    hash1 = imagehash.dhash(img, hash_size=8)

    # split specific file name
    file_name = file_.rsplit('\\', 1)[-1]

    # set folder that you want to check
    img_list = glob.glob(folder + '*.jpg')

    # check image in folder
    for image in img_list:
        img2 = Image.open(image)
        hash2 = imagehash.dhash(img2, hash_size=8)
        # if hashdiff > 18(is not duplicate img) copy to target folder 
        if hash1 - hash2 > 18:
            flag = True
        # else (is duplicate img) copy to folder_backup
        elif image != file_:
            flag = False
            break

    # if img duplicate will go in if true
    if flag == True:
        print('isnt dupplicate')
        shutil.copy(file_, target)
    elif flag == False:
        pass
        print('Flag: False')
        # shutil.copy(file_, folder_backup)

#dhash_image_while(file_, folder, target)
# print('lasted_file: ', lasted_file(folder))
# dhash_image_while(lasted_file(folder), folder, target)

check = '' # check lasted file

# main run
while True:
    if check == lasted_file(folder):
        continue
    elif check != lasted_file(folder):
        file_now = lasted_file(folder)
        print('file_now: ', file_now.rsplit('\\', 1)[-1])
        dhash_image_while(file_now, folder, target)
        check = file_now
















































'''
def dhash_image(file_, folder, target):
    flag = False
    # open image1 and hash
    img = Image.open(file_)
    hash1 = imagehash.dhash(img, hash_size=8)

    # set folder
    img_list = glob.glob(folder + '*.jpg')

    #check img in folder
    for image in img_list:
        img2 = Image.open(image)
        hash2 = imagehash.dhash(img2, hash_size=8)
        # if duplicate
        if hash1 - hash2 > 18:
            flag = True
        else:
            flag = False
            break
    if flag == True:
        print('isn\'t duplication' )
        shutil.copy(file_, target)
    elif flag == False:
        print('Duplicate')
'''