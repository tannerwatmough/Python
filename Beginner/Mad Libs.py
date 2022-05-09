# Init Variables
darkness = ""
light = ""
man = ""
blinding = ""
ally = ""
me = ""

shadows = ["", "", "", ""]
adverb = ["", ""]
# Get Input from User
print("Welcome user!")
print("Let's play a game of madlibs!")
me = input("Please share your name with me.\n")

# Get darkness var from user
print(f"Hello {me}! Are you ready?")
darkness = input("What is something you wish to know more about?\n")

# Get ally var from user
print(
    f"Oh you wish to know about {darkness}? Brave of you. Fine, I shall tell you, but first tell me what you already know about {darkness}?")
ally = input(f"What noun would you categorize {darkness} as:\n")

# Get adverb vars from user
print(f"Give me some adverbs for {darkness}\n")

for i in range(len(adverb)):
    adverb[i] = input(f"Adverb for {darkness} {i+1} / {len(adverb)}")

# Get light var from user
light = input(f"Opposing noun to {darkness}.\n")

# Get man var from user
man = input(f"An alternate noun for {me}.\n")

# Get blinding var from user
blinding = input(f"An adjective for {light}.\n")

# Get shadows vars from user
print(f"Things that belong to {me}:\n")

for i in range(len(shadows)):
    shadows[i] = input(f"Things (plural) {i+1} / {len(shadows)}")

# Init Story Flavor Text
print(f"Well here is everything you wanted to know about {darkness}")

# Init Story
story = (
    f"Ah you think {darkness} is your {ally}? You merely adopted the {darkness}. I was {adverb[0]} in it, {adverb[1]} by it.I didn't see the {light} until I was already a {man}, by then it was nothing to me but {blinding}! The {shadows[0]}, {shadows[1]}, {shadows[2]}, {shadows[3]} betray you because they belong to {me}")

# Print Story
print(story)
input()
