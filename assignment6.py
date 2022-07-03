#Question 1
#Perfect Number

def perfect_number(n):
    s=0
    for i in range(1,n):
        if(n%i==0):
            s+=i #Storing the sum of divisors excluding the number itself
    if(s==n):
        return True
    else:
        return False

N=int(input("Enter a number: ")) #taking user's input
if(perfect_number(N)==True):
    print(N," is a perfect number")
else:
    print(N," is not a perfect number")
print()

#Question 2
#Palindrome String

def palindrome(s):
    s1=""
    s1 = s[::-1]
    return s1
S=input("Enter a String: ")
if(palindrome(S)==S):
    print(S,"is a palindrome")
else:
    print(S,"is not a palindrome") 
print()

#Question 3
#Pascal's Triangle

def factorial(m):
    s=1
    for i in range(1,m+1):
        s*=i
    return s

def pascal(n):
    for i in range(n):
        for j in range(n-i+1):
            print(end=" ")
        for j in range(i+1):
            #nCr=n!/(r!(n-r)!)
            print(factorial(i)//(factorial(j)*factorial(i-j)),end=" ")
        
        print() #Printing new line
N=int(input("Enter a number: "))
pascal(N)
print()

#Question 4
# Check if the string is pangram

def ispangram(str):
	alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	for char in alphabet:
		if char not in str.lower():
			return False

	return True
	
s=input("Enter a String: ")
if(ispangram(s) == True):
	print(f"Yes '{s}' is a panagram")
else:
	print(f"No '{s}' is not a panagram")
print()

#Question 5
#Hyphen Seperated Sentence


input_string=str(input("Enter a hyphen separated sentence: "))

li=input_string.split("-") #Splitting the string into a list of strings
li.sort() #Sorting the list using sort function

print("-".join(li))
print()
#Question 6
#Student Data

def student_data(student_id,**kwargs):
    print("Student ID=",student_id)
    if "student_name" in kwargs:
        print("Student Name=",kwargs["student_name"])
    if "student_class" in kwargs:
        print("Student Class=",kwargs["student_class"])

student_data(student_id="21102032")
student_data(student_id="21102032",student_name="Anoop kumar")
student_data(student_id="21102032",student_name="Anoop kumar",student_class="1st Year")
print()


#Question 7

class Student:
    pass 
class Marks:
    pass 
student1 = Student()
marks1 = Marks()
print(isinstance(student1, Student))
print(isinstance(marks1, Student))
print(isinstance(marks1, Marks)) 
print(isinstance(student1, Marks))
print("\nCheck whether the said classes are subclasses of the built-in object class or not.")
print(issubclass(Student, object))
print(issubclass(Marks, object))
print()

#Question 8
#Print all triplets within an array whose sum is zero


#Question 8
#Print all triplets within an array whose sum is zero

def findTriplets(arr, n):

	found = False
	for i in range(0, n-2):
	
		for j in range(i+1, n-1):
		
			for k in range(j+1, n):
			
				if (arr[i] + arr[j] + arr[k] == 0):
					print(arr[i], arr[j], arr[k])
					found = True
	
			
# If no triplet with 0 sum found in array
	if (found == False):
		print("No triplets exist")
lst = []
n = int(input("Enter number of elements : "))

for i in range(0, n):
	ele = int(input())
	lst.append(ele) 
print(findTriplets(lst,n))

#Question 9
#Parantheses 

class parantheses:
    def find(str):
        a= ['()', '{}', '[]'] 
        while any(i in str for i in a):
            for j in a:
                str = str.replace(j, '') 
        return not str 

s = input("Enter the sequence of parantheses : ")
if parantheses.find(s):
    print(s,"-","is balanced")
else:
    print(s,"-","is unbalanced")
    
    
    
#Output of question 1
Enter a number: 6
6  is a perfect number

#Output of question 2
Enter a String: mam
mam is a palindrome

#Output of question 3
Enter a number: 5
      1 
     1 1
    1 2 1
   1 3 3 1
  1 4 6 4 1

#Output of question 4
Enter a String: the quick brown fox jumps over a lazy hazy dazy dog
Yes 'the quick brown fox jumps over a lazy hazy dazy dog' is a panagram

#Output of question 5
Enter a hyphen separated sentence: red-yellow-blue-green
blue-green-red-yellow

#Output of question 6
Student ID= 21102032
Student ID= 21102032
Student Name= Anoop kumar
Student ID= 21102032
Student Name= Anoop kumar
Student Class= 1st Year

#Output of question 7
True
False
True
False

Check whether the said classes are subclasses of the built-in object class or not.
True
True

#Output of question 8
Enter number of elements : 6
-4
3
1
5
6
-11
-4 3 1
5 6 -11
None

#Output of question 9
Enter the sequence of parantheses : {}[]
{}[] - is balanced
