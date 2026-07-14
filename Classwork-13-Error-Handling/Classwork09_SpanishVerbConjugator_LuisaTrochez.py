pronouns = ['Yo', 'Tu', 'El', 'Nosotros', 'Vosotros', 'Ellos']
 
endings = {
    'ar': ['o', 'as', 'a', 'amos', 'ais', 'an'],
    'er': ['o', 'es', 'e', 'emos', 'eis', 'en'],
    'ir': ['o', 'es', 'e', 'imos', 'is', 'en']
}
 
verb = input("Write a spanish verb (ar/er/ir): ")
 
stem = verb[:-2]
ending = verb[-2:]
 
conjugations = endings[ending]
 
for index,pronoun in enumerate(pronouns):
    print(f"{pronoun} {stem}{conjugations[index]}")
    
    
    

#⊹₊˚‧︵‿₊୨ᰔ୧₊‿︵‧˚₊⊹⊹₊˚‧︵‿₊୨ᰔ୧₊‿︵‧˚₊⊹⊹₊˚‧︵‿₊୨ᰔ୧₊‿︵‧˚₊⊹⊹₊˚‧︵‿₊୨ᰔ୧₊‿︵‧˚₊⊹⊹₊˚‧︵‿₊୨ᰔ୧₊‿︵‧˚₊⊹⊹₊˚‧︵‿₊୨ᰔ୧₊‿︵‧˚₊⊹⊹₊˚‧︵‿₊୨ᰔ୧₊‿︵‧˚₊⊹

                                                      #CLASSW 09 -ERROR HANDLING
    

pronouns = ['Yo', 'Tú', 'Él', 'Nosotros', 'Vosotros', 'Ellos']

endings = {
    'ar': ['o', 'as', 'a', 'amos', 'ais', 'an'],
    'er': ['o', 'es', 'e', 'emos', 'eis', 'en'],
    'ir': ['o', 'es', 'e', 'imos', 'is', 'en']
}

verb = input("Write a spanish verb (ar/er/ir): ")

if " " in verb:
    print("El verbo no debe tener espacios extra")

elif verb != verb.lower():
    print("El verbo debe escribirse en minúsculas")

else:
    stem = verb[:-2]
    ending = verb[-2:]

    try:
        conjugations = endings[ending]
        for index, pronoun in enumerate(pronouns):
            print(f"{pronoun} {stem}{conjugations[index]}")
    except KeyError:
        print("El verbo debe terminar en ar, er o ir")
        