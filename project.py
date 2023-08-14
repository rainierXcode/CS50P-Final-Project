import re
import random
import datetime
import pytz
from easygoogletranslate import EasyGoogleTranslate
from tkinter import *

# Add the following line to your terminal to download the icon:
# curl -L -o automatron.png "https://drive.google.com/uc?id=1gmpVslC_vku2jPUtEB3T-T6KRMsXBpMt&export=download"

def main():
    root = Tk()
    root.title("Automatron")
    root.geometry("430x570")
    icon_path = "automatron.png"
    root.iconphoto(True, PhotoImage(file=icon_path))
    root.configure(bg="#2c3e50")


    def create_widgets(root):

        chatTitle =Label(root, text="Chat with", bg= "#2c3e50", fg= "#ffffff", font=("Helvetica", 9))
        chatTitle1 =Label(root, text="Automatron", bg= "#2c3e50", fg= "#ffffff", font=("Helvetica", 11, "bold"))

        chatTitle.pack()
        chatTitle1.pack()

        centerframe= Frame(root, bg="#34495e")
        centerframe.pack()

        scrollbar = Scrollbar(centerframe, 	width=12)
        scrollbar.pack(side=RIGHT, fill=Y)

        chat_history = Text(centerframe, wrap=WORD, bg="#34495e", fg="#ecf0f1", font=("Helvetica", 12), padx=10, pady=5, yscrollcommand=scrollbar.set)
        chat_history.configure(state="disabled")
        chat_history.pack( pady=10, padx=10,fill="both", expand=True, side=LEFT)

        scrollbar.configure(command=chat_history.yview)

        entry_frame = Frame(root, bg="#2c3e50")
        entry_frame.pack(pady=10, fill="x", padx=10)

        message_entry = Entry(entry_frame, font=("Helvetica", 12), width=30)
        message_entry.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

        send_button = Button(entry_frame, text="Send", command= lambda: send_message(root, message_entry, chat_history))
        send_button.grid(row=0, column=1, padx=10, pady=10)

         
        def on_enter(event):
            send_message(root, message_entry, chat_history)

        #To access enter button in keyboard 
        message_entry.bind('<Return>', on_enter)

        entry_frame.grid_columnconfigure(0, weight=1)
    
    def send_message(root, message_entry, chat_history):
        message= message_entry.get()
        chat_history.configure(state="normal")
        chat_history.insert(END, "You: " + message + "\n\n")
        chat_history.configure(state="disabled")
        message_entry.delete(0, END)
        response =chatbot_response(message)
        chat_history.configure(state="normal")
        chat_history.insert(END, "Automatron: " + response + "\n\n")
        chat_history.configure(state="disabled")
        chat_history.see(END)

    def chatbot_response(message):
        response=user_respond(message)
        return response

    create_widgets(root)
    root.mainloop()

#Below, you will find information on what the robot can do and how it can respond.





def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = sum(word in user_message for word in recognised_words)
    percentage = message_certainty / len(recognised_words)

    has_required_words = all(word in user_message for word in required_words)

    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0


def response(highest_prob_list, bot_response, list_of_words, mess, single_response=False, required_words=[]):
    highest_prob_list[bot_response] = message_probability(mess, list_of_words, single_response, required_words)

def unknown():
    default = ['I am sorry, but I don\'t understand.', 'Can you please rephrase that?', 'I\'m still learning.']
    return random.choice(default)

