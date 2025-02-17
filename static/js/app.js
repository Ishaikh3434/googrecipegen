const path = document.getElementById('data-container').getAttribute('host-path');
const togglebutton = document.getElementById('micButton');
const saveOptions = document.getElementById('saveOptions');
console.log(path);



document.getElementById('generateButton').addEventListener('click', async () => {
    const inputText = (document.getElementById('recipeName').value+': '+document.getElementById('inputField').value);

    try {
        const response = await fetch(path, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ inputText }),
        });

        const data = await response.json();
        const outputContainer = document.getElementById('outputContainer');
        outputContainer.innerHTML = data.outputText;

        // Add Save options once content is generated
        console.log("hwhatya lookin at?");
        saveOptions.style.display="inline"
    } catch (error) {
        console.error('Error:', error);
    }

});



// Create a Blob URL for the recipe content
function createBlobURL() {
    const content = document.getElementById('outputContainer').innerText;
    const blob = new Blob([content], { type: 'application/pdf' });
    return URL.createObjectURL(blob);
}

// Microphone input handling (unchanged)
let recognition; // Declare the recognition object in the outer scope
let isRecognizing = false; // Flag to track recognition state

togglebutton.addEventListener('click', () => {
    if (!('webkitSpeechRecognition' in window) && !('SpeechRecognition' in window)) {
        alert('Speech Recognition API not supported in this browser.');
        return;
    }

    if (!recognition) {
        recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
        recognition.lang = 'en-US';
        recognition.interimResults = false; // Allow interim results
        recognition.maxAlternatives = 1;
        recognition.continuous = true; // Keep recognition active after pauses

        recognition.onstart = () => {
            isRecognizing = true;
            console.log('Speech recognition started.');
        };

        recognition.onresult = (event) => {
            var speechResult = event.results[event.results.length-1][0].transcript;
            document.getElementById('inputField').value += speechResult;
            speechResult = ''
        };

        recognition.onerror = (event) => {
            console.error('Speech recognition error:', event.error);
            alert('Speech recognition error: ' + event.error);
            togglebutton.classList.remove('on');
            togglebutton.classList.add('off');
            togglebutton.textContent = '🎤';
        };

        recognition.onend = () => {
            isRecognizing = false;
            console.log('Speech recognition ended.');
        };
    }

    if (isRecognizing) {
        // Stop recognition
        recognition.stop();
        togglebutton.classList.remove('on');
        togglebutton.classList.add('off');
        togglebutton.textContent = '🎤';
    } else {
        // Start recognition
        recognition.start();
        togglebutton.classList.remove('off');
        togglebutton.classList.add('on');
        togglebutton.textContent = '🟥';
    }
});
