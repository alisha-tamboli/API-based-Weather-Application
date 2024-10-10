document.querySelector('form').onSubmit = async function (e) {
    e.preventDefault();

    const city = document.querySelector('input[name = "city"]').value;
    const response = await fetch('/weather/${city}');
    const data = await response.json();

    if(data.error) {
        document.querySelector('#weather-result').innerHTML = '<p style = "color : red; ">${data.error}</p>';
    }
    else {
    document.querySelector('#weather-result').innerHTML = `
        <h2>Weather in ${data.name}:</h2>
        <p>Temperature: ${data.main.temp}°C</p>
        <p>Weather: ${data.weather[0].description}</p>
        <p>Humidity: ${data.main.humidity}%</p>
        <p>Wind Speed: ${data.wind.speed} m/s</p>`;
}
};