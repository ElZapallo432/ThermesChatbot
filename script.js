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
                displayPrompt(userInput);
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
    responseElement.textContent = `> ${response}`; // Agrega el sufijo "> " antes del texto
    responseElement.style.color = 'white';
    responseElement.style.padding = '2px';
    responseElement.style.textAlign = 'left'; // Alinea el texto a la izquierda
    terminalInside.appendChild(responseElement);

    let index = 0;
    function typeWriter() {
        if (index < response.length) {
            responseElement.textContent += response.charAt(index);
            index++;
            setTimeout(typeWriter, 40); // Velocidad de escritura, ajusta según prefieras
        }
    }
    typeWriter();
}

function displayPrompt(input) {
    let terminalInside = document.querySelector('.terminal-inside');
    let responseElement = document.createElement('div')
    responseElement.textContent = `>>> ${input}`; // Agrega el sufijo ">>> " ant
    responseElement.style.color = 'white';
    responseElement.style.padding = '3px';
    responseElement.style.textAlign = 'left'; // Alinea el texto a la izquierda
    terminalInside.appendChild(responseElement);
}
