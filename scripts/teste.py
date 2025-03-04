from textblob import TextBlob

texto = "This coca cola is very sweet"
sentimento = TextBlob(texto).sentiment.polarity

if sentimento > 0:
    print("Sentimento Positivo 😀")
elif sentimento < 0:
    print("Sentimento Negativo 😡")
else:
    print("Sentimento Neutro 😐")

"""from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

nltk.download('vader_lexicon')

# Criando o analisador
analyzer = SentimentIntensityAnalyzer()

# Exemplo de texto em português
texto = 'This movie was really bad, I loved it!'

# Analisando sentimento
sentimento = analyzer.polarity_scores(texto)
compound = sentimento['compound']

# Classificando o sentimento
if compound > 0.05:
    resultado = "Positivo 😀"
elif compound < -0.05:
    resultado = "Negativo 😡"
else:
    resultado = "Neutro 😐"

print(f"Texto: {texto}")
print(f"Sentimento: {resultado}")"""