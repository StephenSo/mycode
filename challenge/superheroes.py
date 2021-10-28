#!/usr/bin/env python3
from random import randint

classinfo = {"all": 
    [
        {
            "First": "Bala",
            "Last": "Kambale",
            "Skill Level": "G.O.A.T.",
            "Spirit Animal": "zebra",
            "Super Power": "Mind control",
        },
        {
            "First": "Inderjeet",
            "Last": "Khalsa",
            "Skill Level": "astonishing",
            "Spirit Animal": "seal",
            "Super Power": "Technopathy",
        },
        {
            "First": "Jon",
            "Last": "Whiteside",
            "Skill Level": "stunning",
            "Spirit Animal": "ram",
            "Super Power": "Levitation",
        },
        {
            "First": "Nikita",
            "Last": "Nikale",
            "Skill Level": "wondrous",
            "Spirit Animal": "otter",
            "Super Power": "Psychic",
        },
        {
            "First": "Steve",
            "Last": "Spike",
            "Skill Level": "breathtaking",
            "Spirit Animal": "lion",
            "Super Power": "Portal creation",
        },
        {
            "First": "Vinod",
            "Last": "Singh",
            "Skill Level": "wonderful",
            "Spirit Animal": "badger",
            "Super Power": "Immortal",
        },
    ]
}
# "My name is ______ and my spirit animal is _______.

vowels = ['a','e','i','o','u']
for student in classinfo["all"]:
    if (student['First'] == "Steve"):
        print(f"My name is {student['First']} {student['Last']} and my spirit animal is {student['Spirit Animal']}")
print()

for student in classinfo["all"]:
    ia = "a"
    if (student['Skill Level'][0] in vowels):
        ia = "an"
    print(f"{student['First']} {student['Last']}, {ia} {student['Skill Level']} {student['Spirit Animal']} of a programmer, possesses {student['Super Power']} keeping them at the top of their game.")
