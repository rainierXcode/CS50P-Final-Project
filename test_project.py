from project import user_respond
from project import message_probability
from project import arithmetic_response
from project import translate_text



def test_message_probability():
    assert message_probability(['hello', 'bot'],['hello', 'hi', 'hey', 'sup', 'heyo'], single_response=True) == 20
    assert message_probability(['what', 'is', 'your', 'name'],  ['what', 'is', 'your', 'name'], required_words=['what', 'name'] ) == 100
    assert message_probability(['a', 'good', 'programming', 'course', 'to', 'take'], ['what', 'is', 'good', 'programming', 'course', 'take'], required_words=['programming', 'course', 'take']) == 66
    assert message_probability(['yyyyyyy'] , ['what', 'is', 'good', 'programming', 'course', 'take'], required_words=['programming', 'course', 'take']) == 0



def test_user_respond():
    assert user_respond("Hello") == "Hello! How can I help you today?"
    assert user_respond("I want to change your name") == "I appreciate your interest, but my name cannot be changed. You can refer to me as Automatron. How can I assist you today?"
    assert user_respond("Are you a robot?") == 'Yes, I\'m a robot'
    assert user_respond("Find the product of 7 and 8.") == "The answer is 56"
    assert user_respond("Dutch Translation for Hello, how are you?") == "Hallo hoe is het"

def test_arithmetic_response():
    assert arithmetic_response(['1', 'plus', '1']) == "The answer is 2"
    assert arithmetic_response(['50', 'times', '10']) == "The answer is 500"
    assert arithmetic_response(['square', 'of', '9']) == "The answer is 81"
    assert arithmetic_response(['times']) == "What do you mean?"
    assert arithmetic_response(['25', 'divide', '0']) == "The answer is Error: Division by zero"


def test_translate_text():
    assert translate_text(['Spanish','Translation', 'for', 'Thank', 'You', 'Very','Much']) == "Muchas gracias"
    assert translate_text(['Spanish', 'Translation', 'for', 'Programming']) == "Programación"
    assert translate_text(['Portuguese','Translation', 'for','Goodbye']) == "Adeus"
    assert translate_text(['Esp','Transl', 'for', 'Hello', 'Love']) == "[Language] Translation for: [text to be translated]. Please provide the language you'd like to translate from and to, along with any specific instructions or preferences."
    assert translate_text(['French','Translation', 'for','Nice', 'to', 'meet', 'you']) == "Ravi de vous rencontrer"
