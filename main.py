#from keep_alive import keep_alive
import discord
from discord import app_commands
from discord.ext import commands
import my_config
import queries  
import embed_settings       

#bot settings
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(intents=intents, command_prefix="+")
user_listas=[]

@bot.event
async def on_ready():
  print(f"Estou pronto! Bem-vindo {bot.user}")

@bot.command(name="listas")
async def get_lists(ctx):
 # await ctx.message.delete()
  user_listas = queries.get_list_user(ctx.author.id)
  if len(user_listas) == 0:
    await ctx.send("Não existem listas criadas para este usuário")
  else:
    embed = embed_settings.lists_by_user(user_listas,ctx.author.id)
    await ctx.send(embed=embed)

@bot.command(name="add")
async def add_list(ctx):
  if ctx.message.author == bot.user:
    return

  if 'lista' in ctx.message.content:
    await ctx.send("Qual será o nome da nova lista?")
    message = await bot.wait_for('message', check=lambda message: message.author == ctx.author)
    queries.create_list_user(message.content,ctx.author.id)
    await ctx.send(f"A lista **{message.content}** foi **CRIADA** com sucesso!")
    return

  if 'tarefa' in ctx.message.content:
    await ctx.send("Digite o #ID da lista para a qual deseja adicionar a tarefa.")
    user_listas = queries.get_list_user(ctx.author.id)
    await ctx.send(user_listas)
    message = await bot.wait_for('message', check=lambda message: message.author == ctx.author)
    await ctx.send("Digite a(s) tarefa(s) que deseja adicionar separadas por (;) ponto e virgula.")
    tasks_user = await bot.wait_for('message', check=lambda message: message.author == ctx.author)
    tasks = split_tasks(tasks_user.content)
    result = queries.add_task_list_user(message.content,ctx.author.id, tasks)
    if result is True:
      await ctx.send(f"A tarefa **CRIADA** com sucesso!")
    if result is False:
      await ctx.send(f"**NÃO foi possível criar a tarefa!** \n Algumas causas possíveis: \n - Não existe lista com o #ID informado \n - A lista informada não pertence ao usuário")

  else:
    await ctx.send("Comando desconhecido. Caso tenha dúvidas, digite +help")
    return

@bot.command(name="delete")
async def delete_list(ctx):
  if ctx.message.author == bot.user:
    return

  if 'lista' in ctx.message.content:
    await ctx.send("Digite o #ID da lista que deseja deletar. \n **ATENÇÃO:** esta ação não poderá ser desfeita!")
    user_listas = queries.get_list_user(ctx.author.id)
    response = (f"Resultado teste: {user_listas} =)")
    await ctx.send(user_listas)
    message = await bot.wait_for('message', check=lambda message: message.author == ctx.author)
    result = queries.delete_list_user(message.content,ctx.author.id)
    if result is True:
      await ctx.send(f"A lista **#{message.content}** foi **DELETADA** com sucesso!")
    if result is False:
      await ctx.send(f"**NÃO foi possível deletar a lista informada!** \n Algumas causas possíveis: \n - Não existe lista com o #ID informado \n - A lista informada não pertence ao usuário e não pode ser deletada por outro(s)")


  if 'tarefa'in ctx.message.content:
    await ctx.send("Digite o #ID da lista que contém a tarefa que deseja deletar. \n **ATENÇÃO:** esta ação não poderá ser desfeita!")
    user_listas = queries.get_list_user(ctx.author.id)
    response = (f"Resultado teste: {user_listas} =)")
    await ctx.send(user_listas)

    message = await bot.wait_for('message', check=lambda message: message.author == ctx.author)
    list_id = message.content
    result_tasks_list = queries.all_task_list_user(message.content,ctx.author.id)
    await ctx.send(result_tasks_list)

    await ctx.send("Digite o #ID da tarefa que deseja deletar. \n **ATENÇÃO:** esta ação não poderá ser desfeita!")
    message = await bot.wait_for('message', check=lambda message: message.author == ctx.author)
    result = queries.delete_task_list_user(list_id, ctx.author.id, message.content)
    if result is True:
      await ctx.send(f"A tarefa **#{message.content}** foi **DELETADA** com sucesso!")
    if result is False:
      await ctx.send(f"**NÃO foi possível deletar a tarefa informada!** \n Algumas causas possíveis: \n - Não existe lista com o #ID informado \n - A lista informada não pertence ao usuário e não pode ser deletada por outro(s)")
  else:
    await ctx.send("Comando desconhecido. Caso tenha dúvidas, digite +help")
    return
 
def split_tasks(tasks_list):
  tasks=[]
  for task in tasks_list.split(';'):
    tasks.append(task)
  return tasks

@bot.command(name="tarefas")
async def get_tasks_by_list_id(ctx):
  await ctx.send("Digite o #ID da lista para consultar as tarefas.")
  message = await bot.wait_for('message', check=lambda message: message.author == ctx.author)
  tasks_list = queries.all_task_list_user(message.content, ctx.author.id)
  if len(tasks_list) == 0:
    await ctx.send("Não existem listas criadas para este usuário")
  else:
    await ctx.send(embed=embed_settings.tasks_by_list(tasks_list = tasks_list)) 

#Apollo
#keep_alive()
bot.run(my_config.TOKEN)
