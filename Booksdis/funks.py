import discord
import json


def create_embed(title: str, content: str, color: discord.Color):
    embed = discord.Embed(title=title, color=color)
    embed.add_field(name=content, value="")
    print(type(embed))
    return embed


def config() -> dict:
    with open("Config.json", "r") as f:
        return json.load(f)
