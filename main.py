import turtle
import speech_recognition as sr

# Word to shape mapping (can be expanded)
shape_map = {
    'circle': 'circle',
    'square': 'square',
    'triangle': 'triangle',
    'star': 'star',
    'tree': 'branch',
    'sun': 'circle',
    'moon': 'circle',
    'wheel':'circle'
}

# Setup turtle
screen = turtle.Screen()
t = turtle.Turtle()
t.speed(0)

def draw_star():
    for _ in range(5):
        t.forward(50)
        t.right(144)

def draw_branch():
    t.left(90)
    for i in range(3):
        t.forward(50 - i*15)
        t.backward(50 - i*15)
        t.right(45)
    t.left(90)

def draw_shape(shape):
    if shape == 'circle':
        t.circle(40)
    elif shape == 'square':
        for _ in range(4):
            t.forward(50)
            t.right(90)
    elif shape == 'triangle':
        for _ in range(3):
            t.forward(50)
            t.right(120)
    elif shape == 'star':
        draw_star()
    elif shape == 'branch':
        draw_branch()

# Recognize speech
recognizer = sr.Recognizer()
with sr.Microphone() as source:
    print("🎤 Speak a sentence with words like 'circle', 'star', 'tree'...")
    audio = recognizer.listen(source)

try:
    text = recognizer.recognize_google(audio)
    print("✅ You said:", text)
    words = text.lower().split()

    # Draw shapes based on words
    x, y = -200, 0
    for word in words:
        shape = shape_map.get(word)
        if shape:
            t.penup()
            t.goto(x, y)
            t.pendown()
            draw_shape(shape)
            x += 100
        else:
            print(f"Skipping unrecognized word: {word}")

except sr.UnknownValueError:
    print("❌ Could not understand audio.")
except sr.RequestError:
    print("❌ Could not request results from Google.")

turtle.done()
