#!/bin/usr/python3
from hikari import GatewayBot, Intents, Activity, ActivityType, GuildMessageCreateEvent
from config import *
import time
import asyncio

bot: GatewayBot = GatewayBot(token=TOKEN, intents=Intents.ALL)


async def countdown(t: int) -> None:
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        await bot.rest.create_message(channel=TIMER_CHANNEL, content=timer)
        time.sleep(1)
        t -= 1


@bot.listen(GuildMessageCreateEvent)
async def trigger_countdown(event: GuildMessageCreateEvent):
    print(event.content)
    if event.content.startswith('!cd'):
        await bot.rest.create_message(content=f'<@&{GAY_MASTER}> Sabotage!!!!!', channel=TIMER_CHANNEL, role_mentions=True,
                                      mentions_everyone=True, user_mentions=True)
        await countdown(90)


@bot.listen(GuildMessageCreateEvent)
async def give_ghost_role(event: GuildMessageCreateEvent):
    if event.content.startswith('!ghost'):
        await bot.rest.add_role_to_member(guild=DEFAULT_SERVER,role=GHOST_ROLE, user=event.author_id)
        await event.message.respond(content=f'Ghost rolle hinzugefügt!')

def main() -> None:
    bot.run(activity=Activity(type=ActivityType.WATCHING, name="the game"))


if __name__ == '__main__':
    main()
