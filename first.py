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