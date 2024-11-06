#GenAI script
import google.generativeai as genai
from dotenv import load_dotenv
import os

from VTT import voiceToText

texthandler=voiceToText()

class recipeWriter:
    def __init__(self):
        load_dotenv()
        genai.configure(api_key=os.environ["API_KEY"])
        self.model = genai.GenerativeModel("gemini-1.5-flash") #Initialise the Gemini model
        self.contextdata = """instructions('''You are a backend API designed to generate cooking recipes for a website. The workflow is as such: 
        Reject any input that is not possible to create a recipe from. Return an error specifying that an invalid input was recieved, formatted correctly:
        header: "INSTRUCTIONS:"
        subheader: "Please provide a list of ingredients from which to generate a recipe." 
        text: "You may also include:"
        list: "steps you would like to see, quantities, number of servings, serving suggestions"
        Your inputs are ingredients used, the quantities they are used in,and the name of the dish.
        Your outputs are a step-by-step recipe to make the dish using only the ingredients stated in the quantities given..
        The recipe should have an ingredient list, stating each ingredient, how it should be prepared, and what quantity.
        The recipe should have a methods list, stating the steps that need to be taken to successfully make the dish.
        The methods list should be structured so that parts of the dish that are made separately are listed in separate subsections.
        Ingredients list should go first, and ingredients for a subsection should be grouped.
        Methods list should go after, and steps for a subsection should be grouped.
        The input will be formatted as natural text or as a list, and the job of the API is to successfully parse it.
        The only output should be the completed recipe or error embedded in html tags. do not include ```html.''')
        input:{
        """
        
    
    def generate(self,text):
        # Change this to alter the output
        ingredients=text
        response = self.model.generate_content(self.contextdata+ingredients) 
        responsetext=response.text
        responsetext=responsetext.replace("```html","")
        responsetext=responsetext.replace("```","")
        file=open("output.txt", "w")
        file.write(responsetext)
        file.close()
        print(os.path.abspath(os.curdir))



writer=recipeWriter()
ingredients=texthandler.voiceRecognise(timeout=10,stopword='stop')
print(ingredients)
writer.generate(text=ingredients)

