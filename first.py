print ("hello") # wyświetla wartość pomiędzy nawiasami,
	print("10"+"10") # da nam 1010
	print(10 + 10) # da nam 20
	print(type(10)) # zwróci nam informacje o rodzaju zmiennej - tutaj int
	print(type("dziesięć")) # zwróci nam informację o rodzaju zmiennej - tutaj str

 str "hello" 'hello' # wartość wyrażona w słowach przez użytkownika, można używać podwójnych, pojedyńczych quotation marks, trzy to Multi LinK String
'''
MULTI
LINE
STRING
'''
int 3 6 -9 # wartość wyrażona w liczbach całkowitych+ -
float 10.9 66.6 -69.60 # wartość wyrażona w liczbach z rozwinięciem dziesiętnym
bool True False # de facto są tylko dwa stany, on/off, 0/1, Prawda lub Fałsz



Variables # placeholders do późniejszego wykorzystania

1.
x = 10
y = 20
whatever = True

print (x) # da nam 10
print (x + y) # da nam 30

2.
x = "120"
print(x / 4) # da nam błąd próby dzielenia stringa przez int

x = "120"
X = int(x) #konwersja str na int, działa tylko w jeśli faktycznie str to liczba
print(x / 4) #da nam 30

3.
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)


Operators -   
												# można przyrównywać również str:
 + addition										# x = "hello"
 - substraction									# y = "hello"
 * multiplication								# print(x == y)
 / division										# True
 % modulus - reszta z dzielenia
 ** the power - potęga
 // dzielenie z zaokrągleniem do mniejszej
 == equals
 != not equals
 < less than
 > greater than
<= less or equals
>= more or equals

and 					 10 < 20 and 20 < 30   wynik: true 
or 						 10 = 10 or 20 > 10		wynik: true
not						# odwraca wynik 0 -> 1, 1 -> 0

Operator		Name					Description
& 				AND						Sets each bit to 1 if both bits are 1
|				OR						Sets each bit to 1 if one of two bits is 1
^				XOR						Sets each bit to 1 if only one of two bits is 1
~ 				NOT						Inverts all the bits
<<				Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off
>>				Signed right shift		Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off

input - wartość jaką poda uzytkownik

x = input("Enter number x: ")
y = input("Enter number y: ")
print (x + y) # x = 3, y = 3 , wynik 33, lub x = cycki, y = duże, wynik = cyckiduże


x = int(input("Enter number x: "))
y = int(input("Enter number y: "))		# zamiana inputa na int
print (x + y) # x = 3, y = 3, wynik 6, lub x = cycki, wynik = błąd



Statements:

if x < y:									# pierwszy warunek, jeśli się zgadza, to print
	print("x jest mniejsze niż y!")
elif: x > y:								# jeśli pierwszy się nie zgadza, to sprawdza ten
	print("x jest większe niż y")
else:										# jeśli obydwa się nie zgadzają, to:
	print("x jest równe y")

## Przykład:

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")




Loops:
while 						#wykonywanie programu do czas aż...
for x in range (1,21)		#wykonanie programu 20x

break 						#koniec pętli
pass



#6 LISTS

	#index 0   1   2    3        4     5		liczenie zaczynamy od 0
mylist = [10, 20, 30, "string", True, 8.97]
print(mylist) # wynik [10, 20, 30, 'string' True, 8.97]
print(mylist[3]) # wynik 'string'
print(mylist[:3]) # wynik [10, 20, 30]
print(mylist[1:3]) # wynik [20, 30]
print(mylist[-2]) # wynik True - 2 od końca, liczenie zaczynamy od prawej od 1

mylist[3] = "anoter string" # zmiana 3 wpisu na "xxxx"
print(mylist) # wynik [10, 20, 30, "another string", True, 8.97]

for x in mylist:
	print(x)

# unpacking a list:
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x) # wynik apple,
print(y) # wynik banana,
print(z) # wynik cherry,

x = [1, 2, 3]
y = [4, 5, 6]
print(x + y) # wynik [1, 2, 3, 4, 5, 6]
print(x * 2) # wynik [1, 2, 3, 1, 2, 3]
print(len(x)) # 3 - len/lenght
print(max(x)) # 3 - podaje max wartość listy
print(min(x)) # 1 - podaje min wartość listy
x.append("new") # dodanie wartości na ostatnim miejscu listy
print(x) # wynik [1, 2, 3, new]
print(x.index("new")) # wynik 3 - zwraca index wartości o którą pytamy
x.insert (2, "another one") # wynik [1, 2, another one, 3, new] - wstawienie wartość o indexie 2
x.remove("another one") # wynik [1, 2, 3, new] - remove usuwa konkretną wartość
x.pop(3) # wynik [1, 2, 3] - pop usuwa wartość o indexie 3
x.sort() # układa od najmniejszego do największego i zapisuje liste w tej kolejnosci
print(sorted(x)) # wyświetla listę od najmniejszej do największej wartości,
y = sorted(x) # tworzy listę y z posortowanej listy x



Tuples - Krotki:
x = (1, 2, 3) # lista której nie można modyfikować

