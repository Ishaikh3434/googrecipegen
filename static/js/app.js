const path = document.getElementById('data-container').getAttribute('host-path');
console.log(path)
document.getElementById('generateButton').addEventListener('click', async () => {
    const inputText = document.getElementById('inputField').value;
    
    try {
        const response = await fetch(path, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ inputText })
        });

        const data = await response.json();
        document.getElementById('outputContainer').innerHTML = data.outputText;
    } catch (error) {
        console.error('Error:', error);
    }
});

// Microphone input handling
let recognition; // Declare the recognition object in the outer scope
let isRecognizing = false; // Flag to track recognition state

document.getElementById('micButton').addEventListener('click', () => {
    if (!('webkitSpeechRecognition' in window) && !('SpeechRecognition' in window)) {
        alert('Speech Recognition API not supported in this browser.');
        return;
    }

    recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
    recognition.lang = 'en-US';
    recognition.interimResults = true;  // Allow interim results
    recognition.maxAlternatives = 1;
    recognition.continuous = true; // Keep recognition active after pauses

    recognition.onstart = () => {
        isRecognizing = true; // Set flag when recognition starts
        console.log('Speech recognition started.');
    };

    recognition.onresult = (event) => {
        const speechResult = event.results[0][0].transcript;
        document.getElementById('inputField').value = speechResult;
    };

    recognition.onerror = (event) => {
        console.error('Speech recognition error:', event.error);
        alert('Speech recognition error: ' + event.error);
    };

    recognition.onend = () => {
        isRecognizing = false; // Reset flag when recognition stops
        console.log('Speech recognition ended.');
    };

    if (!isRecognizing) {
        recognition.start(); // Start recognition if not already started
    }
});

// Stop recognition on button click
document.getElementById('stopButton').addEventListener('click', () => {
    if (recognition && isRecognizing) {
        recognition.stop(); // Stop the recognition process
        console.log('Speech recognition stopped.');
    }
});