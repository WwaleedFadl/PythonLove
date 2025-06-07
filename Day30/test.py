#with open('a_file.txt') as file: 
#    file.read()

'''
try:
    file = open("a_file.txt")
    a_dictionary = {"Key" : "Value"} 
    #print(a_dictionary['s'])

except FileNotFoundError: 
    file = open('a_file.txt','w')
    file.write("Text for now")

except KeyError as error_message: 
    print("That key is not exist: ",error_message)

else: 
    content=file.read()
    print(content)
    #print("Sorry we do not understand this one")
finally: 
    print("Done for now")
    raise TypeError("Made UP")
height = float(input("Height: "))
weight = int(input("Weight: "))


if(height > 3): 
    raise ValueError("Human height should not be over 3m")
bmi = weight / (height ** 2)

print(bmi)

fruits =  [ "Apple","Pear","Orange"]

def make_pie(index):
    try: 
        fruit = fruits[index]
    except IndexError: 
        print("Fruit Pie")
        print("Out of Index")
    else: 
        print(fruit + " Pie")

make_pie(3)

'''

facebook_posts = [
    {"Likes":21,"Comments":2},
    {"Likes":13,"Comments":2,"Shares":1},
    {"Likes":33,"Comments":8,"Shares":8},
    {"Comments":4,"Shares":2},
    {"Comments":1,"Shares":1},
    {"Likes":19,"Comments":3},
]

total_likes = 0 

for post in facebook_posts:
    try:
        total_likes = total_likes + post["Likes"]
    except KeyError: 
        print("Hey i'm facing a key error")
    else: 
        print(f"Total Likes are : {total_likes} ")
    




































