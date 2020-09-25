list1 = []
n=int(input("Enter no of elements in the list: "))
print("Enter elements of the list: ")
for i in range(n):
    ele=float(input())
    list1.append(ele)
print("Positive elements of the list: ")
for x in list1:
    if(x>=0):
        print(x)