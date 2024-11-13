from app.imports import *
from app.command import router

bot = Bot(token='7619489280:AAHo_hhjdzQepKxHPegXS7afNe2OwfvYWFs')
dp = Dispatcher()

async def main():
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Disable")