import discord # Тут я импортировал дискорд
from discord.ext import commands # Из библиотеки импортировал команды
import os

PREFIX = '.'

client = commands.Bot( command_prefix = PREFIX ) # Установил префикс

client.remove_command( 'help' )

@client.event

async def on_ready():			# Бот пишет 'Conection done' в консоль когда присоединяется к серверу	
	print( 'Bot connected' )

# команда для удаления сообщений

@client.command( pass_context = True)
@commands.has_permissions( administrator = True )

async def clear( ctx , amount = 1000000000000):
	await ctx.channel.purge( limit = amount )

# Kick command
@client.command( pass_context = True)
@commands.has_permissions( administrator = True )
 
async def kick( ctx, member: discord.Member, *, reason = None ):
	await ctx.channel.purge( limit = 1 )

	await member.kick( reason = reason )

	await ctx.send( f'{member.mention} has been kicked')

#Команда бана

@client.command( pass_context = True)
@commands.has_permissions( administrator = True )

async def ban( ctx, member: discord.Member, *, reason = None ):
	await ctx.channel.purge( limit = 1 )

	await member.ban( reason = reason )

	author=ctx.message.author

	await ctx.send( f'{author.mention} забанил {member.mention}')

#Команда разбана

@client.command( pass_context = True)
@commands.has_permissions( administrator = True )

async def unban( ctx, *, member):
	await ctx.channel.purge( limit =1 )
	author=ctx.message.author
	banned_users = await ctx.guild.bans()

	for ban_entry in banned_users:
		user = ban_entry.user

		await ctx.guild.unban( user )
		await ctx.send(f'{author.mention} розбанил {user.mention}')

		return

#help command

@client.command( pass_context = True )

async def help( ctx ):
	await ctx.channel.purge( limit = 1 )

	emb = discord.Embed( title = 'Навигация по командам')

	emb.add_field( name = '{}clear'.format( PREFIX ), value = 'Очистка чата')
	emb.add_field( name = '{}kick'.format( PREFIX ), value = 'Удаление участника с сервера')
	emb.add_field( name = '{}ban'.format( PREFIX ), value = 'Забанить участника')
	emb.add_field( name = '{}unban'.format( PREFIX ), value = 'Разбанить участника')
	emb.add_field( name = '{}mute_voice'.format( PREFIX ), value = 'Забрать голос у Ариель')
	emb.add_field( name = '{}unmute_voice'.format( PREFIX ), value = 'Дать голос Ариель')
	emb.add_field( name = '{}mute_chat'.format( PREFIX ), value = 'Забрать право писать')
	emb.add_field( name = '{}unmute_chat'.format( PREFIX ), value = 'Дать право писать')
	emb.add_field( name = '{}help'.format( PREFIX ), value = 'Команды сервера')

	await ctx.author.send( embed = emb)


#Функция voice mute

@client.command( pass_context = True )
@commands.has_permissions( administrator = True )

async def mute_voice( ctx, member: discord.Member):
	await ctx.channel.purge( limit = 1 )

	author=ctx.message.author

	v_mute_role = discord.utils.get( ctx.message.guild.roles, name = 'voice mute')

	await member.add_roles( v_mute_role )

	await ctx.send( f'{author.mention} забрал голос у {member.mention}.')


#Функция voice unmute

@client.command( pass_context = True )
@commands.has_permissions( administrator = True )

async def unmute_voice( ctx, member: discord.Member):
	await ctx.channel.purge( limit = 1 )

	author=ctx.message.author

	v_mute_role = discord.utils.get( ctx.message.guild.roles, name = 'voice mute')

	await member.remove_roles( v_mute_role )

	await ctx.send( f'{author.mention} дал голос {member.mention}.')


#Функция chat mute

@client.command( pass_context = True )
@commands.has_permissions( administrator = True )

async def mute_chat( ctx, member: discord.Member):
	await ctx.channel.purge( limit = 1 )

	author=ctx.message.author

	c_mute_role = discord.utils.get( ctx.message.guild.roles, name = 'chat mute')

	await member.add_roles( c_mute_role )

	await ctx.send( f'{author.mention} запретил писать {member.mention}.')


#Функция chat unmute

@client.command( pass_context = True )
@commands.has_permissions( administrator = True )

async def unmute_chat( ctx, member: discord.Member):
	await ctx.channel.purge( limit = 1 )

	author=ctx.message.author

	c_mute_role = discord.utils.get( ctx.message.guild.roles, name = 'chat mute')

	await member.remove_roles( c_mute_role )

	await ctx.send( f'{author.mention} разрешил писать {member.mention}.')

#Команда удаляется когда её написали

@client.command( pass_context = True)

async def hello( ctx, amount = 1 ):
	await ctx.channel.purge( limit = amount )

	author=ctx.message.author
	await ctx.send( f'Hello, {author.mention} ' )

# bot connection

# token = open( 'token.txt', 'r').readline()

#client.run( token )

token =  os.environ.get('BOT_TOKEN')

bot.run(str(token))
