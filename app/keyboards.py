from app.imports import *

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Browser"),
                                     KeyboardButton(text="PC"),
                                     KeyboardButton(text="Game")]],
                                     resize_keyboard=True,
                                     input_field_placeholder='mew')

Browser = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="restart"),
                                     KeyboardButton(text="test1"),
                                     KeyboardButton(text="test1")],
                                     [KeyboardButton(text='Back<')]],
                                     resize_keyboard=True,
                                     input_field_placeholder='mew')

PC = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="test2"),
                                     KeyboardButton(text="test2"),
                                     KeyboardButton(text="test2")],
                                     [KeyboardButton(text='Back<')]],
                                     resize_keyboard=True,
                                     input_field_placeholder='mew')

Game = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="test3"),
                                     KeyboardButton(text="test3"),
                                     KeyboardButton(text="test3")],
                                     [KeyboardButton(text='Back<')]],
                                     resize_keyboard=True,
                                     input_field_placeholder='mew')                               