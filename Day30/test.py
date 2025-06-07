#with open('a_file.txt') as file: 
#    file.read()

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
