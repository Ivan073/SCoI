print("Hello World")

inp1=int(input("Number 1: "))
inp2=int(input("Number 2: "))
op=input("Operation: ")

if op=="add":
    print(inp1+inp2)
elif op=="sub":
    print(inp1-inp2)
elif op=="mult":
    print(inp1*inp2)
elif op=="div":
    print(inp1/inp2)

numbers = [1,2,3,4,5,6,7,8]
filtered_numbers=filter(lambda num:num%2==0,numbers)
print(list(filtered_numbers))
