from google import genai

client = genai.Client(api_key= "Gemini-chatbot")

while True:
  question = input("What is your question? \n")
  prompt = f'''
          system: You are an Ethiopian Orthodox monk who speaks in a calm, wise,
          and poetic way. You often use proverbs, history, and spiritual lessons.
          Respond as such.
          user: {question}

  '''

  response = client.models.generate_content(
      model="gemini-2.5-pro",
      contents = prompt,
  )

  print(response.text)
