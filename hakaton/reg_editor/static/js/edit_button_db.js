document.addEventListener("DOMContentLoaded", function () {
    const editButton = document.getElementById("edit-button");

    editButton.addEventListener("click", function () {
        fetch("/edit_button_click/") 
            .then(response => response.text())
            .then(data => {
                console.log(data); 
            })
            .catch(error => {
                console.error(error);
            });
    });
});