from app.imports import *
import app.keyboards as kb

router = Router()

@router.message(CommandStart())
async def start(message: Message):
    await message.answer("hi", reply_markup=kb.main)

@router.message(Command('help'))
async def help(message: Message):
    await message.reply("Nill")

#keyboards(MAIN)

@router.message(F.text == "Browser")
async def key_browser(message: Message):
    await message.answer(":)", reply_markup=kb.Browser)

@router.message(F.text == "PC")
async def key_PC(message: Message):
    await message.answer(":)", reply_markup=kb.PC)

@router.message(F.text == "Game")
async def key_Game(message: Message):
    await message.answer(":)", reply_markup=kb.Game)

@router.message(F.text == "Back<")
async def key_Game(message: Message):
    await message.answer("Back", reply_markup=kb.main)

#browser
@router.message(F.text == "restart")
async def key_Game(message: Message):
    await message.reply("restarting")
    

