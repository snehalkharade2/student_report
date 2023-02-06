import pickle
import json
import config3
import numpy as np

class Student_Success():
    def __init__(self,Marital_status,Application_mode,Application_order,Course,Daytime_evening_attendance,Previous_qualification,Nacionality,Mothers_qualification,Fathers_qualification,Mother_occupation,Father_occupation,Displaced,Educational_special_needs,Debtor,Tuition_fees,Gender,Scholarship_holder,Age_at_enrollment,International,Curricular_units_1st_sem_credited,Curricular_1st_sem_Enrolled,Curricular_units_1st_sem_evaluations,Curricular_units_1st_sem_approved,Curricular_unit_1st_sem_grade,Curricular_units_1st_sem_without_evaluations,Curricula_units_2nd_sem_credited,Curricular_units_2nd_sem_enrolled,Curricular_units_2nd_sem_evaluations,Curricular_units_2nd_sem_approved,Curricular_units_2nd_sem_grade,Curricular_units_2nd_sem_without_evaluations,Unemployment_rate,Inflation_rate,GDP):
        self.Marital_status = Marital_status
        self.Application_mode = Application_mode
        self.Application_order = Application_order
        self.Course = Course
        self.Daytime_evening_attendance = Daytime_evening_attendance
        self.Previous_qualification = Previous_qualification
        self.Nacionality = Nacionality
        self.Mothers_qualification = Mothers_qualification
        self.Fathers_qualification = Fathers_qualification
        self.Mother_occupation = Mother_occupation
        self.Father_occupation = Father_occupation
        self.Displaced = Displaced
        self.Educational_special_needs = Educational_special_needs
        self.Debtor = Debtor
        self.Tuition_fees = Tuition_fees
        self.Gender = Gender
        self.Scholarship_holder = Scholarship_holder
        self.Age_at_enrollment =Age_at_enrollment
        self.International = International
        self.Curricular_units_1st_sem_credited = Curricular_units_1st_sem_credited
        self.Curricular_1st_sem_Enrolled = Curricular_1st_sem_Enrolled
        self.Curricular_units_1st_sem_evaluations = Curricular_units_1st_sem_evaluations
        self.Curricular_units_1st_sem_approved = Curricular_units_1st_sem_approved
        self.Curricular_unit_1st_sem_grade = Curricular_unit_1st_sem_grade
        self.Curricular_units_1st_sem_without_evaluations = Curricular_units_1st_sem_without_evaluations
        self.Curricula_units_2nd_sem_credited = Curricula_units_2nd_sem_credited
        self.Curricular_units_2nd_sem_enrolled = Curricular_units_2nd_sem_enrolled
        self.Curricular_units_2nd_sem_evaluations = Curricular_units_2nd_sem_evaluations
        self.Curricular_units_2nd_sem_approved = Curricular_units_2nd_sem_approved
        self.Curricular_units_2nd_sem_grade = Curricular_units_2nd_sem_grade
        self.Curricular_units_2nd_sem_without_evaluations = Curricular_units_2nd_sem_without_evaluations
        self.Unemployment_rate = Unemployment_rate
        self.Inflation_rate = Inflation_rate
        self.GDP = GDP

    def __load_model(self):

        with open(r"artifacts\logistic_reg.pkl", "rb") as f:
            self.log_reg = pickle.load(f)
            print("Logistic Model ::", self.log_reg)

        with open(r"artifacts\project_data.json", "r") as f:
            self.project_data = json.load(f)
            print("Project Data ::",self.project_data)

        
    def get_student_prediction(self):
        self.__load_model()
        test_array = np.zeros((1,self.log_reg.n_features_in_))
        test_array[0][0] = self.Marital_status
        test_array[0][1] = self.Application_mode
        test_array[0][2] = self.Application_order
        test_array[0][3] = self.Course
        test_array[0][4] = self.Daytime_evening_attendance
        test_array[0][5] = self.Previous_qualification
        test_array[0][6] = self.Nacionality
        test_array[0][7] = self.Mothers_qualification
        test_array[0][8] = self.Fathers_qualification
        test_array[0][9] = self.Mother_occupation
        test_array[0][10] = self.Father_occupation
        test_array[0][11] = self.Displaced
        test_array[0][12] = self.Educational_special_needs
        test_array[0][13] = self.Debtor
        test_array[0][14] = self.Tuition_fees
        test_array[0][15] = self.Gender
        test_array[0][16] = self.Scholarship_holder
        test_array[0][17] = self.Age_at_enrollment
        test_array[0][18] = self.International
        test_array[0][19] = self.Curricular_units_1st_sem_credited
        test_array[0][20] = self.Curricular_1st_sem_Enrolled
        test_array[0][21] = self.Curricular_units_1st_sem_evaluations
        test_array[0][22] = self.Curricular_unit_1st_sem_grade
        test_array[0][23] = self.Curricular_units_1st_sem_without_evaluations
        test_array[0][24] = self.Curricula_units_2nd_sem_credited
        test_array[0][25] = self.Curricular_units_2nd_sem_enrolled
        test_array[0][26] = self.Curricular_units_2nd_sem_evaluations
        test_array[0][27] = self.Curricular_units_2nd_sem_approved
        test_array[0][28] = self.Curricular_units_2nd_sem_grade
        test_array[0][29] = self.Curricular_units_2nd_sem_without_evaluations
        test_array[0][30] = self.Unemployment_rate
        test_array[0][31] = self.Inflation_rate
        test_array[0][32] = self.GDP

        print("Test Array", test_array)

        progress_predict = self.log_reg.predict(test_array)[0]

        print("Progress of Student ::",progress_predict)

        return progress_predict



