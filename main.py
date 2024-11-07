from VTT import voiceToText
from googgen import recipeWriter
texthandler=voiceToText()
writer=recipeWriter()

#adjust the timeout and termination keyword here
ingredients=texthandler.voiceRecognise(timeout=100,stopword='stop')
print(ingredients)
writer.generate(text=ingredients)
