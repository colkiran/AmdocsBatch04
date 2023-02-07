
player_count = 11
rating = 8.5
has_won_world_cup = True
team_name = "Argentina"

print(player_count)
print(rating)
print(has_won_world_cup)
print(team_name)
# module name
print(__name__)         # double underscore => dunder_name

print("-" * 40)

a, b, c = 10, 20, "Hello"
print(a, b, c, sep=", ")

a = b = c = 150
print(a, b, c, sep=" : ")

first_name = "Micheal"
last_name = "Slater"

print("My first name is " + first_name + " and lastname is " + last_name)
# interpolation - format string or f string

print(f"My first name is {first_name} and lastname is {last_name}")

print("-" * 40)

prd1 = "Ooty Apples"
prd2 = "Kanpur Oranges"

print(f"we sell {prd1} and {prd2} to our customers")
print(f"we made a turnover of {150 * 50 + 200 * 180} by selling {prd1} and {prd2}")

print("-" * 40)
team_name = "Sahara India"
print(team_name)

team_name = "Sahara 'India'"
print(team_name)

team_name = 'Sahara \'India\''
print(team_name)

team_name = 'Sahara "India"'
print(team_name)
