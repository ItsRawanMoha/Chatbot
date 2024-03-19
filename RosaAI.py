import openai
import speech_recognition as sr
import pyttsx3



# Initialize text-to-speech engine
engine = pyttsx3.init()

# Function to interact with GPT-3 and get response
def ask_gpt3(prompt):

    openai.api_key = 'your_openai_api_key_here'
    
    response = openai.Completion.create(
      engine="text-davinci-003",
      prompt=prompt,
      temperature=0.7,
      max_tokens=150
    )

    return response.choices[0].text.strip()

# Function to record text from user's speech
def record_text():
    # Loop incase of errors
    while(1):
        try:
            # use the microphone as source for input.
            with sr.Microphone() as source2:
                # Prepare recognizer to receive input
                sr.adjust_for_ambient_noise(source2, duration=0.2)

                # listen for the user's input
                audio2 = r.listen(source2)

                # using google to recognize audio
                MyText = r.recognize_google(audio2)
                print(MyText)
                

                return MyText 
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

# Main loop
while True:
    user_input = record_text()
    if user_input.lower() == 'exit':
        print("Bot: Goodbye!")
        engine.say("Goodbye!")
        engine.runAndWait()
        break
    elif user_input.strip() == '':
        print("Bot: Please say something.")
        engine.say("Please say something.")
        engine.runAndWait()
    else:
        # Send user input to GPT-3
        response = ask_gpt3(user_input)
        print("Bot:", response)
        engine.say(response)
        engine.runAndWait()