# Created By Mohammed at Sep, 1 2022
from curses import init_pair


print("Welcom to Band Name Generator")

city = input("Enter city you grew up in:\n")
petName = input("Enter your pet name:\n")

bandName = city + " " + petName
print(bandName)