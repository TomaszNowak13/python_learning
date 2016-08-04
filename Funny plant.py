"""Scientist have discovered a new plant. The fruit of the plant
can feed 1 person for a whole week and best of all, the plant never dies.
Fruits needs 1 week to grow, so each week you can harvest it fruits.
Also the plant gives 1 fruit more than the week before and to get more
plants you need to plant a fruit.
Now you need to calculate after how many weeks, you can support a
group of x people, given y fruits to start with."""

def plant():
    people = int(input("Enter number of people: "))
    fruits = int(input("Enter number of fruits available from beginning: "))
    weeks = 1
    total_fruits = 0
    total_plants = fruits
    while people > total_fruits:
        total_fruits += total_plants
        total_plants += total_fruits
        weeks += 1
    print("Weeks before you can feed", people, "people -", weeks)

plant()
