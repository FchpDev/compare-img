from PIL import Image
import imagehash, shutil, glob, os, cfg
#last_image = payload['last_image'] 
#print(f"last image: {last_image}")
#import random
#payload['last_image'] = "king"+str(random.random())
# temp = ['C:', 'darknet_billet_ocr', 'CiraCore', 'billet', 'Duplicate', 'folder_backup', '1653535139059_000.jpg']

#################################

factory_number = 3

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

# delete
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


# pair
def pare_10(file_, bf, tg):
    fix_hashdif = 10
    flag = False
    img1 = Image.open(file_)
    #print(f'img: {img1}')
    hash1 = imagehash.dhash(img1, hash_size = 8)
    print(f'hash: {hash1}')

    # 10 lastest file in directory
    last_10 = glob.glob(bf + '*.jpg')[-11:-1]
    last_10_size = len(last_10)
    print(f'last_10(size): {last_10_size}')
    print(f'last_10: {last_10}')
    for image in last_10:
        #print(f'image: {image}')
        if len(last_10) == 1:
            shutil.copy(last_10[0], tg)
            break
        # load image 2 and hash
        img = Image.open(image)
        #print(f'img2: {img}')
        hash2 = imagehash.dhash(img, hash_size = 8)
        print(f'hash2: {hash2}')

        # hashdiff
        hashdif = hash1 - hash2
        print(f'hashdiff {hashdif}')
        # check hashdiff
        if hashdif > fix_hashdif:  # doesn't duplicate
            flag = True
        elif file_ != image: # duplicate
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

# run main
# temp = payload['last_image']
# check = collect_path(temp)
current = ''
check = ''

# define folder
folder_backup = cfg.list_of_backup_image_path[factory_number]
target = cfg.list_of_image_path[factory_number]
cold = r'D:\Project\CodingHub\tata\compare-img\img_folder\cold\\'
hot = r'D:\Project\CodingHub\tata\compare-img\img_folder\hot\\'

jpg_list = glob.glob(cold + '*.jpg')
while True:
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
            if check == current and check == last_10[0]:
                print('folder backup is\'n update')
                continue
            elif check != current and current != '':
                print(f'current: {current}')
                pare_10(current, folder_backup, target)
                # payload['last_image_factory3'] = current.replace('\\', '\\\\')
                check = current
                print(f'---------------------------------\n')
        elif not current:
                print('Program doesn\'t have current file')
                continue
    except Exception as e:
        print(f'Exception {e}')

# while True:
#     try:
#         current = lasted_file(folder_backup)
#         if current:
#             if check == current:
#                 print('folder backup is\'n update')
#                 pass
#             elif check != current and current != '':
#                 print(f'current: {current}')
#                 pare_10(current, folder_backup, target)
#                 # payload['last_image'] = current.replace('\\', '\\\\)
#                 check = current
#             print(f'---------------------------------\n')
#         if not current:
#             print('Program doesn\'t have current file')
#             pass
#     except Exception as e:
#         print(f'Exception {e}')
#         pass

# for j in jpg_list:
#     try:
#         current = lasted_file(folder_backup)
#         if current:
#             if check == current:
#                 print('folder backup isn\'t update')
#                 pass
#             elif check != current and current != '':
#                 print(f'current: {current}')
#                 pare_10(current, folder_backup, target)
#                 # payload['last_image'] = current.replace('\\', '\\\\)
#                 check = current
#             print(f'---------------------------------\n')
#         if not current:
#             print('Program doesn\'t have current file')
#             pass
#     except Exception as e:
#         print(f'Exception {e}')
#         pass
#     shutil.copy(j, folder_backup)
        

# delete(folder_backup)
# delete(target)