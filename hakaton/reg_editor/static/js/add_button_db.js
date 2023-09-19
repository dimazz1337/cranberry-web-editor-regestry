document.addEventListener("DOMContentLoaded", function () {
    const addButton = document.getElementById("add-button");

    addButton.addEventListener("click", function () {
        fetch("/add_button_click/") 
            .then(response => response.text())
            .then(data => {
                console.log(data); 
            })
            .catch(error => {
                console.error(error);
            });
    });
});