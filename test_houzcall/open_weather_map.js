// use api from https://api.openweathermap.org/data/2.5/forecast?q=jakarta&appid=dc5f27a9e8edb94bb568711aa0b4617e to display the output in the form of a weather forecast for the city of Jakarta for the next 5 days
// the output should be dat, date, and temperature for the weather forecast for the city of jakarta for the next 5 days

let url = 'https://api.openweathermap.org/data/2.5/forecast?q=jakarta&appid=dc5f27a9e8edb94bb568711aa0b4617e'
// console log the output should be dat, date, and temperature for the weather forecast for the city of jakarta for the next 5 days


// get data from url then console.log
fetch(url)
  .then(response => response.json())
  .then(data => {
    console.log(data)
  }
)