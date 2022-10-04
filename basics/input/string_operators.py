print("Please enter the number of lives.")
lives = int(input())
heart = u'\u2665'
totalL = str(lives*heart)

print("Please enter the energy level.")
energy = int(input())
diamond = u'\u25C6'
totalE = str(energy*diamond)

print("Please enter the shield level")
shield = int(input())
totalS = str(shield*diamond)

print("Health has been set.")
print("\n")

print(f"Lives: {totalL}")
print(f"energy: {totalE}")
print(f"shield: {totalS}")