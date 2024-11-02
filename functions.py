#functions they are used to perform a specific task(method 2)
#you define the function def and its followed with the function_name():
# parameters: is the data or informations passed through the function to perform a particular task(variables)
#arguments:are the values
#function call:to call a function with the function name and we call the function out of the function body

#create a function that returns the main components of a functions

def functionBasics():
    print(f"the mainComponents of a function are {functionBasics}")
functionBasics()

#create a function the returns your student_name student_number and student_age 
def studentDetails():
    student_name = 'leticia'
    student_number = '2024\dsc\0010\ss'
    student_age = '22'
    print(f" the student details is {student_name} and {student_number} and { student_age}")
    print(f"am{student_number} with student reg no{student_number} and am{student_age}")

#local variables  are crrate within the function

# create a function that returns your student_name, student_reg_number , student_age  as parameters
def studentsDetailsParam( name,age,regNo):
    print(f"{name}, {age},{regNo}")
    studentsDetailsParam("leticia" ,"22" " 2024\dcs\0010\ss") #calling the functions

    #return values
    def myName():
        name ="leticia"
        return name
    myName()
    
    def myNamepara(name):
        return name
    myNamepara('leticia')
     

