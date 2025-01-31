const nav = document.querySelector('nav');
const toggle_btn = document.getElementById('toggle-btn');
const smallTap = document.querySelector('.smallTap');
const divcon = document.querySelector('.content');
const procon = document.querySelector('.projects');
const partcon = document.querySelector('.part');
const MEC = document.querySelector('.marginedited');

toggle_btn.onclick = function() {
    nav.classList.toggle('hide');
    if (partcon) partcon.classList.toggle('expand');
    if (smallTap) smallTap.classList.toggle('expand');
    if (procon) procon.classList.toggle('expand');
    if (MEC) MEC.classList.toggle('expand');
    if (divcon) divcon.classList.toggle('expand');
};

function toggleMode() {
    var icon = document.getElementById("bgModeIcon");
    var body = document.body;
    
    if (body.classList.contains("light-mode")) {
        body.classList.remove("light-mode");
        icon.classList.remove("fa-moon");
        icon.classList.add("fa-sun");
    } else {
        body.classList.add("light-mode");
        icon.classList.remove("fa-sun");
        icon.classList.add("fa-moon");
    }
    body.classList.toggle("dark-mode");
}

document.getElementById("bgModeBtn").addEventListener("click", toggleMode);

// Prevent form submission
document.getElementById('submit').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the form from submitting
    // Add your search logic here
    console.log('Search button clicked');
    // You can access the search input value like this:
    const searchValue = document.getElementById('Search').value;
    console.log('Search value:', searchValue);
});