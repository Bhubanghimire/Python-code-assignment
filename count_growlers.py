def count_growlers(animals):
    count = 0
    dog=animals.count("dog")
    god = animals.count("god")
    cat = animals.count("cat")
    tac= animals.count("tac")
    print(dog)
    print(cat)
    print(god)
    print(tac)
    if dog != cat:
        count += abs(dog-cat)
    if god != tac:
        count += abs(god-tac) 
    return count


animals = ['dog', 'cat', 'dog',
 'god', 'dog', 'god',
  'dog', 'god','dog',
   'dog', 'god', 'god',
    'cat', 'dog', 'god',
     'cat','tac']

result = count_growlers(animals)
print(result)