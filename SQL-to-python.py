import mysql.connector
import pandas as pd

f = "C:/Users/Yi Ting/Desktop/CA2/Data/graduate-employment-survey-ntu-nus-sit-smu-suss-sutd.csv"
raw = pd.read_csv(f, header = 0, na_values=['-','NA', 'N/A', 'na'], encoding='latin-1')

cnx = mysql.connector.connect(user='root', password='1234', host='127.0.0.1', database='mydatabase') 

sql = "SELECT year,university, school, degree, basic_monthly_mean FROM grad_survey where basic_monthly_mean > 3800" 

df = pd.read_sql(sql, con = cnx)

print()
print('The following are the degrees that has a basic monthly mean salary of greater than $3,800.')
print(df)



