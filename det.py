import json
user_dict = {}
i=0
num_entries = int(input("Enter the number of entries you want to add: "))
for i in range(num_entries):
    key = input("Enter Roll number: ")
    value = input("Enter Name: ")
    user_dict[key] = value
    #Add to the file
with open('C:/PY/details.txt', 'w') as convert_file: 
     convert_file.write(json.dumps( user_dict))
    
    #Read from file
with open('C:/PY/details.txt', 'r') as file:
    # read lines from the file
    lines = file.readlines()
    
# initialize an empty dictionary
res = {}

# iterate through each line and split key-value pairs
#for line in lines:
    #key,value = line.strip().split(':')
    d = dict(s.split(':') for s in line)
    	res[key.strip()] = value.strip()

#student_details = json.loads(jsonString)
num_entries1 = int(input("Enter the number of Roll number you want to search ")) 
searchItems=[]
j=0
for j in range(num_entries1):
    key1 = input("Enter Roll number: ")
    searchItems.append(key1)
print("----The Result---")
for key, value in res.items():
        if key in searchItems:
            print(key,value)
