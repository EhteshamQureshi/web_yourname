"""
This file can read any number of student records from Student.txt and create seperate .txt file for each student
and add marks of all the subjects of that student print as Total.
input: template.txt,Student.txt
ex:  template.txt:( you can change the order of columns)
     std_id,std_name,marks,subject
     Student.txt:
     std_id,std_name,subject,marks
     101,Santosh,Maths,35
     102,Hina,English,41
     101,Santosh,Hindi,30
output: prints Total marks of the students on output screen and creates seperate .txt file for each students
     
"""

from collections import defaultdict

temp_dict_list=[]
actual_dict_list=[]
marks_list=[]
std_names_list=[]
file_names_list=[]
std_id_list=[]

fd=open(r"./template.txt","r")
header=fd.readlines()
header_format=header[0].split(",")
fd.close()

fd=open("./Student.txt","r")
string=fd.readlines()
temp_header=string[0].split(",")
temp_header[3]=temp_header[3].strip()
len_std_record=len(string)
fd.close()

student=[]
for i in range(1,len_std_record):
    student.append(string[i][:-1].split(","))

for i in range(len(student)):
    temp_dict_list.append(dict(zip(temp_header,student[i])))
    actual_dict_list.append({item:temp_dict_list[i][item] for item in header_format})
    file_names_list.append(actual_dict_list[i]["std_name"]+"."+actual_dict_list[i]["std_id"]+".txt")
    marks_list.append(actual_dict_list[i]["marks"])
    std_names_list.append(actual_dict_list[i]["std_name"])
    std_id_list.append(actual_dict_list[i]["std_id"])

n=len(actual_dict_list)

'''
######################################################################
creating student.id.txt file by grouping relevent student records
ex: santosh.101.txt
    {'std_id': '101', 'std_name': 'Santosh', 'marks': '35', 'subject': 'Maths'}
    {'std_id': '101', 'std_name': 'Santosh', 'marks': '30', 'subject': 'Hindi'}
    {'std_id': '101', 'std_name': 'Santosh', 'marks': '90', 'subject': 'Science'}
    
######################################################################
'''
for i in range(n):
    for j in range(n):
        if i is not j :
            if actual_dict_list[i]["std_id"]==actual_dict_list[j]["std_id"]:                
                with open("%s"%file_names_list[i],"a+") as fo:
                    fo.seek(0,0)
                    if str(actual_dict_list[i]["subject"]) not in fo.read():
                        fo.write(str(actual_dict_list[i]))
                        fo.write("\n")
                        fo.close()
            else:
                with open("%s"%file_names_list[j],"a+") as fo:
                    fo.seek(0,0)
                    if str(actual_dict_list[j]["subject"]) not in fo.read():
                        fo.write(str(actual_dict_list[j]))
                        fo.write("\n")
                        fo.close()

'''
##################################################################################
Calculating Total Marks of students in all the subjects and appending to the file
##################################################################################
'''
res = [(i, j) for i, j in zip(std_id_list, marks_list)]
id_names=dict(zip(std_id_list,std_names_list))
id_marks=defaultdict(list)

for std_id,mark in res:
    id_marks[std_id].append(mark)

for std_id,name in id_names.items():
    for key in id_marks:
        if std_id==key:
            with open("%s.%d.txt" %(name,int(std_id)),"a+") as fo:
                Total=0                
                for i in range(len(id_marks[key])):
                    Total+=int(id_marks[key][i])
                fo.write("Total:"+str(Total))
                print("Total Marks of "+id_names[key]+":"+str(Total))
                fo.close()