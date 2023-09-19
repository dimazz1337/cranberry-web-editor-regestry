document.addEventListener("DOMContentLoaded", function () {
    const searchButton = document.getElementById("search-button");

    searchButton.addEventListener("click", function () {
        fetch("/search_button_click/") 
            .then(response => response.text())
            .then(data => {
                console.log(data); 
            })
            .catch(error => {
                console.error(error);
            });
    });
});