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
y - input("Enter number y: ")
print (x + y) # x = 3, y = 3 , wynik 33, lub x = cycki, y = duże, wynik = cyckiduże


x = int(input("Enter number x: "))
y - int(input("Enter number y: "))		# zamiana inputa na int
print (x + y) # x = 3, y = 3, wynik 6, lub x = cycki, wynik = błąd



Statements:

if x < y:									# pierwszy warunek, jeśli się zgadza, to print
	print("x jest mniejsze niż y!")
elif: x > y:								# jeśli pierwszy się nie zgadza, to sprawdza ten
	print("x jest większe niż y")
else:										# jeśli obydwa się nie zgadzają, to:
	print("x jest równe y")


