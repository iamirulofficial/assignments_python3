types_of_people = 10
x =  f"There are {types_of_people} types of people."
binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

print(f"I said : {x}")
print(f"I also said: '{y}'")

hilarious = False
joke_evolution = "Isn't that joke so funny? {}"

print(joke_evolution.format(hilarious))

print(x + y)
e1="c"
e2="a"
e3="t"
e4="t"
e5="l"
e6="e"
print(e1 + e2 + e3, end=' ')
print(e4 + e5 + e6)

formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
 "Try your",
 "Own text here",
 "Maybe a poem",
 "Or a song about fear"
 ))
