import requests
import datetime
url = f"http://api.openweathermap.org/data/2.5/forecast?q=jakarta&appid=dc5f27a9e8edb94bb568711aa0b4617e"

data = requests.get(url)
cuaca = data.json()

print('Weather Forecast: ')
# looping
for i in range(0, len(cuaca['list'])):
  # if "dt_txt" in cuaca = 12:00:00
  if "12:00:00" in cuaca['list'][i]['dt_txt']:
    suhu = f"{(cuaca['list'][i]['main']['temp']) - 273.15:.2f}"
    tahun = f"{cuaca['list'][i]['dt_txt'][0:4]}"
    tanggal_hari = f"{cuaca['list'][i]['dt_txt'][8:10]}"
    bulan = f"{cuaca['list'][i]['dt_txt'][5:7]}"
    
    x = datetime.datetime(int(tahun), int(bulan), int(tanggal_hari) )
    hari = x.strftime("%A")
    
    
    if bulan == "01":
      bulan = "Jan"
    elif bulan == "02":
      bulan = "Feb"
    elif bulan == "03":
      bulan = "Mar"
    elif bulan == "04":
      bulan = "Apr"
    elif bulan == "05":
      bulan = "May"
    elif bulan == "06":
      bulan = "Jun"
    elif bulan == "07":
      bulan = "Jul"
    elif bulan == "08":
      bulan = "Aug"
    elif bulan == "09":
      bulan = "Sep"
    elif bulan == "10":
      bulan = "Oct"
    elif bulan == "11":
      bulan = "Nov"
    elif bulan == "12":
      bulan = "Dec"
      
    
    print(f"{hari[0:3]}, {tanggal_hari} {bulan} {tahun}: {suhu}°C")
    
