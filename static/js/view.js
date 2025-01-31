function renameButtons() {
    // Get all rows in the table body
    const rows = document.querySelectorAll("#TBody tr");

    // Iterate through each row
    rows.forEach(row => {
        // Get the status cell and button cell
        const statusCell = row.querySelector("td:nth-child(9)"); // 9th column is Status
        const buttonCell = row.querySelector("td:nth-child(11)"); // 11th column is Change Status

        // Get the status text
        const status = statusCell.textContent.trim();

        // Get the button element
        const button = buttonCell.querySelector("button");

        // Rename the button based on the status
        if (status === "Active") {
            button.textContent = "Deactivate";
        } else {
            button.textContent = "Activate";
        }
    });
}

// Call the function when the page loads
window.onload = renameButtons;


const csrftoken = getCookie('csrftoken');
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// document.addEventListener("DOMContentLoaded", function () {}

const statusButtons = document.getElementsByClassName('status');
for (let i = 0; i < statusButtons.length; i++) {
    statusButtons[i].addEventListener('click', function () {
        const recordId = statusButtons[i].getAttribute('id'); // Get the record ID
        console.log(recordId)
        if (confirm("Are you sure you want to change the status of the student with id: " + recordId)) {
            fetch(`/students/change_status/${recordId}/`, {  // Correct URL
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrftoken  // Ensure you have the CSRF token
                },
            })
            .then(function () {
                location.reload();  // Reload the page after change
            })
            .catch(error => {
                console.error('Error:', error);
            });
        }
    });
}
