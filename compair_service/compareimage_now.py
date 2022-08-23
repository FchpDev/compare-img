from multiprocessing.reduction import duplicate
import imagehash
from PIL import Image
import glob, os, shutil

from numpy import diff

#ทดสอบเพิ่มให้หน่อยว่าค่าที่ควรนำมาใช้ควรเป็นตัวเลขความห่าง(hashdiff)เท่าไรดี

count = 0

# hash img
def image2hash(filename):
    image_file = Image.open(filename)
    # print(type(image_file))
    phash1 = imagehash.phash(image_file, hash_size = 8)
    return phash1

# hash and write to txt file
def hash2txt(folder):
    #os.remove('result.txt')
    file = open('result.txt', 'w')
    for img in glob.glob(folder + '*.jpg'):
        # check img
        # print(img)
        # hash img
        hash = image2hash(img)
        # write value to txt file
        file.write(img + ': ' + str(hash) + '\n') 
        #print(type(hash))
        #print(hash)

# pair 2 img
def pair(image, image2):
    # open img
    img_file1 = Image.open(image)
    img_file2 = Image.open(image2)
    # hash img
    hash1 = imagehash.phash(img_file1, hash_size = 8)
    hash2 = imagehash.phash(img_file2, hash_size = 8)
    # pair img and return
    return hash2 - hash1

def sel_one(file_, folder):
    img1 = Image.open(file_)
    file = open('result.txt', 'w')
    print(f"origin: {file_} #")
    print('img1: ', img1)
    hash1 = imagehash.phash(img1, hash_size = 8)
    print('hash1: ', hash1)
    global count
    for img in glob.glob(folder + '*.jpg'):
        img2 = Image.open(img)
        print(f"compare with: {img} *")

        print('img2: ', img2)
        hash2 = imagehash.phash(img2, hash_size = 8)
        print('hash2: ', hash2)
        hashdiff = hash1 - hash2

        if file_ == img:
            continue
        if hashdiff < 8:
            os.remove(img)
            print('remove: ', img, "!!!")
            print('hashdiff: {}'.format(hash1 - hash2))
            file.write('remove: ' + str(img) + '\n' + str(hashdiff) + '\n')
            count = count + 1
        else:
            pass
            # print('pass: ', file_, ' : ', img)
            # print('hashdiff: {}'.format(hash1 - hash2))

def d_sel_one(file_, folder):
    img1 = Image.open(file_)
    file = open('result_delete_d.txt', 'w')
    print(f"origin: {file_} #")
    # print('img1: ', img1)
    hash1 = imagehash.dhash(img1, hash_size = 8)
    # print('hash1: ', hash1)
    global count
    for img in glob.glob(folder + '*.jpg'):
        img2 = Image.open(img)
        # print('img2: ', img2)
        print(f"compare with: {img} *")
        hash2 = imagehash.dhash(img2, hash_size = 8)
        # print('hash2: ', hash2)
        hashdiff = hash1 - hash2

        if file_ == img:
            continue
        if hashdiff < 18:
            os.remove(img)
            print('remove: ', img, "!!!")
            print('hashdiff: {}'.format(hash1 - hash2))
            file.write('remove: ' + str(img) + '\n' + str(hashdiff) + '\n')
            count = count + 1
        else:
            pass
            # print('pass: ', file_, ' : ', img)
            # print('hashdiff: {}'.format(hash1 - hash2))

def loop_sel_one(folder):
    print(f"############### start ##################")
    jpg_lists = glob.glob(folder + "*.jpg")
    for j in jpg_lists:
        #file_name = j.rsplit('\\', 1)[-1]
        #name_only = file_name.rsplit('.', 1)[0]
        # print(file_name + name_only)
        # print(name_only)
        if os.path.exists(j):
            file_ = j
            sel_one(folder, file_)
    print('count delete: ', count)
    print(len(jpg_lists))

def loop_dsel_one(folder):
    print(f"############### start ##################")
    jpg_lists = glob.glob(folder + "*.jpg")
    for j in jpg_lists:
        #file_name = j.rsplit('\\', 1)[-1]
        #name_only = file_name.rsplit('.', 1)[0]
        # print(file_name + name_only)
        # print(name_only)
        if os.path.exists(j):
            file_ = j
            d_sel_one(file_, folder)
    print('count delete: ', count)
    print(len(jpg_lists))

