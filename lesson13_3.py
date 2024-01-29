#Write a Python program to add two given lists using map and
#lambda.(map-y kara function-ic heto mekic avel hajordakanutyun
#ynduni, orinak erku list)
list0 = [1,2,3,4]
list1 = [5,6,7,8]
result = map(lambda x,z: x+z,list0,list1)
print(list(result))