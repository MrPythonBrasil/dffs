import discord
import uuid
import time
from discord.ext import commands

# Configurações do bot
TOKEN = 'MTM0OTE1MTUwNzY2NDIxMjA4MA.G1GJsG.oZZ03eZdpkG1ceC4aj6mJ_lzmok4K9eWRHFf78'  # Substitua pelo token do seu bot
PROMO_ID = '1310745070936391821'  # ID da promoção (fixo)

# Inicialização do bot
intents = discord.Intents.default()
intents.message_content = True  # Habilita o acesso ao conteúdo das mensagens
intents.members = True  # Habilita o acesso aos membros do servidor

bot = commands.Bot(command_prefix="!", intents=intents)  # Prefixo do comando: !

# Função para gerar o link Nitro
def generate_nitro_link():
    try:
        # Gerar UUID único
        unique_id = str(uuid.uuid4())

        # Gerar timestamp de expiração (24 horas a partir de agora)
        expiration_time = int(time.time()) + 86400  # 86400 segundos = 24 horas

        # Montar o link
        nitro_link = f"https://discord.com/billing/partner-promotions/{PROMO_ID}/{unique_id}?expires={expiration_time}"

        return nitro_link
    except Exception as e:
        print(f"Erro ao gerar o link: {e}")
        return None

# Comando para gerar o link Nitro
@bot.command(name='gen nitro')
async def gen_nitro(ctx):
    try:
        print(f"Comando 'gen nitro' recebido de {ctx.author}.")

        # Gerar o link
        nitro_link = generate_nitro_link()
        if not nitro_link:
            await ctx.send("Erro ao gerar o link. Tente novamente.")
            return

        # Enviar o link via DM
        await ctx.author.send(f"Aqui está o seu link Nitro: {nitro_link}")
        # Notificar no canal que a mensagem foi enviada
        await ctx.send(f"{ctx.author.mention}, verifique suas mensagens diretas (DMs)!")
    except discord.Forbidden:
        # Se o usuário tiver DMs desativadas
        await ctx.send(f"{ctx.author.mention}, não foi possível enviar a mensagem direta. Verifique se suas DMs estão ativadas!")
    except Exception as e:
        # Captura qualquer outro erro e exibe no terminal
        print(f"Erro no comando 'gen nitro': {e}")
        await ctx.send("Ocorreu um erro ao processar o comando. Tente novamente mais tarde.")

# Iniciar o bot
bot.run(TOKEN)
