#Libraries imported
from bs4 import BeautifulSoup  #“Beautiful Soup” is used to extract data from websites, Html, and XML pages.
import smtplib                  #“Requests” library is used to send HTTP requests 
import requests as rq           #“smtplib” is used to send emails to any machine.

#Getting Weather Data

url = rq.get('https://forecast.weather.gov/MapClick.php?lat=40.71455000000003&lon=-74.00713999999994')

soup = BeautifulSoup(url.text, 'html.parser')

weather = (soup.select('#current_conditions-summary p')[0]).text
temperature = (soup.select('#current_conditions-summary p')[1]).text

#Building smtplib object
server = smtplib.SMTP('smtp.gmail.com', 587)
print(server.ehlo())
print(server.starttls())

server.login('Enter your email', 'Password')

#Sending email
if weather == 'Raining' or weather == 'Overcast' :

    subject = "Umbrella Reminder"
    body = f"Take an umbrella with you. Weather condition for today is {weather} and temperature is {temperature} in New York."

    msg = f"Subject:{subject}\n\n{body}\n\nRegards,\nVishal".encode('utf-8')
    print(msg)

    server.sendmail('Sender's Email', 'Recipient Email', msg)

    print("Email Sent!")

    server.quit()
else :
    print("There is going to be {} and temperature is {} in New York".format(weather, temperature))

    
