class Item:
    def __init__(self, name, boatPart):
        self.name = name
        self.boatPart = boatPart

theBeach = "the Beach"
moreSand = Item("more Sand", True)
sand = Item("sand", True)
evenMoreSand = Item("Even More Sand", False)
birds = Item("Birds", False)
crabs = Item("Crabs", False)
deadFish = Item("A dead fish", False)
messageBottle = Item("A message in a bottle", False)
practiceDummy = Item("a beat up Practice Dummy", False)
emerge = "You emerge from the jungle onto the beach. 'If I weren't stuck here, this beach would be a beautiful place,' you think to yourself bitterly."

theRavine = "the Ravine"
crumblingCliffs = Item("Crumbling Cliffs", True)
number42 = Item("the number 42", False)
views = Item("Scenic views", False)
tree = Item("A fallen tree", False)
meaning = Item("The meaning of life, the universe, and everything", False)
emergeRavine = "There is barely any warning as you emerge from the jungle and find yourself facing a massive ravine. You look precariously over the edge, but it is so deep you cannot see the bottom"

theSpring = "the Spring"
despair = Item("Despair", False)
water1 = Item("Water", True)
water2 = Item("Water", False)
water3 = Item("Water", False)
food = Item("Food", False)
crocodile = Item("Crocodile", False)
nothing =  Item("Nothing", False)
deer = Item("a small deer", False)
emergeSpring = "The soft gurgle of water leads you up a small bluff to reveal a small spring, its waters bubbling out of the rocks."

theTemple = "the Temple"
statue = Item("Golden Monkey Statuette", True)
boulderTrap = Item("Boulder Trap", False)
emergeTemple = "As you push your way through the thick vegetation, you stumble upon an ancient Temple standing stalwart in a small clearing. The area around the temple seems quiet. Too quiet..."