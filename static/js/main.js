const opennav = document.getElementById('opennav');
const closenav = document.getElementById('closebar')
function openBar() {
  document.getElementById('nav').style.display = "flex";
  opennav.style.display = "none";
  closenav.style.display = "block";

}

function closeBar() {
  document.getElementById('nav').style.display = "none";
  closenav.style.display = "none";
  opennav.style.display = "block";

}


function ctaAction() {
    alert("Welcome to Ezydevs Studio! Let's build your dream website.");
}

function getStarted() {
    alert('Redirecting to the signup page...');
    // Here you can redirect to your signup or registration page
    window.location.href = '/signup';
}


// List of words you want to rotate
const texts = ["Emails", "Sites", "Projects", "Blogs"];

// Get the element where the text should change
const dynamicText = document.getElementById("dynamic-text");

let index = 0;

// Function to change the text
function changeText() {
    dynamicText.textContent = texts[index];
    index = (index + 1) % texts.length; // Loop through the array
}

// Set interval to change text every 3 seconds (3000 milliseconds)
setInterval(changeText, 3000);
