# **Automatron: A Simple Text Recognition Chatbot**

**Automatron** is a simple yet powerful chatbot developed as the final project for CS50's Introduction to Programming with Python course. This text recognition chatbot, which has a user-friendly interface, evaluates input and generates relevant responses, providing seamless conversation. Explore the world of Automatron and see how its straightforward design may improve your interaction experience.

Imported Python Libraries:

```python
import datetime

import pytz

from easygoogletranslate import EasyGoogleTranslate

from tkinter import *
```

## **Features**
* **Simple Text Recognition**
* **Determine the Current Time & Date**
* **Arithmetic Problem Solving** 
* **Text Translation**
* **Can define what programming is**

## **Project Workflow: How the Chatbot Functions**
The concept behind Automatron is straightforward: users submit their questions into the entry frame, and the chatbot generates responses based on the input. The chatbot's response selection is determined by several factors:

1. The presence of more recognized words in the user's input compared to others.
1. Ensuring all required words are included in the user's input.
1. The response with the highest probability is chosen.

By considering these factors, Automatron provides relevant and accurate responses to user inputs, enhancing the overall chatbot experience.


```python
    message_certainty = sum(word in user_message for word in recognised_words)
    percentage = message_certainty / len(recognised_words)

    has_required_words = all(word in user_message for word in required_words)

    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0

```


## **Showcasing Interaction: User Input and Chatbot Responses**
<img src="automatron.gif" alt="Alt text" title="Chatbot Responses" width="430" height="570">

## **Possible Enhancements for Automatron:**

* Artificial Intelligence (AI) Integration

* Increasing the number of languages supported for translation

* Using voice recognition to provide hands-free interaction

* Options for modifying the chatbot's appearance and personality

* Including a learning mechanism that will allow the chatbot to adapt and improve over time

## **YouTube demonstration**
[My Final Project Presentation](https://youtu.be/1L0w_uJkgtg)

## **About CS50P**
CS50P teaches the fundamentals of programming in Python, including variables, functions, loops, and reading and writing files. It draws from real-world programming problems and has plenty of practical exercises. The course is taught by David J. Malan.

[CS50's Introduction to Programming with Python course](https://cs50.harvard.edu/python/2022/)

