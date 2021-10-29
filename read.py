
##Get the file that the notes are located in 
file=input("what file are you looking for? ")

fread=open(file)
lines = fread.readlines()

#search the lines for the keyword 
keyword = input("Search keyword: ")

for line in lines:
    search = line.find(keyword)

    if keyword in line:
        print(line)
 

    

