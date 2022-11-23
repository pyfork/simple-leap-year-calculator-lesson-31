# Get year from user
y = int(input("Which year do you want to check?\n"))

print(y)

l = "Leap year"
n = "Normal year"

# Can the year be divided by 4 with no remainder? Yes-next if; No-normal
# Can the year be divided by 100 with no remainder? Yes-next if; No-leap
# Can the year be divided by 400 with no remainder? Yes-leap; No-normal
if (y % 4 == 0):
  if (y % 100 == 0):
    if (y % 400 == 0):
      print(f"Divisible by 4, by 100 and by 400. Hooray! {y} is a {l}")
    else:
      print(f"Divisible by 4 and by 100 but not by 400 so this is a {n}")
  else:
    print(f"Divisible by 4 but not by 100 so this {y} is a {l} ")
else:
  print(f"Not divisible by 4 so it's a {n}")
