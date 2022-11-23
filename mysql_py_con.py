
import mysql.connector as c
import math as m
import csv
# Details for the connection between mysql and python 
mydb = c.connect(
  host = "localhost",
  user = "root",
  password = "",
  database = "automobile_details"
)
with open("data.csv",'r') as file:
  csvreader=csv.reader(file)
  amr_csv=list(csvreader)
  v=float(amr_csv[0][0])
  mile=float(amr_csv[0][1])
data=(v,)
mycursor = mydb.cursor()
q= "SELECT latitude,longitude FROM zip_info WHERE Zip_code=%s" 
mycursor.execute(q,data) 
result = mycursor.fetchone()
print (result)
# getting the latitude and longitude from zip code
latitude =[]
longitude = []
latitude.append(result[0])
longitude.append(result[1])

# calculate the new latitude, new longitude
meters = 1609*mile
earth = 6378.137
Pi = m.pi
n = (1 / ((2 * Pi / 360) * earth)) / 1000
new_latitude1 = round(result[0] + (meters * n),4)
new_latitude2 = round(result[0] - (meters * n),4)
cos = m.cos
new_longitude1 = round(result[1] + ((meters) * n) / cos(result[0] * (Pi / 180)),4)
new_longitude2 = round(result[1] - ((meters) * n) / cos(result[0] * (Pi / 180)),4)
print(new_latitude1,new_latitude2,new_longitude2,new_longitude1)
data1=(new_latitude1,new_latitude2, new_longitude2,new_longitude1)
# query for selecting the rows of zip within the latitude and longitude
q1= "SELECT vehicle_live_id, vin, make, model, year, amenities, price, miles FROM dealers dl INNER JOIN listing ls ON dl.dealer_number = ls.dealer_number INNER JOIN zip_info zi ON zi.Zip_code=ls.Zip_code WHERE %s >= latitude and latitude < %s and %s <= longitude and %s > longitude"

mycursor.execute(q1,data1) 
result2 = mycursor.fetchall()
print(result2)
