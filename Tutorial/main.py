from amsync import Bot, Msg

bot = Bot(prefix="!s")

@bot.on()
async def ready():
  print("Ready!")
  
@bot.add()
async def oi(m: Msg):
  await bot.send(f"Oi {m.nickname}!")
  
bot.run()
