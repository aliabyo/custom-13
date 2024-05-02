import random
import time
from highrise import BaseBot, Position, User, AnchorPosition, GetMessagesRequest
import asyncio, random
from highrise.__main__ import *
from highrise import BaseBot, Highrise, Position, AnchorPosition, Reaction
from highrise import __main__
from asyncio import run as arun
import asyncio
from random import choice
from json import load, dump
from time import time
from math import sqrt
from highrise import BaseBot, User, Position, AnchorPosition
import json
from typing import List
from datetime import datetime, timedelta
from highrise.models import SessionMetadata
import re
from highrise.models import SessionMetadata, User, Item, Position, CurrencyItem, Reaction
from typing import Union
import random
import time
from highrise import BaseBot, Highrise, Position, AnchorPosition, Reaction
from highrise import __main__
from asyncio import run as arun
import asyncio
from random import choice
import json
from typing import List
from datetime import datetime, timedelta
from highrise.models import SessionMetadata
import re
from highrise.models import SessionMetadata, User, Item, Position, CurrencyItem, Reaction
from typing import Any, Dict, Union
import random
import time
from highrise import BaseBot, Highrise, Position, AnchorPosition, Reaction
from highrise import __main__
from asyncio import run as arun
import asyncio
from random import choice
import json
from typing import List
from datetime import datetime, timedelta
from highrise.models import SessionMetadata
import re

from highrise.models import SessionMetadata, User, Item, Position, CurrencyItem, Reaction
from highrise import BaseBot, Position
from highrise import __main__
from highrise.models import Item
from asyncio import run as arun
from highrise.models import AnchorPosition
import requests
from highrise import BaseBot, __main__
from highrise.models import (AnchorPosition, Item, Position, User,)
from highrise import BaseBot
from collections import UserDict
from highrise.models import SessionMetadata, User
from json import load, dump
from time import time
from math import sqrt
from highrise import BaseBot, User, Position, AnchorPosition
from highrise.models import Position
from highrise.models import SessionMetadata, User, CurrencyItem, Item, AnchorPosition, Reaction, ModerateRoomRequest, Position
import random
from highrise import *
from highrise.models import *
import asyncio
from asyncio import Task
from typing import Union
import asyncio
import contextlib
import random
from typing import Any, Dict, Union
from importlib.machinery import ModuleSpec
from click.decorators import pass_context
from highrise import BaseBot
from typing import Any, Dict, Union
from highrise import *
from highrise.models import *
from asyncio import Task
from highrise.__main__ import *
from emotes import Emotes
import asyncio
import contextlib
import random
from typing import Any, Dict, Union
from importlib.machinery import ModuleSpec
from click.decorators import pass_context
from highrise import BaseBot
from typing import Any, Dict, Union
from highrise import *
from highrise.models import *
from asyncio import Task
from highrise.__main__ import *
from highrise.models import (
    AnchorPosition,
    Item,
    Position,
    SessionMetadata,
    User,
)
from highrise.models import (
    CurrencyItem,
    GetMessagesRequest,
    Item,
    SessionMetadata,
)
import random
import requests
import os
import importlib
import asyncio
import contextlib
import logging
from highrise import BaseBot, AnchorPosition, Position, User, TaskGroup
moderator = ['Alionardo_','siyanda_mathole']
co_mod = ['Alionardo_','siyanda_mathole']

class BotDefinition:
    def __init__(self, bot, room_id, api_token):
        self.bot = bot
        self.room_id = room_id
        self.api_token = api_token
class ResponseError(Exception):
  pass

class Counter:
    bot_id = ""
    static_ctr = 0
    usernames = ['Alionardo_']

