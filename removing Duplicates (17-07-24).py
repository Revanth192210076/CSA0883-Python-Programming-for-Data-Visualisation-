test_list = [-12, -78, -35, -42]
print("The original list is : " + str(test_list))

res = []
for i in test_list:
    if i not in res:
        res.append(i)

print("The list after removing duplicates : " + str(res))
