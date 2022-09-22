# 78
list_ = [6,12,4,3,8]
for i in range(len(list_)-1):
    for z in range(len(list_)-1-i):
        if list_[z] > list_[z+1]:
            list_[z], list_[z+1] =  list_[z+1], list_[z]
print(list_)


