import pandas
fil = pandas.read_csv("alpha.csv")
list = []
newlist = []
gh = {}
name = input(f"enter the word : ")
list[:0] = name.upper()
print(list)
for n in list:
   for (index, row) in fil.iterrows():
     if row.letter == n:
       sorted
       newlist.append(row.code)
       gh = newlist
print(gh)