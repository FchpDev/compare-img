from PIL import Image
import imagehash, shutil, glob, os, cfg
#last_image = payload['last_image'] 
#print(f"last image: {last_image}")
#import random
#payload['last_image'] = "king"+str(random.random())
# temp = ['C:', 'darknet_billet_ocr', 'CiraCore', 'billet', 'Duplicate', 'folder_backup', '1653535139059_000.jpg']

factory_number = payload['factory_number']

#################################

def collect_path(path):
    i = 0
    ret = ''
    for p in path:
        if i > 0:
            ret = ret + '\\\\' + p
        i += 1
    return 'C:' + ret

# get lasted file
def lasted_file(folder):
    type = r'\*jpg'
    file_ = glob.glob(folder + type)
    #print(file_)
    lasted = max(file_, key=os.path.getctime)
    return lasted

# pair
def pare_10(file_, bf, tg):
    fix_hash = 7
    flag = False
    img1 = Image.open(file_)
    #print(f'img: {img1}')
    hash1 = imagehash.dhash(img1, hash_size = 8)
    print(f'hash: {hash1}')

    # 10 lastest file in directory
    last_10 = glob.glob(bf + '*.jpg')[-11:-1]
    print(f'last_10: {last_10}')
    for image in last_10:
        #print(f'image: {image}')
        # load image 2 and hash
        img = Image.open(image)
        #print(f'img2: {img}')
        hash2 = imagehash.dhash(img, hash_size = 8)
        print(f'hash2: {hash2}')

        # hashdiff
        hashdif = hash1 - hash2
        print(f'hashdiff {hashdif}')
        # check hashdiff
        if hashdif > fix_hash:
            flag = True
        elif file_ != image:
            flag = False
            break

    # copy if isn't Dupplicate
    if flag == True:
        print('no')
        shutil.copy(file_, tg)
    elif flag == False:
        #file_name = file_.rsplit('\\', 1)[-1]
        # print(len(last_10))
        # if len(last_10) != 0:
            # os.remove(file_)
        print('Dupplicate')

# define folder
folder_backup = cfg.list_of_backup_image_path[factory_number]
print(f'folder_backup: {folder_backup}')
target = cfg.list_of_image_path[factory_number]
print(f'target: {target}')

# run main
temp = payload['last_image_factory1']
check = collect_path(temp)
print(f'check: {check}')
# check = ''
current = ''

try:
    current = lasted_file(folder_backup)
    last_10 = glob.glob(folder_backup + '*.jpg')[-11:-1]
    last_10_size = len(last_10)
    print(f'last_10(size): {last_10_size}')
    #print(f'last_10: {last_10}')
    # if len(last_10) == 1:
    #     size_tg = len(glob.glob(target + '*.jpg'))
    #     if size_tg == 0:
    #         shutil.copy(current, target)
    #         pass
    if current:
        if check == current:
            print('folder backup is\'n update')
            pass
        elif check != current and current != '':
            print(f'current: {current}')
            pare_10(current, folder_backup, target)
            payload['last_image_factory1'] = current.replace('\\', '\\\\')
            #check = current
            print(f'---------------------------------\n')
    elif not current:
            print('Program doesn\'t have current file')
            pass
except Exception as e:
    print(f'Exception {e}')
    pass
