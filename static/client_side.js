let div = document.getElementById("timestamp");

fetch("/timestamp")
    .then(response => response.text())
    .then(text => div.innerText = text);
