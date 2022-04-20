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


if __name__ == "__main__":
    choice = input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:")
    num1 = float(input("Podaj składnik 1: "))
    num2 = float(input("Podaj składnik 2: "))
    if choice == '1':
      logging.info("Dodaje: %f %f", num1, num2)
      print("wynik to", dodaj(num1,num2))
    elif choice == '2':
      logging.info("Odejmuję: %f %f", num1, num2)
      print("wynik to", odejmij(num1,num2))
    elif choice == '3':
      logging.info("Mnożę: %f %f", num1, num2)
      print("wynik to", pomnoz(num1,num2))
    elif choice == '4':
      logging.info("Dzielę: %f %f", num1, num2)
      print("wynik to", podziel(num1,num2))
    else:
      logging.info("niepoprawna wartość")

