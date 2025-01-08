**REWORKED FROM PREALPHA!**

A tool to automate the process of noting down recipes using Google Gemini!
Currently still in development, with basic functionality fully operational


Project breakdown:
Core functions are to take a voice input consisting of name of dish, ingredients, as well as optional serving suggestions, number of servings, quantities.
Runs a local web server to display the output formatted as a step-by-step recipe.

Setup:
Requirements: 
.env file containing the following:
  -Google Gemini API key
  -Self-Generated Session Key
  -Host IP
  -Host Port
SSL certificate and key (.crt and .key, respectively)

Ensure that the .env is in the project root, and have the paths to the certificate and key handy to add them to the code (default is in project root, adjust as needed)
A sample env file is included, just replace the fields with the info as required, and rename it from sample.env -> .env (blank name)

Features planned:
-Save feature allowing generated recipes to be collected
-Editable recipe, rather than statically displayed
-More robust voice recognition/instruction parsing


Jan 2025 Update - I'm looking to publicly host an instance of this project, which will require separation of the front and backend (since this version is designed for localhosting, the front and backend are packaged together for ease-of-setup). I'll probably make a new repo for each separately  for ease of hosting, but I do plan to continue updating this repo since it's nice to have everything in one place, locally-hostable.
