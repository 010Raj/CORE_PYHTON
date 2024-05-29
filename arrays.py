#integer in array
array_list=[10,12,13,516,78]
print("array using list :",array_list[0])
for i in array_list:
    print(i)
#passing string
string_array=['ramu','shyamu','pappu','giyan']
print(len(string_array))
#insertion
string_array.insert(1,"aniket")
print(string_array)
#deletion
string_array.remove("shyamu")
print(string_array)

#table
array_table=int(input("enter the no. = "))
for i in range(1,11):
    print(array_table,'x',i,'=',array_table*i)

