import discord

async def send(ctx, message, isEmbed):
    if isEmbed:
        if isinstance(ctx, discord.ApplicationContext):
            await ctx.respond(embed=message)
        else:
            await ctx.send(embed=message)
    else:
        if isinstance(ctx, discord.ApplicationContext):
            await ctx.respond(message)
        else:
            await ctx.send(message)