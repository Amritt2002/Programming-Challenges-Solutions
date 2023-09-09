Q1 - Variable Declaration and Printing
Question Type: Variable declaration and printing.

In this section, you're creating four variables with different data types and printing their values.

a is a string variable containing the name "Amritanshu".
b is a tuple variable containing a mix of integers, strings, floats, and a complex number.
c is a tuple variable containing three floating-point numbers.
d is a tuple variable containing four strings representing fruits.
You're printing the values of these variables using print().

Q2 - Data Type Checking
Question Type: Data type checking.

In this section, you're checking the data types of four variables and printing the results.

var1 is an empty string, so its data type is str (string).
var2 is a string containing a list-like structure, but it's still a string, so its data type is str.
var3 is a list containing three strings, so its data type is list.
var4 is a floating-point number with a decimal point, so its data type is float.
You're using the type() function to determine and print the data types of these variables.

Q3 - Operator Explanation
Question Type: Explanation of mathematical operators.

In this section, you're explaining the use of four mathematical operators with examples.

/ is the division operator. It divides one number by another. For example, 6 / 2 results in 3.0 because it divides 6 by 2, giving you a floating-point result.

% is the modulo operator. It calculates the remainder when one number is divided by another. For example, 5 % 2 results in 1 because when 5 is divided by 2, you have a remainder of 1.

// is the floor division operator. It divides two numbers and returns the integer part of the result. For example, 6 // 3 results in 2 because it divides 6 by 3 and gives you the integer quotient, which is 2.

** is the exponentiation operator. It raises one number to the power of another. For example, 5 ** 2 results in 25 because it raises 5 to the power of 2, giving you 25.

You're performing these operations and printing the results.

Q5 - Loop and Conditional Statements
Question Type: Loop and conditional statements.


In this section, you're using a while loop to determine if number A is purely divisible by number B and counting how many times it can be divided.

You take two integer inputs from the user, A and B.
You initialize a counter (count) to 1 and a temporary variable (temp) to B.
You use a while loop to repeatedly add B to temp and increment count until A is less than temp. This loop essentially checks how many times B can be added to itself until it becomes greater than A.
After the loop, you check if A is divisible by B (A % B == 0). If it is, you print that B can divide A purely and mention how many times (count) it can do so. If not, you print that B cannot divide A purely.


Q6 - List Manipulation and Conditional Statements
Question Type: List manipulation and conditional statements.

In this section, you're creating a list of 25 integers and using a for loop with an if-else condition to check if each element is divisible by 3.

You create a list l containing 25 integers.
You then calculate the length of the list and store it in the variable count.
You use a for loop to iterate through each number in the list (num).
Inside the loop, you use the modulo operator (%) to check if num is divisible by 3. If the remainder is 0, it means num is divisible by 3, and you print a message indicating that. Otherwise, you print "not" to indicate that it's not divisible by 3.
So, this code prints whether each number in the list is divisible by 3 or not using a for loop and if-else condition.

Q7 Q7. What do you understand about mutable and immutable data types? Give examples for both showing
this property.
"""Immutable Data Types:

Immutable data types are those where the data cannot be changed after it is created. When you perform an operation that appears to modify an immutable data type, you're actually creating a new object with the modified value, leaving the original object unchanged.
Examples of Immutable Data Types:

Integers (int): Once an integer is assigned to a variable, it cannot be changed. Any operation that seems to change the integer results in a new integer.
Strings (str): Strings are also immutable. Any operation that seems to modify a string creates a new string."""
#EX:1
x = 5  # x is assigned the integer 5
x = x + 1  # A new integer (6) is created and assigned to x
#EX:2
s = "Hello"  # s is assigned the string "Hello"
s = s + " World"  # A new string is created ("Hello World") and assigned to s

"""Mutable Data Types:

Mutable data types, on the other hand, can be modified in place. This means you can change their content without creating a new object.
Examples of Mutable Data Types:

Lists (list): Lists are mutable. You can modify their elements, append, remove, or change values within the same list."""

#EX:1
my_list = [1, 2, 3]
my_list.append(4)  # Modifies the original list by adding 4

#EX:2
my_dict = {"name": "Alice", "age": 30}
my_dict["age"] = 31  # Modifies the age value in the original dictionary







