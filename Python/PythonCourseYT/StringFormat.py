animal = "cow"
item = "moon"

print("the {} jumped over the {}".format(animal,item)) # old way
print(f"the {animal} jumped over the {item}") # new way
print("the {0} jumped over the {1}".format(animal,item)) # old way with index
print("the {animal} jumped over the {item}".format(animal="cow",item="moon")) # old way with keyword arguments")

text = "the {} jumped over the {}"
print(text.format(animal,item)) # old way with variable
print(f"{text} {animal} {item}") # new way with variable