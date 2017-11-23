#Simple list comps
# even number print

print([x for x in range(10) if x % 2 == 0])


# How to go from for loop to list comp:
"""
http://treyhunner.com/2015/12/python-list-comprehensions-now-in-color/

We copy-paste from a for loop into a list comprehension by:

Copying the variable assignment for our new empty list
Copying the expression that we’ve been append-ing into this new list
Copying the for loop line, excluding the final :
Copying the if statement line, also without the :
"""
# end How to go from for loop to list comp

# from ...
doubled_odds = []
for n in numbers:
    if n % 2 == 1:
        doubled_odds.append(n * 2)

# to ...
doubled_odds = [n * 2 for n in numbers if n % 2 == 1]
