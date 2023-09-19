document.addEventListener("DOMContentLoaded", function () {
    const deleteButtons = document.querySelectorAll(".delete-button");

    deleteButtons.forEach(function (button) {
        button.addEventListener("click", function () {

            const row = button.closest("tr");
            const csrftoken = getCookie("csrftoken");
            const id = row.querySelector("td:nth-child(1)").textContent;
            const uid = row.querySelector("td:nth-child(2)").textContent;

            fetch("/del_button_click/", {
                method: "POST",  

                body: JSON.stringify({ id, uid }),
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": csrftoken   

                }
            })
            .then(response => response.text())
            .then(data => {
                console.log(data);
            })
            .catch(error => {
                console.error(error);
            });
        });
    });
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
