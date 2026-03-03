import os
import discord
from discord.ext import commands

TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.members = True  # Üye join eventleri için gerekli
bot = commands.Bot(command_prefix="!", intents=intents)

AUTO_ROLE_ID = 1474832131363442858  # Otomatik verilecek rol ID'si

@bot.event
async def on_ready():
    print(f"Bot hazır! {bot.user} olarak giriş yapıldı.")

@bot.event
async def on_member_join(member):
    role = member.guild.get_role(AUTO_ROLE_ID)
    if role:
        try:
            await member.add_roles(role)
            print(f"{member} kullanıcısına {role} rolü verildi.")
        except discord.Forbidden:
            print("Yetkim yok, rol veremedim!")
        except Exception as e:
            print(f"Hata oluştu: {e}")
    else:
        print("Rol bulunamadı!")

bot.run(TOKEN)
