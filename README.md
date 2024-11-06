A tool to automate the process of noting down recipes using Google Gemini and vosk voice recognition!
Currently still in development, with basic functionality constrained to running locally.
Requires a Google Gemini API key, save it to .env (API_KEY=YOUR_API_KEY)
Project breakdown:
Core functions are to take a voice input consisting of name of dish, ingredients, as well as optional serving suggestions, number of servings, quantities.
Runs a local web server to display the output formatted as a step-by-step recipe.

Features planned:
-Save feature allowing generated recipes to be collected
-Editable recipe, rather than statically displayed
-More robust voice recognition/instruction parsing
