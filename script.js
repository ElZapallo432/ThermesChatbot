document.getElementById("input").addEventListener("keypress", function(event) {
    if (event.key === "Enter") {
        let userInput = event.target.value;
        
        // Desactivar el input para evitar más entradas mientras se procesa
        event.target.disabled = true;
        
        fetch('http://localhost:5000/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ message: userInput })
        })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                displayResponse("Error: " + data.error);
            } else {
                displayResponse(data.response);
            }
        })
        .catch(error => {
            displayResponse("Network error: " + error.message);
        })
        .finally(() => {
            // Reactivar el input para permitir nuevas entradas
            document.getElementById("input").disabled = false;
            document.getElementById("input").value = "";  // Limpiar el campo de entrada
        });
    }
});

function displayResponse(response) {
    let terminalInside = document.querySelector('.terminal-inside');
    let responseElement = document.createElement('p');
    responseElement.textContent = response;
    responseElement.style.color = 'white';
    terminalInside.appendChild(responseElement);
}
