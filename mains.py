from PyDictionary import PyDictionary
import easygui
dictionary = PyDictionary()

a = easygui.msgbox(msg="What word do you wanna know?",ok_button='LOL')
bio = dictionary.meaning('bionic')
b = easygui.msgbox(msg='Meaning: {}'.format(bio['Adjective'][0].capitalize()))