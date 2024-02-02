document.addEventListener('DOMContentLoaded', function () {
    var alertBox = document.getElementById('alertBox');
    alertBox.style.display = 'block';

    setTimeout(function () {
        alertBox.style.display = 'none';
    }, 6000); // Hide the alert after 3 seconds
});