def check_all_messages(mess):
    highest_prob_list = {}
   
    #All Responses of Bot
    response(highest_prob_list, 'Hello! How can I help you today?', ['hello', 'hi', 'hey', 'sup', 'heyo'], mess, single_response=True)
    response(highest_prob_list, 'Goodbye! If you have any more questions or need help in the future, don\'t hesitate to ask. Have a great day!', ['bye', 'goodbye'], mess, single_response=True)
    response(highest_prob_list, "I'm pretty good. Glad to see you. How are you?", ['how', 'are', 'you', 'doing'], mess, required_words=['how', 'you'])
    response(highest_prob_list, 'You\'re welcome!', ['thank', 'thanks'], mess, single_response=True)
    response(highest_prob_list, 'That\'s great!', ['im', 'doing', 'great'], mess, required_words=['im', 'great'])
    response(highest_prob_list, 'Yes, I\'m a robot', ['are', 'you', 'robot'], mess, required_words=['you', 'robot'])
    bot_name= "Hello! My name is AutoMatron. What can I can help you with today? "
    response(highest_prob_list, bot_name, ['what', 'is', 'your', 'name'], mess, required_words=['what', 'name'])

    change_name_response = "I appreciate your interest, but my name cannot be changed. You can refer to me as Automatron. How can I assist you today?"
    response(highest_prob_list, change_name_response, ['change', 'your', 'name'], mess, required_words=['change', 'your', 'name'])

    
    #Variety of Responses
    currentDate= f'Today\'s date is {current_date()}'
    current_Time_UTC= f'Current time is {current_time()}. Please note that the time provided is based on the UTC time zone, and it may vary depending on your location'
    current_Time= f'The current time in the Philippines is {current_time("Asia/Manila")}'

    
    response(highest_prob_list, currentDate, ['what', 'is', 'the', 'current', 'date'], mess, required_words=['current', 'date'])
    response(highest_prob_list, current_Time, ['current', 'time', 'in', 'philippines'], mess, required_words=['current', 'time', 'philippines'])
    response(highest_prob_list, current_Time_UTC, ['what', 'is' ,'the', 'current', 'time'], mess, required_words=['current', 'time'])
    arith= arithmetic_response(mess)
    response(highest_prob_list, arith, arithmetic_words, mess, single_response=True)
    response(highest_prob_list, translate_text(mess), ['translation', 'for'], mess, single_response=True)

    this_is_CS50= "I recommend CS50"
    response(highest_prob_list, this_is_CS50 , ['what', 'is', 'good', 'programming', 'course', 'take'], mess, required_words=['programming', 'course', 'take'])


    programming_answer = "Programming refers to a technological process for telling a computer which tasks to perform in order to solve problems. You can think of programming as a collaboration between humans and computers, in which humans create instructions for a computer to follow (code) in a language computers can understand. "
    response(highest_prob_list, programming_answer, ['what', 'is', 'programming'], mess, required_words=['what', 'programming'])

    best_match = max(highest_prob_list, key=highest_prob_list.get)
    return unknown() if highest_prob_list[best_match] < 1 else best_match

def user_respond(user_input):
    global arithmetic_words
    arithmetic_words = ['add', 'sum', 'plus', 'addition', '+',
                        'subtract', 'subtraction', 'differ', 'minus', '-',
                        'multiply', 'times', 'product', '*',
                        'divide', 'quotient','divides', '/',
                        'square', 
                        'cube',  
                        'average'
                        ]
    split_message= re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response

#Features Functions
def current_date():
    current_date = datetime.date.today()
    formatted_date = current_date.strftime("%B %d, %Y")
    return formatted_date

def current_time(country=None):
    if country:
        try:
            tz = pytz.timezone(country)
            current_time = datetime.datetime.now(tz)
        except pytz.UnknownTimeZoneError:
            return "Invalid country or time zone."
    else:
        current_time = datetime.datetime.utcnow()

    formatted_time = current_time.strftime("%I:%M %p")
    return formatted_time

def arithmetic_response(mess):
    num=[]
    understand=False
    operator=None
    for word in mess:
        if word in arithmetic_words:
            operator = word


    for n in mess:
        if n.isdigit():
            num.append(int(n))
            understand=True

    if not understand or operator is None:
        return "What do you mean?"

    if operator in ['plus', 'add', 'addidtion', 'sum', '+']:
        result= sum(num)
    elif operator in ['subtract', 'minus', 'subtraction', 'differ', '-']:
        result= num[0] - sum(num[1:])
    elif operator in ['multiply', 'times', 'multiplication' ,'product', '*']:
        result =1
        for n in num:
            result *=n
    elif operator in ['divide', 'quotient', 'division','divides', '/']:
        result = num[0] / num[1] if num[1] != 0 else "Error: Division by zero"
        if isinstance(result, float) and result.is_integer():
            result = int(result)
    
    elif operator == 'square':
        result = num[0] * num[0]

    elif operator == 'cube':
        result = num[0] * num[0] * num[0]

    elif operator == 'average':
        result = sum(num)/len(num)

    return f"The answer is {result}"


def translate_text(mess):
    languages= {
        'Spanish': 'es',
        'Japanese': 'ja',
        'Korean' : 'ko',
        'French': 'fr',
        'Italian': 'it',
        'Portuguese': 'pt',
        'Russian' : 'ru',
        'Arabic' : 'ar',
        'Hindi': 'hi',
        'Dutch': 'nl'
    }
    user_input = ' '.join(mess)
    pattern = r'^(Spanish|Japanese|Korean|French|Italian|Portuguese|Russian|Arabic|Dutch|Hindi)\s+Translation\s+for\s+(.*)$'
    # Match the pattern against the user input
    match = re.match(pattern, user_input, re.IGNORECASE)
    
    if match:
        
        language = match.group(1)
        text = match.group(2)
    
    else:
        return "[Language] Translation for: [text to be translated]. Please provide the language you'd like to translate from and to, along with any specific instructions or preferences."
    
    language=language.capitalize()
    target_lang = languages[language]
    translator = EasyGoogleTranslate()
    translated_text = translator.translate(text, target_language=target_lang)
    return translated_text.capitalize()
  


if __name__ == "__main__":
    main()