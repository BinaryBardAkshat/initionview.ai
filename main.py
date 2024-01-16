import random
import pyttsx3
import pandas as pd
import json
import speech_recognition as sr
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print("user said: ", query)

        except Exception as e:
            print("Can you say that again please..")
            return "None"
        return query.lower()

with open("..\mainques.json") as json_data:
    question = json.load(json_data)
    q = pd.DataFrame(question)
    x = random.randint(0, 7)
    y = x + 1
    print(x, y)

# intro
speak("Hey geek welcome to Initionview AI. Enter your name in order to start your mock interview")
name = input("Enter your name: ")
speak(f"Welcome {name} to your first interview.")
speak("Are you ready to start your interview?")
query = takeCommand()
if 'yes' in query:
    speak(f"Great {name}")

speak("Here is a quick guide about this mock interview. I'll ask you 10 questions, and it will include a coding "
      "problem too. Based on your answers, I'll give you marks.")
speak("So let's start your interview with the first question. Your first question is:")

ques = q['questions'][x][str(y)]
print(ques)
speak(ques)

print(q['questions'][x]['keywords'])

for i in range(len(q['questions'][x]['keywords'])):
    keyword = q['questions'][x]['keywords'][i]
    print(keyword)

answer = takeCommand()
print("user said:", answer)

x_list = word_tokenize(keyword)
print(x_list)
y_list = word_tokenize(answer)
print(y_list)

sw = stopwords.words('english')
l1 = []
l2 = []

X_set = {w for w in x_list if not w in sw}
Y_set = {w for w in y_list if not w in sw}

rvector = X_set.union(Y_set)
for w in rvector:
    if w in X_set:
        l1.append(1)
    else:
        l1.append(0)
    if w in Y_set:
        l2.append(1)
    else:
        l2.append(0)
c = 0

for i in range(len(rvector)):
    c += l1[i] * l2[i]
cosine = c / float((sum(l1) * sum(l2)) ** 0.5)
perc1 = round(cosine, 1) * 100
print("Answer matching percentage is:", perc1, "%")
speak(f"Answer matching percentage is {perc1}%")

perf = []
count = 0

while count < 2:
    with open("..\mainques.json") as json_data:
        question = json.load(json_data)
        q = pd.DataFrame(question)
        x = random.randint(0, 7)
        y = x + 1
        print(x, y)
        ques = q['questions'][x][str(y)]
        count = count + 1
        print(ques)
        speak(ques)

        print(q['questions'][x]['keywords'])

        for i in range(len(q['questions'][x]['keywords'])):
            keyword = q['questions'][x]['keywords'][i]
            print(keyword)

        answer = takeCommand()
        print("user said:", answer)

        x_list = word_tokenize(keyword)
        print(x_list)
        y_list = word_tokenize(answer)
        print(y_list)

        sw = stopwords.words('english')
        l1 = []
        l2 = []

        X_set = {w for w in x_list if not w in sw}
        Y_set = {w for w in y_list if not w in sw}

        rvector = X_set.union(Y_set)
        for w in rvector:
            if w in X_set:
                l1.append(1)
            else:
                l1.append(0)
            if w in Y_set:
                l2.append(1)
            else:
                l2.append(0)
        c = 0

        for i in range(len(rvector)):
            c += l1[i] * l2[i]
        cosine = c / float((sum(l1) * sum(l2)) ** 0.5)
        perc = round(cosine, 1) * 100
        print("Answer matching percentage is:", perc, "%")
        speak(f"Answer matching percentage is {perc}%")

        perf.append(perc)

print(perf)
result = sum(perf)
fr = round(result)
print(fr)
speak(fr)
frs = round(result/200*100)
speak(frs)
print(frs)

if frs >= 35:
    print(f"So you did an amazing job in the interview and got {frs} percent. "
          f"You'll definitely be able to crack the interview and get the dream job in your first attempt.")
    speak(f"So you did an amazing job in the interview and got {frs} percent. "
          f"You'll definitely be able to crack the interview and get the dream job in your first attempt.")

else:
    print(f"Your score was {frs}, which isn't a very good score. "
          f"But you need to practice more so you'll be able to do well in the next interview. Practice makes perfect, after all.")
    speak(f"Your score was {frs}, which isn't a very good score. "
          f"But you need to practice more so you'll be able to do well in the next interview. Practice makes perfect, after all.")
