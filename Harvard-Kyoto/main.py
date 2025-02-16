from devanagiri import devanagiri as dv
import tkinter as tk
import pyperclip

screen = tk.Tk()
screen.title("Harvard Kyoto - Latin & देवनागरी")
screen.geometry('600x40')

entry = tk.Entry(screen, width=100)
entry.grid(row=1, column=1, columnspan=5)

display = tk.Entry(screen, width=80)
display.grid(row=2, column=1, columnspan=4)

def d_to_l(text):
    output_text = ''
    index = 0

    while index < len(text):
        found_match = None

        if (index + 1) < len(text):
            two_letters = text[index:index+2]

            if two_letters in dv['vowels']:
                output_text += dv['vowels'][two_letters]
                found_match = dv['vowels'][two_letters]
                index += 2

            elif two_letters in dv['consonants']:
                output_text += dv['consonants'][two_letters]
                found_match = dv['consonants'][two_letters]
                index += 2

        if found_match == None:
            letter = text[index]

            if letter in dv['vowels']:
                output_text += dv['vowels'][letter]
                found_match = dv['vowels'][letter]
                index += 1

            elif letter in dv['consonants']:
                output_text += dv['consonants'][letter]
                found_match = dv['consonants'][letter]
                index += 1

            if found_match == None:
                output_text += text[index]
                index += 1


    return output_text

def fixer(text):
    for index in range(len(text)):
        if index + 1 < len(text):
            if text[index] in dv['consonant_list']:
                if text[index + 1] in dv['consonant_list']:
                    text = text[:index + 1] + dv['halant'] + text[1 + index:]
                if text[index + 1] in dv['vowel_list']:
                    text = text[:index + 1] + dv['vowel_list'][text[index + 1]] + text[2 + index:]

    return text

def convert():
    text_to_process = entry.get()
    display.delete(0, tk.END)
    text = fixer(d_to_l(text_to_process))
    display.insert(0, text)
    pyperclip.copy(text)

button = tk.Button(screen, text='Convert.', command=convert, width=15)
button.grid(row=2, column=5)

tk.mainloop()