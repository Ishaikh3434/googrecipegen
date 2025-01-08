const path = document.getElementById('data-container').getAttribute('host-path');
const togglebutton = document.getElementById('micButton');
const saveOptions = document.getElementById('saveOptions');
console.log(path);

document.getElementById('generateButton').addEventListener('click', async () => {
    const inputText = document.getElementById('inputField').value;

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
        console.log("this should display");
        saveOptions.style.display="inline"
    } catch (error) {
        console.error('Error:', error);
    }
    
});
    // Initialize Save to Google Drive functionality
    initGoogleDriveSave();




// Initialize Google Drive Save button
function initGoogleDriveSave() {
    const saveToDriveDiv = document.getElementById('saveToDrive');
    saveToDriveDiv.innerHTML = ''; // Clear any existing buttons

    const publicBlobURL = createBlobURL();
    saveToDriveDiv.innerHTML = `
        <div class="g-savetodrive"
            data-src="${publicBlobURL}"
            data-filename="recipe.pdf"
            data-sitename="Qook">
        </div>`;
    if (window.gapi && gapi.savetodrive) {
        gapi.savetodrive.render(saveToDriveDiv); // Render the Drive button
    }
}

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
        recognition.interimResults = true; // Allow interim results
        recognition.maxAlternatives = 1;
        recognition.continuous = true; // Keep recognition active after pauses

        recognition.onstart = () => {
            isRecognizing = true;
            console.log('Speech recognition started.');
        };

        recognition.onresult = (event) => {
            const speechResult = event.results[0][0].transcript;
            document.getElementById('inputField').value = speechResult;
            console.log(speechResult);
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
