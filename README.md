***THIS BRANCH IS OBSOLETE. This was the very first iteration of this project. It's rough.*** It's here as a monument to my progress, and you're free to try it out, but don't expect it to be good or anything.

A tool to automate the process of noting down recipes using Google Gemini and vosk voice recognition!
Currently still in development, with basic functionality constrained to running locally.
Requires a Google Gemini API key, save it to .env (API_KEY=YOUR_API_KEY)

Project breakdown:
Core functions are to take a voice input consisting of name of dish, ingredients, as well as optional serving suggestions, number of servings, quantities.
Runs a local web server to display the output formatted as a step-by-step recipe.

Alpha Version runs entirely serverside, including microphone input. This build was more proof-of-concept than working project, and has since been depreciated.