# sposób na zmianę
x = (1, 2, 3)
x = list(x)
x[2] = 10
x = tuple(x)
print(x)  # wynik (1, 2, 10)



Dictionary:
person = {"name":"Mark", "age":69, "gender": "male" }  # sposób tworzenia 
print(person["name"])
person{"newKey"} = "black" # dodawanie nowego wpisu

print(person.items()) # wyświetla wszystko, tj. keys + values
print(person.keys()) # wyświetla tylko keys, name, age, etc
print(person.values()) # wyświetla wartości



Membership Operators
x = [1,2,3]
print(2 in x) # wynik True
print(7 in x) # wynik False

	if type(x) is int:
		print("x is int")
	else:
		print("x is not int")



## 7 Functions

def helloworld():			# sposób tworzenia własnych algorytmów
	print("hello world!")

helloworld()				#uruchomienie algorytmu

# przykład 1.
def add(x=0, y=0):
	return x + y

result = add()
print(result)

#przykład 2.
def mysum(*numbers):
	result = 0 					#defaultowa liczba, może być 0
	for number in numbers:
		result += number
	return result

print(mysum(1, 2, 3, 50))

# przykład 3.
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x) #Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.
	# To create a global variable inside a function, you can use the global keyword.


## 8 Exception Handling

try:			#tym sposobem możemy wymusić kontynuowanie działania kodu po wykryciu błędu
	x = int(input("first number: "))
	y = int(input("second number: "))
	print (x / y)
except:
	print("there was an error!") # to zostanie wykonane w razie błędu

# kolejny przykład

try:			
	x = int(input("first number: "))
	y = int(input("second number: "))
	print (x / y)
except ValueError:				# w przypadku wykrycia błędu ValueError
	print("Please enter a valid number")
except ZeroDivisionError:
	print("nie dziel chuju przez zero")
	y = 1
	print(x / y)
finally:
	print("Well done my nygga!")

## 9 File Operation

open #funkcja otwarcia pliku
open('myfile.txt', 'r') # r - reading,
file.close() # zamknięcie po wykonaniu operacji

# drugi sposób na automatyczne zamknięcie pliku:
file = open('myfile.txt', 'r')
with open('file.txt', 'r') as f:  #with - funkcja otwarcia pliku, po zakończeniu autom. zamyka
	# ALL OF MY CODE			  # as f: - zapisz jako f
	pass

file = open("file.txt", "w")	# w - nadpisanie tekstu
file.write("Hello śmieciu!")
file.flush # zapisuje zmiany w pliku bez jego zamykania, aby dalej z niego korzystać

file = open("file.txt", "a") # a - dodanie na końcu tekstu

from os import * # z modułu os zaimportuj * - czyli wszystko
from os import rename, remove # z modułu zaimportuj tylko dwie funkcje
mkdir("test") # make directory "test"
chdir("test") #change directory - wejście do folderu test
mkdir("newDir") # wynik - stworzenie NewDir w test
rename("myfile.txt", "mynewfile") #zmiana nazwy pliku
remove("mynewfile.txt") # usunięcie pliku



-------------   ## 10 String Functions

text = "Hello World!"
print(len(text)) # podaje długość stringu, tutaj: 12, liczy wszystko, spacje, , , ! etc.
															
													index:	0    1    2    3    4
# o stringu możemy myśleć jako o liście. "Hello" = text = ["H", "e", "l", "l", "o"]
print(text[2]) # wynik - "l"
print(text[:6]) # wynik - "World"

for letter in text:
	print(letter) # wynik
					H
					e
					l
					l
					o

					W
					o
					r
					l
					d
					!

text = "Hello World! /nThis day is awsome!" # /n newline, tworzy nową linijkę
print(text) # Wynik: Hello World!
			#  		 This day is awsome!
/t = tab
/b = backspace
/s = space

name = input()
age = int(input())
print("My name is %s and I am %d years old" (name, age)) # %s - oczekiwany typ danych - string, %d - different type data
print("My name is () and I am () years old!".format(name, age)
txt = "We are the so-called \"Vikings\" from the north." #The escape character allows you to use double quotes when you normally would not be allowed:


text = "This is my text!"
text = text.upper() # Wynik - "THIS IS MY TEXT"
text = text.lower() # wynik - "this is my text"
text = text.title() # wynik - "This Is My Text"
text = text.swapcase() # wynik - "tHIS IS MY TEXT"
print(text.count("i")) # wynik - 2
print(text.count("t") + text.count("T")) # wynik - 3
print(text.find("my")) # wynik 8

#The strip() method removes any whitespace from the beginning or the end:
		a = " Hello, World! "
		print(a.strip()) # returns "Hello, World!"

#The replace() method replaces a string with another string:
		a = "Hello, World!"
		print(a.replace("H", "J"))


separator = ";" # rozdziela wartości z listy wskazanym separatorem
mylist = ["dupa", "cycki", "kot"]
print(separator.join(mylist)) # wynik dupa;cycki;kot

text = "raz dwa trzy raz"
words = text.split("a") # rozdziela tekst po wystąpieniu wskazanego znaku
print(words) # wynik - ['r', 'z dw', ' trzy r', 'z']
print(text.replace("raz", "osiem")) # podmienia wskazane słowo na inne; wynik - osiem dwa trzy osiem


#Use the format() method to insert numbers into strings:
		age = 36
		txt = "My name is John, and I am {}"
		print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))


