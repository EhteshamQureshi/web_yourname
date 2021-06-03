
menuFile = "demofile.txt"
with open(menuFile, 'r') as file:
    menu = file.read()
    print(menu)


marksFile = 'marks.txt'

#data = {"IY468":{"P12345":{"name": "Ali", "marks": 90}, "P23765":{"name": "Sam", "marks": 80}, "P54544": {"name": "Saly", "marks": 40}}}
data = {}
firstLine = True
with open(marksFile, 'r') as file:
    for line in file:
        if firstLine:
            firstLine = False
            pass
        else:
            moduleCode, ID, name, marks = line.split(',')
            if moduleCode not in data.keys():
                data[moduleCode] = {ID:{"name":name, "marks": marks}}
            else:
                data[moduleCode][ID] = {"name":name, "marks":marks}
selectedOption = input("Choose option: ")
while selectedOption not in "123":
    selectedOption = input("Please choose valid option ")
if selectedOption == "1":
    moduleCode = input("Enter Module Name: ")
    if moduleCode not in data.keys():
        print("module code doesn't exist")
    else:
        avg = 0.0
        counter = 0
        for v in data[moduleCode].values():
            avg += float(v['marks'])
            counter += 1
        avg = avg/counter
        print("Average marks of module with code ", moduleCode, " are : ", round(avg,2))
elif selectedOption == "2":
    studentID = input("Enter Student ID: ")
    if studentID not in data[list(data.keys())[0]].keys():
        print("student with this id doesn't exist")
    else:
        avg = 0.0
        counter = 0
        for k in data.keys():
            avg += float(data[k][studentID]['marks'])
            counter+=1
        avg = avg/counter
        print("Average marks of student with id ", studentID," are : ",round(avg,2))
elif selectedOption == "3":
    studentName = input("Enter Student Name: ").lower()
    if studentName not in [name['name'].lower() for name in data[list(data.keys())[0]].values()]:
        print("student with this name doesn't exist")
    else:
        avg = 0.0
        counter = 0
        for v in data.values():
            for vv in v.values():
                if vv['name'].lower() == studentName:
                    avg += float(vv['marks'])
                    counter += 1
        avg = avg/counter
        print("Avergae marks of ", studentName, " are : ", round(avg,2))
        
    
