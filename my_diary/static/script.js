var username = document.getElementById("username");
var password = document.getElementById("password");
var form = document.getElementById("form");

form.addEventListener("submit", function(evt) {
    evt.preventDefault();
    console.log(username.value)
});