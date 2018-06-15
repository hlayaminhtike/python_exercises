states = {
        'Oregon':'OR',
        'Florida':'FL',
        'California':'CA',
        'New York':'NY',
        'Michigan':'MI'
        }

Cities = {
        'CA':'San Francisco',
        'MI':'Detroit',
        'FL':'Jacksonville'
        }

Cities['NY']='New York'
Cities['OR']='Portland'


print('-' * 10)
print("NY State has: ", Cities['NY'])
print("OR State has: ", Cities['OR'])


print('-' * 10)
print("Michigan's abbreviation is: ",states['Michigan'])
print("Florida's abbreviation is: ",states['Florida'])

print('-' * 10)
print("Michigan has: ", Cities[states['Michigan']])
print("Florida has: ", Cities[states['Florida']])

print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")


print('-' * 10)
for abbrev, city in list(Cities.items()):
    print(f"{abbrev} has the city {city}")

print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {Cities[abbrev]}")

print('-' * 10)
state = states.get('Texas')

if not state:
    print("Sorry, no Texas.")

city=Cities.get('TX', 'Does Not Exist')
print(f"The city for the state 'TX' is: {city}")
