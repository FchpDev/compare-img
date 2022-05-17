from cv2 import FileNode_TYPE_MASK
import imagehash, os, glob, shutil
from PIL import Image

def delete(folder):
    count = 0
    file_list = glob.glob(folder + '*.*')
    for file_ in file_list:
        if os.path.exists(file_):
            if file_.rsplit('\\', 1)[-1] == r'mockup.jpg':
                continue
            os.remove(file_)
            print(file_)
            count = count + 1
    print(f'total delete: {count}')

# get lasted file
def lasted_file(folder):
    type = r'\*jpg'
    file_ = glob.glob(folder + type)
    #print(file_)
    lasted = max(file_, key=os.path.getctime)
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

def stack(folder):
    folder_list = os.listdir(folder)
    temp = []
    count = 0
    for file_ in folder_list:
        temp.append(file_)
        count = count + 1
    #print(f'temp_array: {temp[-10:-1]}')
    #print(f'count: {count}')
    temp2 = []
    for j in temp:
        t = folder + j
        temp2.append(t)
        img = Image.open(t)
        # print(f'temp: {temp2}')
        # print(f'img: {img}\n')
    print(f'temp: {temp2}')
    return temp2[-10: 0]

def pare_10(file_, bf, tg):
    flag = False
    img1 = Image.open(file_)
    # print(f'img: {img1}')
    hash1 = imagehash.dhash(img1, hash_size = 8)
    print(f'hash: {hash1}')

    # 10 lastest file in directory
    #last_10 = stack(bf)   
    last_10 = glob.glob(bf + '*.jpg')[-11:-1]
    # last_10 = glob.glob(bf + '*.jpg')
    print(f'last_10: {last_10}')
    for image in last_10:
        # print(f'image: {image}')
        # load image 2 and hash
        img = Image.open(image)
        # print(f'img2: {img}')
        hash2 = imagehash.dhash(img, hash_size = 8)
        print(f'hash2: {hash2}')

        # hashdiff
        hashdif = hash1 - hash2
        print(f'hashdiff {hashdif}')
        # check hashdiff
        if hashdif > 10:
            flag = True
        elif file_ != image:
            flag = False
            break

    # copy if isn't Dupplicate
    if flag == True:
        print('no')
        shutil.copy(file_, tg)
    elif flag == False:
        # file_name = file_.rsplit('\\', 1)[-1]
        print(len(last_10))
        if len(last_10) != 0:
            os.remove(file_)
        print('Dupplicate')

# def get_10(folder):
#     get = glob.glob(folder + '*.jpg')
#     get10 = get[-10:0]
#     return get10

# folder_all = r'img_folder\all\\'
# list_file = glob.glob(folder_all + '*.jpg')
# print(list_file)
# print('\n')
# print(f'last 10 files: {list_file[-11:-1]}')

# print(get_10(folder_all))











































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