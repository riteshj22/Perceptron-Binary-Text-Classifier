import sys, random, os

dir_path = sys.argv[1]

# Dictionary to store distinct words from training dataset.

vocabulary = {}
filenames = {}

# Total number of Ham and Spam files.

ham_files = 0
spam_files = 0

# ******************************************** Traversing the given directory *****************************************#
low = str.lower
# combine = os.path.join
# for root, sub, files in os.walk(dir_path):
#
#     parent = os.path.basename(root)
#     if low(parent) == "ham":
#         for name in files:
#             # ham_files += 1
#             if name.endswith(".txt"):
#                 path = combine(root, name)
#                 # path = root + "\\" + name
#                 filenames[path] = [-1, []]
#
#     if low(parent) == "spam":
#         for name in files:
#             # spam_files += 1
#             if name.endswith(".txt"):
#                 path = combine(root, name)
#                 # path = root + "\\" + name
#                 filenames[path] = [1, []]
#
# statinfo = os.stat('per_learn.py')
# print(statinfo)


list1 = []


def listdir_fullpath(d, value):

    l = [os.path.join(d, f) for f in os.listdir(d)]
    for l1 in l:
        filenames[l1] = [value, {}]
    list1.extend(l)

for root, sub, files in os.walk(dir_path):

    parent = os.path.basename(root)
    if low(parent) == "ham":
        listdir_fullpath(root,-1)
    elif low(parent) == "spam":
        listdir_fullpath(root, 1)
        # list1.extend(f2)

random.shuffle(list1)
# print(len(list1))

bias = 0
u = 0
for key in list1:
    # print(1)
    alpha = 0
    product = 0
    y = filenames[key][0]
    # print(y)
    file_ptr = open(key, "r", encoding="latin1")
    token_list = file_ptr.read().split()
    for token in token_list:

        if token not in filenames[key][1]:
            filenames[key][1][token] = [0, 1]
            # alpha += vocabulary[token]
        else:
            filenames[key][1][token][1] += 1
            # alpha += vocabulary[token]
    for token in filenames[key][1]:
        alpha += (filenames[key][1][token][0] * filenames[key][1][token][1])
    alpha += bias
    product = y * alpha
    if product <= 0:
        for token in filenames[key][1]:
            t = (y*filenames[key][1][token][1])
            # print(token, t)
            filenames[key][1][token][0] += t
        bias += y
    file_ptr.close()


l = 0
for i in range(1, 20):
    # print(i)
    random.shuffle(list1)
    for key in list1:
        alpha = 0
        product = 0
        y = filenames[key][0]
        # list1 = filenames[key][1]
        l += len(filenames[key][1])
        for token in filenames[key][1]:
            alpha += (filenames[key][1][token][0] * filenames[key][1][token][1])
        alpha += bias
        product = y * alpha
        if product <= 0:
            for token in filenames[key][1]:
                t = (y*filenames[key][1][token][1])
                filenames[key][1][token][0] += t
            bias += y


neg = 0
pos = 0
zero = 0
with open('per_model.txt', "w", encoding="latin1") as f:
    # str1 = ""
    # str1 = "\n".join(['%s %s' % (key, value) for (key, value) in vocabulary.items()])
    for file in list1:
        for key,value in filenames[file][1].items():
            str1 = ''
            str1 += str(key)
            str1 += " "

            str1 += str(value[0])
            f.write(str1 + '\n')
            # f.write(str1)
f.close()
