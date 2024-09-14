"""Dictonary"""

Dict={
    "name" : "Prianka",
    "Age": "27",
    "CGPA" : "3.95",
}
print(Dict)
Dict["name"] = "Purba"
Dict[3] = 23
print(Dict)

"""Null Dictonary"""

null_dict = {} #just make a dictonary and add value afterward
null_dict["name"] = "Prianka"
print(null_dict)

Student = {
    "NAME" : "PURBA",
    "subjects" :{
        "phy" : 67,
        "chem" : 76,
    }
}
print(Student)
print(Student ["subjects"]["chem"]) #find out a specific info