class MyBot(BaseBot):
    continuous_emote_tasks: Dict[int, asyncio.Task[Any]] = {}  
    user_data: Dict[int, Dict[str, Any]] = {}
    continuous_emote_task = None
    cooldowns = {}  # Class-level variable to store cooldown timestamps
    emote_looping = False
    def __init__(self):
      super().__init__()
      self.maze_players = {}
      self.user_points = {}  # Dictionary to store user points
    
      self.Emotes = Emotes
      self.should_stop = False
        
    async def on_start(self, SessionMetadata: SessionMetadata) -> None:
        try:
            
            await self.highrise.walk_to(Position(17, 0,2, "FrontRight"))
            await asyncio.sleep(3)
            await self.highrise.chat(" on duty!")
            item = await self.webapi.get_items(item_name="Top Knot") 
            item_id = item.items[0].item_id
            print(item_id)
        except Exception as e:
            print(f"error : {e}")

    async def send_continuous_emote(self, emote_text ,user_id,emote_time):
      try:
          while True:                    
                tasks = [asyncio.create_task(self.highrise.send_emote(emote_text, user_id))]
                await asyncio.wait(tasks)
                await asyncio.sleep(emote_time)
                await asyncio.sleep(1)
      except Exception as e:
                print(f"{e}")

  
    async def stop_continuous_emote(self, user_id: int):
      if user_id in self.continuous_emote_tasks and not self.continuous_emote_tasks[user_id].cancelled():
          task = self.continuous_emote_tasks[user_id]
          task.cancel()
          with contextlib.suppress(asyncio.CancelledError):
              await task
          del self.continuous_emote_tasks[user_id]
    async def on_user_join(self, user: User, position: Position | AnchorPosition) -> None:
        try:     
            await self.highrise.send_whisper(user.id,f"Hey {user.username}\nwelcome to ️@siyanda_mathole party \nMake sure to follow @siyanda_mathole , your host & your amazing dj!\nVIP is 100g to bot! \n• !list or -list or -help :To check commands, \n for bots pm @Alionardo_")
        except Exception as e:
            print(f"error : {e}")
    async def teleport_user_next_to(self, target_username: str, requester_user: User):
      room_users = await self.highrise.get_room_users()
      requester_position = None

      for user, position in room_users.content:
        if user.id == requester_user.id:
            requester_position = position
            break
      for user, position in room_users.content:
        if user.username.lower() == target_username.lower(): 
          z = requester_position.z 
          new_z = z + 1 

          user_dict = {
            "id": user.id,
            "position": Position(requester_position.x, requester_position.y, new_z, requester_position.facing)
          }
          await self.highrise.teleport(user_dict["id"], user_dict["position"])
    async def on_tip(self, sender: User, receiver: User, tip: CurrencyItem) -> None:
            print(f"{sender.username} tipped {receiver.username} an amount of {tip.amount}")
            await self.highrise.chat(f"Our {sender.username} tipped {receiver.username} amount of {tip.amount}𝐆𝐎𝐋𝐃")

            if receiver.id  == Counter.bot_id:
              if tip.amount == 100:
                   await self.highrise.teleport(sender.id, Position(14,10.25,14.5))
    async def on_reaction(self, user: User, reaction: Reaction, receiver: User) -> None:
    
      if reaction =="wink" and user.username in moderator:
         target_username = receiver.username
         await self.teleport_user_next_to(target_username, user)
      
      if user.username in moderator and reaction == "wave":
          await self.highrise.moderate_room(receiver.id, "kick")
          await self.highrise.chat(f"{receiver.username} is Kicked by {user.username}")
      if user.username in moderator and reaction == "heart":
          await self.highrise.teleport(receiver.id, Position(14,10.25,14.5))
   
    async def on_chat(self, user: User, message: str):
        try:
            if message.lower().lstrip().startswith(("-list", "!list","-help")):
                await self.highrise.chat("\\commands you can use:\n• !emotes or -emotes\n• !loops or -loops \n• -buy or !buy for \n 🎫VIP Tickets🎫 \n• !rules or -rules")
            if message.lower().lstrip().startswith(("-buy" , "!buy")):
                await self.highrise.chat(f"\n  vip = 100g for vip 🎫 \nTip 100 to bot you will be teleported instantly. ")
         
            if message.lower().lstrip().startswith(("-emotes", "!emotes")):
                await self.highrise.send_whisper(user.id, "\n• Emote can be used by NUMBERS")
                await self.highrise.send_whisper(user.id, "\n• For loops say -loop or !loop then the emote number.")         
            if message.lower().lstrip().startswith(("!loop","-loop")):
                await self.highrise.send_whisper(user.id,"\n• loops\n ____________________________\nMention loop before the emote numer\n ____________________________")
            if message.lower().lstrip().startswith(("-teleport", "!teleport")):
                    await self.highrise.chat(f"\n • Teleports\n ____________________________\n-host : (only mods ) \n-g : Ground floor \n-dj : DJ setup (only mods and dj)  \n-vip or -v : (vip only), make sure you have 🎫VIP Tickets 🎫 \n• type -buy or !buy for details ")
            if message.lower().lstrip().startswith(("!rules", "-rules")):
                   await self.highrise.chat(f"\n\n        RULES\n ____________________________\n 1. NO UNDERAGE \n 2. No advertising\n 3. No hate speech \n 4. No begging (those trash will be immediately banned 🚫) \n 5. No spamming ")
            if message.startswith("-vip")and user.username in co_mod:                              
              await self.highrise.teleport(user.id, Position(14,10.25,14.5))
            if message.startswith("-dj")and user.username in co_mod:                    
              await self.highrise.teleport(user.id, Position(16.5,9.25,3.5)) 
            if message.startswith("-g"):           
              await self.highrise.teleport(user.id, Position(15,0, 5)) 
            if message.startswith("-host")and user.username in co_mod:                              
              await self.highrise.teleport(user.id, Position(5.5,9.5,6))
            if message.lstrip().startswith(("!vip","!g","!dj","!host")):
                response = await self.highrise.get_room_users()
                users = [content[0] for content in response.content]
                usernames = [user.username.lower() for user in users]
                parts = message[1:].split()
                args = parts[1:]

                if len(args) < 1:
                    await self.highrise.send_whisper(user.id, f"Kullanım: !{parçalar[0]} <@Alionardo_>")
                    return
                elif args[0][0] != "@":
                    await self.highrise.send_whisper(user.id, "Invalid user format. Please use '@username'.")
                    return
                elif args[0][1:].lower() not in usernames:
                    await self.highrise.send_whisper(user.id, f"{args[0][1:]} is not in the room.")
                    return

                user_id = next((u.id for u in users if u.username.lower() == args[0][1:].lower()), None)
                if not user_id:
                    await self.highrise.send_whisper(user.id, f"User {args[0][1:]} not found")
                    return                     
                try:
                    if message.startswith("!vip")and user.username in co_mod:                              
                        await self.highrise.teleport(user_id, Position(14,10.25,14.5))
                    if message.startswith("!dj")and user.username in co_mod:                    
                        await self.highrise.teleport(user_id, Position(16.5,9.25,3.5))
                    if message.startswith("!g")and user.username in co_mod:           
                        await self.highrise.teleport(user_id, Position(15,0, 5)) 
                    if message.startswith("!host")and user.username in co_mod:                              
                        await self.highrise.teleport(user_id, Position(5.5,9.5,6))
                except Exception as e:
                    print(f"An exception occurred[Due To {parts[0][1:]}]: {e}")

            if message.lower().startswith("loop"):
               parts = message.split()
               E = parts[1]
               E = int(E)
               emote_text, emote_time = await self.get_emote_E(E)
               emote_time -= 1
               user_id = user.id  
               if user.id in self.continuous_emote_tasks and not self.continuous_emote_tasks[user.id].cancelled():
                  await self.stop_continuous_emote(user.id)
                  task = asyncio.create_task(self.send_continuous_emote(emote_text,user_id,emote_time))
                  self.continuous_emote_tasks[user.id] = task
               else:
                  task = asyncio.create_task(self.send_continuous_emote(emote_text,user_id,emote_time))
                  self.continuous_emote_tasks[user.id] = task  

            elif message.lower().startswith("stop"):
               if user.id in self.continuous_emote_tasks and not self.continuous_emote_tasks[user.id].cancelled():
                  await self.stop_continuous_emote(user.id)
                  await self.highrise.chat("Continuous emote has been stopped.")
               else:
                  await self.highrise.chat("You don't have an active loop_emote.")
            elif message.lower().startswith("users"):
                room_users = (await self.highrise.get_room_users()).content
                await self.highrise.chat(f"There are {len(room_users)} users in the room")
        
            if  message.isdigit() and 1 <= int(message) <= 91:
                parts = message.split()
                E = parts[0]
                E = int(E)
                emote_text, emote_time = await self.get_emote_E(E)    
                tasks = [asyncio.create_task(self.highrise.send_emote(emote_text, user.id))]
                await asyncio.wait(tasks)
            
            
            if message == "!tip1":
              if user.username in moderator:
                roomUsers = (await self.highrise.get_room_users()).content
                for roomUser, _ in roomUsers:
                  await self.highrise.tip_user(roomUser.id, "gold_bar_1")

            elif message == "!tip5":
              if user.username in moderator:
                roomUsers = (await self.highrise.get_room_users()).content
                for roomUser, _ in roomUsers:
                  await self.highrise.tip_user(roomUser.id, "gold_bar_5")

            elif message == "!tip10":
              if user.username in moderator:
                roomUsers = (await self.highrise.get_room_users()).content
                for roomUser, _ in roomUsers:
                  await self.highrise.tip_user(roomUser.id, "gold_bar_10")

            elif message == "!tip50":
              if user.username in moderator:
                roomUsers = (await self.highrise.get_room_users()).content
                for roomUser, _ in roomUsers:
                  await self.highrise.tip_user(roomUser.id, "gold_bar_50")


            if message.lower().startswith("wallet"):
                if user.username in moderator:
                  wallet = (await self.highrise.get_wallet()).content
                  await self.highrise.send_whisper(user.id, f"The bot wallet contains {wallet[0].amount} {wallet[0].type}")


            if message == "!fit0077": 
               shirt = ["shirt-n_starteritems2019tankwhite", "shirt-n_starteritems2019tankblack", "shirt-n_starteritems2019raglanwhite", "shirt-n_starteritems2019raglanblack", "shirt-n_starteritems2019pulloverwhite", "shirt-n_starteritems2019pulloverblack", "shirt-n_starteritems2019maletshirtwhite", "shirt-n_starteritems2019maletshirtblack", "shirt-n_starteritems2019femtshirtwhite", "shirt-n_starteritems2019femtshirtblack", "shirt-n_room32019slouchyredtrackjacket", "shirt-n_room32019malepuffyjacketgreen", "shirt-n_room32019longlineteesweatshirtgrey", "shirt-n_room32019jerseywhite", "shirt-n_room32019hoodiered", "shirt-n_room32019femalepuffyjacketgreen", "shirt-n_room32019denimjackethoodie", "shirt-n_room32019croppedspaghettitankblack", "shirt-n_room22109plaidjacket", "shirt-n_room22109denimjacket", "shirt-n_room22019tuckedtstripes", "shirt-n_room22019overalltop", "shirt-n_room22019denimdress", "shirt-n_room22019bratoppink", "shirt-n_room12019sweaterwithbuttondowngrey", "shirt-n_room12019cropsweaterwhite", "shirt-n_room12019cropsweaterblack", "shirt-n_room12019buttondownblack", "shirt-n_philippineday2019filipinotop", "shirt-n_flashysuit", "shirt-n_SCSpring2018flowershirt", "shirt-n_2016fallblacklayeredbomber", "shirt-n_2016fallblackkknottedtee", "shirt-f_skullsweaterblack", "shirt-f_plaidtiedshirtred", "shirt-f_marchingband"]
               pant = ["shorts-f_pantyhoseshortsnavy", "pants-n_starteritems2019mensshortswhite", "pants-n_starteritems2019mensshortsblue", "pants-n_starteritems2019mensshortsblack", "pants-n_starteritems2019cuffedshortswhite", "pants-n_starteritems2019cuffedshortsblue", "pants-n_starteritems2019cuffedshortsblack", "pants-n_starteritems2019cuffedjeanswhite", "pants-n_starteritems2019cuffedjeansblue", "pants-n_starteritems2019cuffedjeansblack", "pants-n_room32019rippedpantswhite", "pants-n_room32019rippedpantsblue", "pants-n_room32019longtrackshortscamo", "pants-n_room32019longshortswithsocksgrey", "pants-n_room32019longshortswithsocksblack", "pants-n_room32019highwasittrackshortsblack", "pants-n_room32019baggytrackpantsred", "pants-n_room32019baggytrackpantsgreycamo", "pants-n_room22019undiespink", "pants-n_room22019undiesblack", "pants-n_room22019techpantscamo", "pants-n_room22019shortcutoffsdenim", "pants-n_room22019longcutoffsdenim", "pants-n_room12019rippedpantsblue", "pants-n_room12019rippedpantsblack", "pants-n_room12019formalslackskhaki", "pants-n_room12019formalslacksblack", "pants-n_room12019blackacidwashjeans", "pants-n_2016fallgreyacidwashjeans"]
               item_top = random.choice(shirt)
               item_bottom = random.choice(pant)
               xox = await self.highrise.set_outfit(outfit=[
                Item(type='clothing', amount=1, id= item_top, account_bound=False, active_palette=-1), 
                Item(type='clothing', amount=1, id=item_bottom, account_bound=False, active_palette=-1),
                Item(type='clothing', amount=1, id='body-flesh', account_bound=False, active_palette=65),     
                      Item(type='clothing', amount=1, id='nose-n_01', account_bound=False, active_palette=-1),
                      Item(type='clothing', amount=1, id='watch-n_room32019blackwatch', account_bound=False, active_palette=-1),
                 Item(type='clothing', amount=1, id='watch-n_room32019blackwatch', account_bound=False, active_palette=-1),
                      Item(type='clothing', amount=1, id='shoes-n_room12019sneakersblack', account_bound=False, active_palette=-1),    
                Item(type='clothing', amount=1, id='freckl-n_sharpfaceshadow', account_bound=False, active_palette=-1),
                 Item(type='clothing', amount=1, id='freckle-n_basic2018freckle22', account_bound=False, active_palette=-1),
                      Item(type='clothing', amount=1, id='mouth-basic2018fullpeaked', account_bound=False, active_palette=3),
                      Item(type='clothing', amount=1, id='hair_front-n_basic2020overshoulderpony', account_bound=False, active_palette=1),
                      Item(type='clothing', amount=1, id='hair_back-n_basic2020overshoulderpony', account_bound=False, active_palette=1),
                      Item(type='clothing', amount=1, id='eye-n_basic2018heavymascera', account_bound=False, active_palette=36),
                      Item(type='clothing', amount=1, id='eyebrow-n_basic2018newbrows09', account_bound=False, active_palette=-1)
              ])
               await self.highrise.chat(f"{xox}") 

            else:
                return
        except Exception as e:
            print(f"Error : {e}")





async def run(self, room_id, token):
        definitions = [BotDefinition(self, room_id, token)]
        await __main__.main(definitions)
