#VTT Script

import vosk
import pyaudio
import json
import time

class voiceToText:
    def __init__(self):
        # Initialize the model
        model = vosk.Model("vosk-model-small-en-us-0.15")
        self.rec = vosk.KaldiRecognizer(model, 16000)
        # Open the microphone stream
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format=pyaudio.paInt16,
                        channels=1,
                        rate=16000,
                        input=True,
                        frames_per_buffer=8192)
    def voiceRecognise(self, timeout: int = 120, stopword: str | None = None):
            print(f"Voice Recogniser running. Speak for a maximum of {timeout}s without input...")
            last_input_time = time.time()  # Track the last recognized input time
            text_to_return=""
            while True:
                data = self.stream.read(4096)  # Read in chunks of 4096 bytes
                if self.rec.AcceptWaveform(data):  # Accept waveform of input voice
                    # Parse the JSON result and get the recognized text
                    result = json.loads(self.rec.Result())
                    recognized_text = result['text']
                    # Append recongised words to the output string
                    text_to_return=text_to_return+(" "+recognized_text)
                    
                    # Update the last input time
                    last_input_time = time.time()
                    


                    # Check for the termination keyword
                    if stopword is not None and stopword.lower() in recognized_text.lower():
                        print("Termination keyword detected. Stopping...")
                        break
                        
                         
                
                # Check for timeout based on inactivity
                if time.time() - last_input_time > timeout:
                    print(f"No voice input detected for the specified timeout period ({timeout}s). Stopping...")
                    break
            
            # Stop and close the stream
            self.stream.stop_stream()
            self.stream.close()

            # Terminate the PyAudio object
            self.p.terminate()

            #Return the composite string
            if stopword.lower() in text_to_return:
                 text_to_return=text_to_return.replace(stopword.lower(),"")
            return(text_to_return)
