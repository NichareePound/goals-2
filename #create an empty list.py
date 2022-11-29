#create an empty list
goals = []

#append the goals
for i in range(5):
    new = (input("how many goal do you want? "))
    goals.append(new)


print(goals)
#edit an item
i = input(' which goal do you want to change? ')
#conver i form string to the integer
i = int(i)
goal[i] = input(' Enter a new goal: ')

print(goals)

#delete an item
i + int(input('which goal do you want to delete? '))
del goals[i-1]
print(goals)