def autopair2txt(folder):   # phash
    file = open('result_pair.txt', 'w')
    file1 = open('result_under_10.txt', 'w')
    jpg_list = glob.glob(folder + '*.jpg')
    for image in jpg_list:
        img = Image.open(image)
        hash1 = imagehash.dhash(img, hash_size = 8)
        file.write('---------------------------------------------------' + '\n')
        file1.write('---------------------------------------------------' + '\n')
        for image2 in jpg_list:
            img2 = Image.open(image2)
            hash2 = imagehash.dhash(img2, hash_size = 8)
            hashdiff = hash1 - hash2
            file.write(image.rsplit('\\', 1)[-1] + ' : ' + image2.rsplit('\\', 1)[-1] + ' = ' + str(hashdiff) + '\n')
            if hashdiff < 10:
                file1.write(image.rsplit('\\', 1)[-1] + ' : ' + image2.rsplit('\\', 1)[-1] + ' = ' + str(hashdiff) + '\n')

def d_autopair2txt(folder):
    diff = 4
    up = 0
    down = 0
    # print(folder)
    # folder_name = folder.split('\\', 1)[1]
    # folder_name = folder_name.replace('test\\', '')
    # folder_name = folder_name.replace('\\', '')
    # print(f'folder_name: {folder_name}')
    # file = open(f'result_dpair_{folder_name}.txt', 'w')
    # file1 = open(f'result_dpair_{folder_name}_under_{diff}.txt', 'w')
    file = open(f'result_dpare.txt', 'a')
    file1 = open(f'result_dpare_under{diff}.txt','a')
    jpg_list = glob.glob(folder + '*.jpg')
    file.write(f'file_name: {folder}\n')
    file1.write(f'file_name: {folder}\n')
    for image in jpg_list:
        img = Image.open(image)
        hash1 = imagehash.dhash(img, hash_size = 8)
        # print(f'hash1: {hash1}')
        file.write('---------------------------------------------------' + '\n')
        file1.write('---------------------------------------------------' + '\n')
        for image2 in jpg_list:
            img2 = Image.open(image2)
            hash2 = imagehash.dhash(img2, hash_size = 8)
            # print(f'hash2: {hash2}')
            hashdiff = hash1 - hash2
            if hashdiff > diff:
                file.writelines(image.rsplit('\\', 1)[-1] + ' : ' + image2.rsplit('\\', 1)[-1] + ' = ' + str(hashdiff) + '\n')
                up = up + 1
            if hashdiff <= diff:
                file1.writelines(image.rsplit('\\', 1)[-1] + ' : ' + image2.rsplit('\\', 1)[-1] + ' = ' + str(hashdiff) + '\n')
                if hashdiff != 0:
                    file.writelines(image.rsplit('\\', 1)[-1] + ' : ' + image2.rsplit('\\', 1)[-1] + ' = ' + str(hashdiff) + ' ###' + '\n')
                    down = down + 1 
                    continue
                file.writelines(image.rsplit('\\', 1)[-1] + ' : ' + image2.rsplit('\\', 1)[-1] + ' = ' + str(hashdiff) + ' #' + '\n')
    file.write('----------------------------------------------------\n' + f'Up: {up}\n' + f'Down: {down}\n')
    print('done')

# delete all in folder
def delete(folder):
    count = 0
    jpg_list = glob.glob(folder + '*.jpg')
    for j in jpg_list:
        if os.path.exists(j):
            os.remove(j)
            print('remove: ' + j.rsplit('\\', 1)[-1])
            count = count + 1
    print(f'total delete: {count}')

# confirm = str(input('Confirmed(yes/no): '))
# if confirm == 'yes' or 'Yes' or 'YES':
#     delete(ocr)

hot_factory1 = r'img_folder\hot_billet_factory1\\'
hot = r'img_folder\hot\\'
duplicate = r'img_folder\billet_dup_test\\'
cold = r'img_folder\cold\\'
backup = r'img_folder\backup\\'

test = [r'img_folder\test\2292_7\\', r'img_folder\test\2293_10\\', r'img_folder\test\2294_6\\',
        r'img_folder\test\2294_8\\', r'img_folder\test\2294_15\\', r'img_folder\test\2294_17\\',
        r'img_folder\test\2295_5\\', r'img_folder\test\2295_6\\', r'img_folder\test\2296_10\\',
        r'img_folder\test\2296_12\\']


