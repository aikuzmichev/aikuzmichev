from datetime import datetime
import requests

data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
current_datetime = datetime.today().date()
  
  print()
  print("This program converts US dollars to Russian ruble")
  print ("USD exchange rate for today", current_datetime, ":", data['Valute']['USD']['Value'], "₽")
  print() 

  dollars = eval(input("Enter amount in dollars: "))
  print() 

  convert_to_ruble = dollars * data['Valute']['USD']['Value']
  print("That is" , convert_to_ruble, "₽ today")
