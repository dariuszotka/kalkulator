import sys
import logging
logging.basicConfig(level=logging.DEBUG)
def dodaj(x, y):
  return x + y
def odejmij(x, y):
  return x - y
def pomnoz(x, y):
  return x * y
def podziel(x, y):
  return x / y
choice = input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:")
num1 = float(input("Podaj składnik 1: "))
num2 = float(input("Podaj składnik 2: "))
if choice == '1':
  logging.info("dodaję", num1, "i", num2)
  print("wynik to", dodaj(num1,num2))
elif choice == '2':
  logging.info("od", num1, "odejmuję", num2)
  print("wynik to", odejmij(num1,num2))
elif choice == '3':
  logging.info("mnożę", num1, "i", num2)
  print("wynik to", pomnoz(num1,num2))
elif choice == '4':
  logging.info("dzielę", num1, "przez", num2)
  print("wynik to", podziel(num1,num2))
else:
  logging.info("niepoprawna wartość")

if __name__ == "__main__":
    logging.debug("The program was called with this parameters %s and %s" % (sys.argv[1], sys.argv[2]))
    x = sys.argv[1]
    y = sys.argv[2]

