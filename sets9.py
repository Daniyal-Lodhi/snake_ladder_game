dog=[]
for i in range(83):
    dog.append(i)
s_dog=set(dog)
print(s_dog)
cat=[]
for i in range(101):
    cat.append(i)
s_cat=set(cat)
print(s_cat)
fish=[]
for i in range(22):
    fish.append(i)
s_fish=set(fish)
print(s_fish)
dogcat=[]
for i in range(31):
    dogcat.append(i)
dogcat_s=set(dogcat)
print(dogcat_s)
dogfish=[]
for i in range(8):
    dogfish.append(i)
dogfish_s=set(dogfish)
print(dogfish_s)
dogcatfish_s={0,1,2,3,4,5}
print(dogcatfish_s)
catorfish=[]
for i in range(8):
    catorfish.append(i)
catorfish_s=set(catorfish)
print(catorfish_s)
s_catfish={0,1,2,3,4,5,6,7,8,9}
print(s_catfish)
print(len(s_dog))
print(len(s_cat))
print(len(dogfish_s))