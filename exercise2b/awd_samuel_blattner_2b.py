import csv
##
##file = open('je-d-16.02.01.08.csv', 'r')
##daten = file.readlines()
##for i in daten:
##    print(i)
##file.close()

reader = csv.reader(open("Liste.csv", "r"), delimiter=';')
for row in reader:
    print(row)
print(reader)[0][0]

##def entfernen(liste):
##    ergebnis = []
##    for i in liste:
##        a = i.replace('
##
##
### Liste à la: daten[0][1]
