document.addEventListener("DOMContentLoaded", function () {
    const saveButton = document.getElementById("save-button");
    const searchInput = document.getElementById("search-input");
    const tableCells = document.querySelectorAll(".table tbody td[contenteditable='true']");
    let hasChanges = false;


    function trackChanges() {
        tableCells.forEach(function (cell) {
            cell.addEventListener("input", function () {
                hasChanges = true;
                saveButton.style.display = "block";
            });
        });
    }

    trackChanges();


    saveButton.addEventListener("click", function () {
        fetch("/save_button_click/") 
            .then(response => response.text())
            .then(data => {
                console.log(data); 
                saveButton.style.display = "none";
            })
            .catch(error => {
                console.error(error);
            });

        });


    searchInput.addEventListener("input", function () {
    });

    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== "") {
            const cookies = document.cookie.split(";");
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + "=")) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});
