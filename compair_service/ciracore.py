from PIL import Image
import imagehash, shutil, glob, os

# get lasted file
def lasted_file(folder):
    type = r'\*jpg'
    file_ = glob.glob(folder + type)
    #print(file_)
    lasted = max(file_, key=os.path.getctime)
    return lasted

# pair
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

# define folder
folder_backup = r'img_folder\folder_backup\\'
target = r'img_folder\target\\'

# run main
check = ''
while True:
    try:
        current = lasted_file(folder_backup)
    except Exception as e:
        # print(f'Exception {e}')
        continue
    if check == current:
        continue
    elif check != current:
        print(f'current: {current}')
        pare_10(current, folder_backup, target)
        check = current
    print(f'---------------------------------\n')