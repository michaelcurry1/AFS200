csv = 'Eric,John,Michael,Terry,Graham:TerryG;Brian'
print(csv)

# split on the comma
name1 = csv.split(',')
print(name1)

# adding the comma seperated items (first 4 items) to friends1
friends1 = name1[:4]
print(friends1)

# add the remaining items to friends2
friends2 = name1[4]
print(friends2)

#split remaining items on the colon
name2 = friends2.split(':')
print(name2)

# appending grahm to friends 1
friends1.append(name2[0])
print(friends1)

#split remaining items on semi colon
friends3 = name2[1].split(';')
print(friends3)

#add remaining items to friends1
for item in friends3:
    friends1.append(item)

print(friends1)

