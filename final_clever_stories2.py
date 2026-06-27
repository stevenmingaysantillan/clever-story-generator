"""
I changed some of the phrases so that the user will have to write more ideas in the story, 
and I added two sentences at the end (line 27-28) to make the story even funnier and unpredictable. 
On line 24 I used an apostrophe so that the program won't be confused with the quotation mark in exclaimation.
"""
print()
print("Please enter the following:")
print()
time = input("time of day: ")
adjective = input("adjective: ")
animal = input("animal: ")
verb = input("verb: ")
place = input("place: ")
exclaimation = input("exclaimation: ")
verb2 = input("verb: ")
verb3 = input("verb: ")
noun = input("noun: ")
favorite_activity = input("favorite thing to do: ")
hate_to_do = input("the thing you hated to do the most: ")
print()
print("Your story is:")
print()
print(f"The other {time}, I was really in trouble. It all started when I saw a very ")
print(f'{adjective} {animal} {verb} down the {place}. "{exclaimation.capitalize()}!" I yelled. But all ')
print(f"I could think to do was {verb2} over and over. Miraculously, ")
print(f"that caused it to stop, but not before it tried to {verb3} ")
print(f"right in front of my {noun}. Then I instinctively {favorite_activity}, thinking ")
print(f"I could stop it. After that, I {hate_to_do}, and call it a day.")