###### Intermediate Tutorial ######

#1 Classes and Objects

Pierwszy sposób:
class Person:
	def __init__(self):	
		self.name = "Master"
		self.age = 32

person1 = Person()
print(person1.name) # wynik - Master
print(person1.age) # wynik - 32

Drugi sposób:
class Person:

	amount = 0 		#początkowa liczba osób
	def __init__(self, name, age, height):
		self.name = name
		self.age = age
		self.height = height
		person.amount += 1 			# doliczenie jednej osoby po jej utworzeniu

	def __del__(self):				# definicja "co się stanie jak skasujemy obiekt"
		person.amount -= 1 			# odjęcie jednej osoby po jej skasowaniu
		print("Object deleted!")

	def __str__ (self):				# kolejny sposób, gdy traktujemy obiekt jako string
		return "Name: {}, Age: {}, Height: {}".format(self.name, self.age, self.height)

person1 = Person("Master", 32, 175)
print(person1.name)
print(person1.age)
print(person1.height)

del person1		#kasowanie obiektu person1

## 2 Inheritance - dziedziczenie

class Worker(Person): #w nawiasie podajemy klasę-matkę 
	def __init__(self, name, age, height, salary):
		super(Worker, self).__init__(name, age, height) # super - przeniesienie definicji z parent-class
		self.salary = salary # Person nie musi mieć salary, Worker tak

	def __str__(self):
		text = super(Worker, self).__str__()
		text += ", Salary {}".format(self.salary)
		return text

	def calc_yearly_salary(self):
		return self.salary * 12

worker1 = Worker("Henry", 40, 176, 3000)
print(worker1)
print(worker1.calc_yearly_salary())

# Overloading operators

class Vector:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __add__(self, other):
		return Vector(self.x + other.x, self.y + other.y)

	def __sub__(self, other):
		return Vector(self.x - other.x, self.y - other.y)

	def __str__(self):
		return "X: {}, Y: {}".format(self.x, self.y)

v1 = Vector(2,5)
v2 = Vector(6,3)

print("V1: ", v1)
print("V2: ", v2)

v3 = v1 + v2

print("V3: ", v3)


## Working with JSON! -JavaScript Object Notation

import json # załaduj moduł json

people_string = '''
{
	"people": [
		{
			"name": "John Smith",
			"phone": "691-689-125",
			"emails": ["js@gmail.com", "js2022@gmail.com"],
			"has_license": false
		},
		{
			"name": "John Doe",
			"phone": "691-689-166",
			"emails": ["jdsq@gmail.com", "jdfuckme@gmail.com"],
			"has_license": true
		}
	]
}
'''
data = json.loads(people_string) # zamienia dictionary na stringa

print(data) # wynik - {'people': [{'name': 'John Smith', 'phone': '691-689-125', 'emails': ['js@gmail.com', 'js2022@gmail.com'], 'has_license': False}, {'name': 'John Doe', 'phone': '691-689-166', 'emails': ['jdsq@gmail.com', 'jdfuckme@gmail.com'], 'has_license': True}]}

for person in data["people"]:
	print(person["name"]) #wynik - John Smith, 
						  #	       John Doe

for person in data["people"]:
	del person["phone"]		#kasuje keys i value "phone"

new_string = json.dumps(data)

print(new_string)

##

import json

with open("states.json") as f:
	data = json.load(f)
for state in data['state']:
	print(state['State'], state["Abbrev"])
	del state["Code"]

with open("new_states.json", "w") as f:
	json.dump(data, f, indent=2)

## JSON - ładowanie z URL
import json
from urllib.request import urlopen

with urlopen("https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json") as response:
	source = response.read()

data = json.loads(source)
print(json.dumps(data, indent=2))

print(len(data["list"]["resources"])) # liczenie wpisów w podliście resources
 
 for item in data["list"]["resources"]:
 	name = item["resource"]["fields"]["name"] # podawanie ścieżki skąd ma pobierać zmienną name
 	price = item["resource"]["fields"]["price"] # jw
 	print(name, price) # wybranie z całej biblioteki zmiennych name i price



## full XML procesing Guide in Python

xml.sax # simple API for XML - można odczytać, używać, ale nie zmieniać
xml.dom # Document Object Model


import xml.sax

class PeopleHandler(xml.sax.ContentHandler):

	def startElement(self, name, attrs):
		self.current = name
		if name == "person":
			print(f"-- Person {attrs["id"]} --")

	def characters(self, content):
		if self.current == "name":
			self.name = content
		elif self.current == "age":
			self.age = content
		elif self.current == "weight":
			self.age = content
		elif self.current == "height":
			self.age = content

	def endElement(self, name):
		if self.current == "name":
			print(f"Name: {self.name}")
		elif self.current == "age":
			print(f"Age: {self.age}")
		elif self.current == "weight":
			print(f"Weight: {self.weight}")
		self.current = ""