# temp db for banned 

import database
from config import ADMINS, REPLIT, PING_INTERVAL

import asyncio
import logging
import aiohttp
import traceback


class temp(object): # Eva Maria Idea of Temping
    BOT_USERNAME = None
    CANCEL = False
    FIRST_NAME = None
    START_TIME = None


class AsyncIter:    
    def __init__(self, items):    
        self.items = items    

    async def __aiter__(self):    
        for item in self.items:    
            yield item  

    async def __anext__(self):
        try:
            return next(self.iter)
        except StopIteration:
            raise StopAsyncIteration


async def ping_server():
    sleep_time = PING_INTERVAL
    while True:
        await asyncio.sleep(sleep_time)
        try:
            async with aiohttp.ClientSession(
                timeout=aiohttp.ClientTimeout(total=10)
            ) as session:
                async with session.get(REPLIT) as resp:
                    logging.info("Pinged server with response: {}".format(resp.status))
        except TimeoutError:
            logging.warning("Couldn't connect to the site URL..!")
        except Exception:
            traceback.print_exc()