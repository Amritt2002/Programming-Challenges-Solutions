#Q1. Create one variable containing following type of data:
#string
a = "Amritanshu"
#list
b=(1,2,5,6, "ak",7.9,4+5j)
#float
c= (5.5,9.9,8.8)
#tuple
d=("apple","banana","gauava","grapes")
print(a)
print(b)
print(c)
print(d)


#next questions
#Q2. Given are some following variables containing data:
#What will be the data type of the above given variable.

var1 = ''
   
var2 = '[ DS , ML , Python]'

var3 = [ 'DS' , 'ML' , 'Python' ]

var4 = 1.

print(type(var1))
print(type(var2))
print(type(var3))
print(type(var4))


#next questions

#Q3. Explain the use of the following operators using an example:

#(i)	/
#this is a divison operator and it is use to divide the numbers and to get result.
a=6/2

#(ii)	% 
#this is  a modulo operator which is use to divide the number and get the remainder only.
b=5%2

#(iii)	//
#this  is a division floor operator and gives quotient or result. 
f=6//3

#(iv)	**
#this is power operator use to guve the power to a number
g= 5**2

print(a)
print(b)
print(f)
print(g)


#next questions

#Q5. Using a while loop, verify if the number A is purely divisible by number B and if so then how manytimes it can be divisible.
# Input the two numbers A and B
# Input the two numbers A and B
A = int(input("Enter number A: "))
B = int(input("Enter number B: "))

# Initialize a counter to keep track of how many times A can be divided by B
count = 1
temp = B
# Use a while loop to repeatedly divide A by B until it's no longer divisible
while A >= temp:
    temp+=temp
    count+=1
    

# Check if A is reduced to 0, indicating it was purely divisible by B
if A % B == 0:
    print(f"{B} can divide {A} purely {count} times.")
else:
    print(f"{B} cannot divide {A } purely.")


#next Qyestion

#Q6. Create a list containing 25 int type data. Using for loop and if-else condition print if the element is divisible by 3 or not.
l = [12,13,16,17,18,89,67,28,1,10,9,4,2,22,77,3,33,99,551,24,2222,189,102,1010,999]
count = len(l)
print(f"list conttain {count} elements")

for num in l:
    if num % 3 == 0:
        {
        print(f"{num} id div by 3")
        }
    else:
            print("not")


 
    

    





