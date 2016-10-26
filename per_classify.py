import sys
import os, random

ham_files = 0
spam_files = 0



ham_predicted = 0
spam_predicted = 0


#  Count of correctly identified documents i.e spam/ham

ham_predicted_correct = 0
spam_predicted_correct = 0


dev_dir = sys.argv[1]

# Dictionary to store distinct words from training dataset.

model = {}
d1 = {}

#  *************************************** reading the model file ******************************************************
file_name = sys.argv[2]

fptr = open("per_model.txt", "r", encoding="latin1")
data = fptr.read().splitlines()
for record in data:
    content = record.split()
    model[content[0]] = int(content[1])
fptr.close()

# ***************************************** Stop Words Filter **********************************************************
# stop_words = []
# stop_ptr = open("stop_words.txt", "r")
# words = stop_ptr.read().splitlines()
# for word in words:
#     stop_words.append(word)


# *********************************** Classifying the documents as spam/ham ********************************************


f1 = open(file_name, "w", encoding="latin1")
bias = 0
y = 0
list1 = []
filenames = {}

def listdir_fullpath(d, value):

    l = [os.path.join(d, f) for f in os.listdir(d)]
    for l1 in l:
        filenames[l1] = [value, {}]
    list1.extend(l)

low = os.path.basename

for root, sub, files in os.walk(dev_dir):

    parent = os.path.basename(root)
    if low(parent) == "ham":
        listdir_fullpath(root,-1)
    elif low(parent) == "spam":
        listdir_fullpath(root, 1)
        # list1.extend(f2)

# random.shuffle(list1)

for key in list1:

    y = filenames[key][0]

    alpha = 0
    file_ptr = open(key, "r", encoding="latin1")
    token_list = file_ptr.read().split()

    for token in token_list:
        if token not in filenames[key][1]:
            filenames[key][1][token] = 1
        else:
            filenames[key][1][token] += 1
    # print(filenames[key][1])
    # print(alpha)
    for token in filenames[key][1]:
        if token in model.keys():
            # print(model[token], filenames[key][1][token])
            alpha += (model[token] * filenames[key][1][token])

    alpha += bias
    # if y == -1:
    #     print(alpha)
    if alpha > 0:
        # print("spam")
        # spam += 1
        str1 = "spam " + key
        f1.write(str1 + "\n")
        spam_predicted += 1
        if y == 1:
            spam_predicted_correct += 1
    if alpha <= 0:
        # print("ham")
        # ham += 1
        # str1 = "ham " + str(os.path.join(root, name))
        str1 = "ham " + key
        ham_predicted += 1
        f1.write(str1 + "\n")
        if y == -1:
            ham_predicted_correct += 1
    # else:
    #     str1 = "ritesh_spam " + str(os.path.join(root, name))
    #     f1.write(str1 + "\n")

    if y == -1:
        ham_files += 1

    if y == 1:
        spam_files += 1
        # print(alpha)

    file_ptr.close()



f1.close()

if ham_files != 0:
    ham_accuracy = ham_predicted_correct/ham_files

if spam_files != 0:
    spam_accuracy = spam_predicted_correct/spam_files

# print(format(ham_accuracy, '.16f'), format(spam_accuracy, '.16f'))

# *********************************** Calculating the precision, recall and F1 score values ****************************
if (ham_predicted != 0):
    ham_precision = ham_predicted_correct/ham_predicted
if (spam_predicted != 0):
    spam_precision = spam_predicted_correct/spam_predicted

ham_recall = ham_predicted_correct/ham_files
spam_recall = spam_predicted_correct/spam_files

# print(ham_precision,ham_recall)
ham_f1 = (2*ham_precision*ham_recall)/(ham_precision+ham_recall)
spam_f1 = (2*spam_precision*spam_recall)/(spam_precision+spam_recall)
#
print(ham_predicted_correct, ham_predicted, ham_files, spam_predicted_correct, spam_predicted, spam_files)
print("ham accuracy", format(ham_accuracy, '.16f'))
print("spam accuracy", format(spam_accuracy, '.16f'))
print("spam precision", format(spam_precision, '.16f'))
print("spam recall", format(spam_recall, '.16f'))
print("spam F1", format(spam_f1, '.16f'))
print("ham precision", format(ham_precision, '.16f'))
print("ham recall", format(ham_recall, '.16f'))
print("ham F1", format(ham_f1, '.16f'))

