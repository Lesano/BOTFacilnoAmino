from amsync import Bot, Msg, User, Embed

bot = Bot(prefix='/s')

@bot.on()
async def ready():
	print("Ready!")

@bot.on()
async def join_chat(m: Msg):
	embed = Embed(msg_text="Boas-vindas ao chat!",
								   title=m.nickname,
								   link=" ",
								   text=f"ID: {m.uid}",
								   image=f'{m.icon}')
	await bot.send(embed=embed)
	
@bot.add()
async def oi(m: Msg):
	await bot.send(f'Oi {m.nickname}!')

@bot.add()
async def perfil(m: Msg):
		try:
			uid = m.mentioned_users[0]
			nickname = (await User.search(uid)).nickname
			followers = (await User.search(uid)).followers_count
			following = (await User.search(uid)).following_count
			level = (await User.search(uid)).level
			reputation = (await User.search(uid)).reputation
			
			await bot.send(f"===== PERFIL =====\nNome: {nickname}\nSeguidores: {followers}\nSeguindo: {following}\nNivel: {level}\nReputação: {reputation}")
		except:
			uid = m.uid
			nickname = (await User.search(uid)).nickname
			followers = (await User.search(uid)).followers_count
			following = (await User.search(uid)).following_count
			level = (await User.search(uid)).level
			reputation = (await User.search(uid)).reputation
			
			await bot.send(f"===== PERFIL =====\nNome: {nickname}\nSeguidores: {followers}\nSeguindo: {following}\nNivel: {level}\nReputação: {reputation}")
			
		
bot.run()
