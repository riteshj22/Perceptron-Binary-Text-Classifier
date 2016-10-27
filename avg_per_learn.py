import sys, random, os

dir_path = sys.argv[1]

# Dictionary to store distinct words from training dataset.

vocabulary = {}
filenames = {}

# Total number of Ham and Spam files.

ham_files = 0
spam_files = 0
weight = {}
avg_weights = {}

# ******************************************** Traversing the given directory *****************************************#
low = str.lower

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

random.shuffle(list1)

bias = 0
avg_bias = 0
counter = 1
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
        if token not in weight:
            weight[token] = 0
        if token not in avg_weights:
            avg_weights[token] = 0
        if token not in filenames[key][1]:
            filenames[key][1][token] = 1
        else:
            filenames[key][1][token] += 1
    for token in filenames[key][1]:
        alpha += (weight[token] * filenames[key][1][token])
    alpha += bias
    product = y * alpha
    if product <= 0:
        for token in filenames[key][1]:
            weight[token] += (y*filenames[key][1][token])
            avg_weights[token] += (y * filenames[key][1][token]*counter)
        bias += y
        avg_bias += (y * counter)
        counter += 1
    file_ptr.close()


l = 0
for i in range(1, 30):
    # print(i)
    random.shuffle(list1)
    for key in list1:
        alpha = 0
        product = 0
        y = filenames[key][0]
        for token in filenames[key][1]:
            alpha += (weight[token] * filenames[key][1][token])
        alpha += bias
        product = y * alpha
        if product <= 0:
            for token in filenames[key][1]:
                weight[token] += (y*filenames[key][1][token])
                avg_weights[token] += (y * filenames[key][1][token] * counter)
            bias += y
            avg_bias += (y * counter)
            counter += 1

inverse_counter_value = 1/counter
for token in avg_weights:
    avg_weights[token] = weight[token] - (avg_weights[token] * inverse_counter_value)
avg_bias = bias - (inverse_counter_value * avg_bias)


with open('per_model.txt', "w", encoding="latin1") as f:
    # str1 = ""
    # str1 = "\n".join(['%s %s' % (key, value) for (key, value) in vocabulary.items()])
    f.write(str(avg_bias))
    f.write("\n")
    for token, weight in avg_weights.items():
        str1 = ''
        str1 += str(token)
        str1 += " "
        str1 += str(weight)
        f.write(str1 + '\n')
f.close()
