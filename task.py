import asyncio
async def task(tt):
    loop = asyncio.get_event_loop()
    t=[loop.run_in_executor(None, z) for z in tt]
    r=[await x for x in t]
    return r

def run(t):
    loop = asyncio.get_event_loop()
    return loop.run_until_complete(t)

def run1(t):
    return run(task(t))

