# Created By Mohammed at Sep, 1 2022
# Band-Name-Generator
from curses import init_pair


print("Welcome to Band Name Generator")

city = input("Enter city you grew up in:\n")
petName = input("Enter your pet name:\n")

bandName = city + " " + petName
print(bandName)
