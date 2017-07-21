import psutil

from oshino import Agent


class HWAgent(Agent):

    async def process(self, event_fn):
        logger = self.get_logger()
        cpu_perc = psutil.cpu_percent(interval=None)
        mem = psutil.virtual_memory()

        event_fn(cpu_perc=cpu_perc, mem=mem)
