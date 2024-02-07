function sendMessage() {
    const messageInput = document.getElementById('messageInput').value;

    // Send the message input to the sentiment analysis route
    fetch('/analyze_sentiment', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ "content": messageInput }),
    })
    .then(response => response.json())
    .then(data => {
        const responseElement = document.getElementById('response');
        responseElement.innerHTML = data.sentiment;

        // Change the color of the response element based on sentiment
        if (data.sentiment === "Positive") {
            responseElement.style.color = 'green';
        } else if (data.sentiment === "Negative"){
            responseElement.style.color = 'red';
        } else {
            responseElement.style.color = 'white';
        }
    })
    .catch(error => {
        console.error('An error occurred:', error);
    });
}

function autoResize() {
    const textarea = document.getElementById('messageInput');
    textarea.style.height = 'auto'; // Reset the height to recalculate correctly

    // Set the height of the textarea based on content and scroll height
    textarea.style.height = textarea.scrollHeight + 'px';
}
