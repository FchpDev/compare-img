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

def pare_10(file_, bf, tg, txt):
    flag = False
    img1 = Image.open(file_)
    print(f'img: {img1}')
    hash1 = imagehash.dhash(img1, hash_size = 8)
    print(f'hash: {hash1}')

    # 10 lastest file in directory
    last_10 = glob.glob(bf + '*.jpg')
    print(f'last_10: {last_10}')
    txt.write(f'last_10: {last_10}\n')
    for image in last_10:
        print(f'image: {image}')
        # load image 2 and hash
        img = Image.open(image)
        print(f'img2: {img}')
        hash2 = imagehash.dhash(img, hash_size = 8)
        print(f'hash2: {hash2}')
        
        # hashdiff
        hashdif = hash1 - hash2
        
        file_name1 = file_.rsplit('\\', 1)[-1]
        file_name2 = image.rsplit('\\', 1)[-1]
        txt.write(f'{file_name1} : {file_name2} ==> {hashdif}\n')
        
        # check hashdiff
        if hashdif > 13:
            flag = True
        elif file_ == image:
            flag = True
            break
        elif file_ != image:
            flag = False
            break

    # copy if isn't Dupplicate
    if flag == True:
        print('no')
        shutil.copy(file_, tg)
    elif flag == False:
        print('Dupplicate')
    txt.write('-------------------------------------------------------------' + '\n')

def rename(folder):
    file_list = glob.glob(folder + '*.jpg')
    name = 1
    for file_ in file_list:
        os.rename(file_,folder + str(name) + '.jpg')
        name += 1

duplicate = r'img_folder\billet_dup_test\\'
cold = r'img_folder\cold\\'
rename(cold)














































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