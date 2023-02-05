from flask import Flask,render_template,request,jsonify
import config3
from utils3 import Student_Success
import traceback

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index3.html")

@app.route("/student_progress", methods = ["GET","POST"])
def student_progress():
    try:
        if request.method == "POST":
            data = request.form.get
            print("User Data is ::",data)

            Marital_status = eval(data("Marital_status"))
            Application_mode = eval(data("Application_mode"))
            Application_order = eval(data("Application_order"))
            Course = eval(data("Course"))
            Daytime_evening_attendance = int(data("Daytime_evening_attendance"))
            Previous_qualification = int(data("Previous_qualification"))
            Nacionality = int(data("Nacionality"))
            Mothers_qualification = eval(data("Mothers_qualification"))
            Fathers_qualification = eval(data("Fathers_qualification"))
            Mother_occupation = eval(data("Mother_occupation"))
            Father_occupation = eval(data("Father_occupation"))
            Displaced = eval(data("Displaced"))
            Educational_special_needs = eval(data("Educational_special_needs"))
            Debtor = eval(data("Debtor"))
            Tuition_fees = eval(data("Tuition_fees"))
            Gender = int(data("Gender"))
            Scholarship_holder = int(data("Scholarship_holder"))
            Age_at_enrollment = eval(data("Age_at_enrollment"))
            International = eval(data("International"))
            Curricular_units_1st_sem_credited = eval(data("Curricular_units_1st_sem_credited"))
            Curricular_1st_sem_Enrolled = eval(data("Curricular_1st_sem_Enrolled"))
            Curricular_units_1st_sem_evaluations = eval(data("Curricular_units_1st_sem_evaluations"))
            Curricular_units_1st_sem_approved = eval(data("Curricular_units_1st_sem_approved"))
            Curricular_unit_1st_sem_grade = eval(data("Curricular_unit_1st_sem_grade"))
            Curricular_units_1st_sem_without_evaluations = eval(data("Curricular_units_1st_sem_without_evaluations"))
            Curricula_units_2nd_sem_credited = eval(data("Curricula_units_2nd_sem_credited"))
            Curricular_units_2nd_sem_enrolled = eval(data("Curricular_units_2nd_sem_enrolled"))
            Curricular_units_2nd_sem_evaluations = eval(data("Curricular_units_2nd_sem_evaluations"))
            Curricular_units_2nd_sem_approved = eval(data("Curricular_units_2nd_sem_approved"))
            Curricular_units_2nd_sem_grade = eval(data("Curricular_units_2nd_sem_grade"))
            Curricular_units_2nd_sem_without_evaluations = eval(data("Curricular_units_2nd_sem_without_evaluations"))
            Unemployment_rate = eval(data("Unemployment_rate"))
            Inflation_rate = eval(data("Inflation_rate"))
            GDP = eval(data("GDP"))

            student_status = Student_Success(Marital_status,Application_mode,Application_order,Course,Daytime_evening_attendance,Previous_qualification,Nacionality,Mothers_qualification,Fathers_qualification,Mother_occupation,Father_occupation,Displaced,Educational_special_needs,Debtor,Tuition_fees,Gender,Scholarship_holder,Age_at_enrollment,International,Curricular_units_1st_sem_credited,Curricular_1st_sem_Enrolled,Curricular_units_1st_sem_evaluations,Curricular_units_1st_sem_approved,Curricular_unit_1st_sem_grade,Curricular_units_1st_sem_without_evaluations,Curricula_units_2nd_sem_credited,Curricular_units_2nd_sem_enrolled,Curricular_units_2nd_sem_evaluations,Curricular_units_2nd_sem_approved,Curricular_units_2nd_sem_grade,Curricular_units_2nd_sem_without_evaluations,Unemployment_rate,Inflation_rate,GDP)
            progress_student = student_status.get_student_prediction()

            if progress_student == 1:
                return render_template("index3.html", prediction = "Graduate")
            else:
                return render_template("index3.html", prediction = "Dropout")    
  
        else:
            data = request.args.get
            print("User Data is ::",data)

            Marital_status = eval(data("Marital_status"))
            Application_mode = eval(data("Application_mode"))
            Application_order = eval(data("Application_order"))
            Course = eval(data("Course"))
            Daytime_evening_attendance = int(data("Daytime_evening_attendance"))
            Previous_qualification = int(data("Previous_qualification"))
            Nacionality = int(data("Nacionality"))
            Mothers_qualification = eval(data("Mothers_qualification"))
            Fathers_qualification = eval(data("Fathers_qualification"))
            Mother_occupation = eval(data("Mother_occupation"))
            Father_occupation = eval(data("Father_occupation"))
            Displaced = eval(data(Displaced))
            Educational_special_needs = eval(data("Educational_special_needs"))
            Debtor = eval(data("Debtor"))
            Tuition_fees = eval(data("Tuition_fees"))
            Gender = int(data("Gender"))
            Scholarship_holder = int(data("Scholarship_holder"))
            Age_at_enrollment = eval(data("Age_at_enrollment"))
            International = eval(data("International"))
            Curricular_units_1st_sem_credited = eval(data("Curricular_units_1st_sem_credited"))
            Curricular_1st_sem_Enrolled = eval(data("Curricular_1st_sem_Enrolled"))
            Curricular_units_1st_sem_evaluations = eval(data("Curricular_units_1st_sem_evaluations"))
            Curricular_units_1st_sem_approved = eval(data("Curricular_units_1st_sem_approved"))
            Curricular_unit_1st_sem_grade = eval(data("Curricular_unit_1st_sem_grade"))
            Curricular_units_1st_sem_without_evaluations = eval(data("Curricular_units_1st_sem_without_evaluations"))
            Curricula_units_2nd_sem_credited = eval(data("Curricula_units_2nd_sem_credited"))
            Curricular_units_2nd_sem_enrolled = eval(data("Curricular_units_2nd_sem_enrolled"))
            Curricular_units_2nd_sem_evaluations = eval(data("Curricular_units_2nd_sem_evaluations"))
            Curricular_units_2nd_sem_approved = eval(data("Curricular_units_2nd_sem_approved"))
            Curricular_units_2nd_sem_grade = eval(data("Curricular_units_2nd_sem_grade"))
            Curricular_units_2nd_sem_without_evaluations = eval(data("Curricular_units_2nd_sem_without_evaluations"))
            Unemployment_rate = eval(data("Unemployment_rate"))
            Inflation_rate = eval(data("Inflation_rate"))
            GDP = eval(data("GDP"))

            student_status = Student_Success(Marital_status,Application_mode,Application_order,Course,Daytime_evening_attendance,Previous_qualification,Nacionality,Mothers_qualification,Fathers_qualification,Mother_occupation,Father_occupation,Displaced,Educational_special_needs,Debtor,Tuition_fees,Gender,Scholarship_holder,Age_at_enrollment,International,Curricular_units_1st_sem_credited,Curricular_1st_sem_Enrolled,Curricular_units_1st_sem_evaluations,Curricular_units_1st_sem_approved,Curricular_unit_1st_sem_grade,Curricular_units_1st_sem_without_evaluations,Curricula_units_2nd_sem_credited,Curricular_units_2nd_sem_enrolled,Curricular_units_2nd_sem_evaluations,Curricular_units_2nd_sem_approved,Curricular_units_2nd_sem_grade,Curricular_units_2nd_sem_without_evaluations,Unemployment_rate,Inflation_rate,GDP)
            progress_student = student_status.get_student_prediction()

            if progress_student == 1:
                return render_template("index3.html", prediction = "Graduate")
            else:
                return render_template("index3.html", prediction = "Dropout")  

    except:
        print(traceback.print_exc())
        return jsonify({"Message" : "Unsuccessful"}) 

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = config3.PORT_NUMBER, debug = False)


          
  