# d_autopair2txt(hot)
for i in test:
    print(f'round: {i}')
    d_autopair2txt(i)

























































'''
image1 = r'img\2181_1\2181_1_3.jpg'
image2 = r'img\2181_1\2181_1_2.jpg'
hash1 = image2hash(image1)
hash2 = image2hash(image2)

print('hash1: ', hash1, type(hash1))
print('hash2: ', hash2, type(hash2))
print('hashdiff = {}'.format(hash2 - hash1))
'''
'''
hash_dict = []
compare_result = []

for name in sorted(glob.glob('*.jpg')):
    hash_dict.append(image2hash(name))
    print(name)

for x in hash_dict:
    row = []
    for y in hash_dict:
        hashdif = x - y
        row.append(str(hashdif).zfill(2))
    compare_result.append(row)

for c in compare_result:
    print(c)
# if use sys import sys
#image1 = sys.argv[1]
#image2 = sys.argv[2]
'''
'''
# auto pair folder
def pair_auto(folder):
    i = 0
    count = 0
    for img in glob.glob(folder + '*.jpg'):
        if i == 0:
            img_file = Image.open(img)
            hash1 = imagehash.phash(img_file, hash_size = 8)
            i = i + 1
            print('hash1: ', hash1)
            print('round 1')
        else:
            img_file1 = Image.open(img)
            hash2 = imagehash.phash(img_file1, hash_size = 8)
            print('hash2:', hash2)
            if hash1 - hash2 < 14:
                print(img)
                os.remove(img)
                print('remove success')
                count = count + 1
            print('\n')
            print('hash1: ', hash1)
            print('hash2: ', hash2)
            hash1 = hash2
            print('replace success')
            print('\n')
            print('hash1: ', hash1)
            print('hash2: ', hash2)
            print('----------------------------------')
    print('Count: ', count)

def auto_pair(folder):
    i = 1
    j = 1
    count = 0
    file = open('result.txt', 'w')
    for img in glob.glob(folder + '*.jpg'):
        print('round: ', i)
        image1 = Image.open(img)
        print('image1: ', image1)
        hash1 = imagehash.phash(image1, hash_size = 8)
        print('hash1: ', hash1)
        for img1 in glob.glob(folder + '*.jpg'):
            if img == img1:
                continue
            print('round: ', i, ', ', j)
            image2 = Image.open(img1)
            print('image2: ', image2)
            hash2 = imagehash.phash(image2, hash_size = 8)
            print('hash2: ', hash2)
            hashdiff = hash1 - hash2
            if hashdiff < 10:
                os.remove(img1)
                print('remove success: ', img1)
                file.write('remove: ' + str(img) + '\n' + str(hashdiff) + '\n')
                j = j + 1
                count = count + 1
            else:
                print('pass')
                j = j + 1
        i = i + 1
    print('Delete: ', count)

def cp_from_temp(file_, og, target):
    # read img
    img = Image.open(file_)
    #print(img)
    # open txt file
    file = open('result_temp.txt', 'w')
    # hash img
    hash1 = imagehash.dhash(img, hash_size = 8)
    print('hash: ', hash)
    # list jpg file in folder
    jpg_list = glob.glob(og + '*.jpg')
    # count in global variable
    global count
    global temp
    # loop cheack duplicate img
    for image2 in jpg_list:
        # read img2
        img2 = Image.open(image2)
        # hash image2
        hash2 = imagehash.dhash(img2, hash_size=8)
        # hash diff
        hashdiff = hash1 - hash2
        # check Duplication image
        if hashdiff < 13:
            temp = []
            temp.append(image2)
        else:
                shutil.copy(image2, target)
                #shutil.copy(file_, target)
                print('copy: ' + image2.rsplit('\\', 1)[-1] + ' to ' + target)
                count = count + 1
    print('total copy: ', count)
    print('temp: ', temp)

def loop_cp_temp(folder, target):
    jpg_list = glob.glob(folder + '*.jpg')
    for j in jpg_list:
        # if os.path.exists(j):
        file_ = j
        cp_from_temp(file_, folder, target)
    print('len(target): ', len(target))
'''