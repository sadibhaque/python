def name(first, last):
    full = f"{first} {last}"
    return full

# full_name = name('Jhon','Mendax')
full_name = name(last='Mendax', first='Jhon')

print(full_name)



def famous(first, last, **extra):
    name = f'{first} {last}'
    print(extra)
    return name

full_name = famous('Sadib', 'Sahib', k = 'CEO')     # k is a key 

print(full_name)