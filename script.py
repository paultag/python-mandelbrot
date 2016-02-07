from mandelbrot import directory, aiodirectory

# for expert in directory.experts():
#     print(expert.get('name'))

def experts():
    for expert in (yield from aiodirectory.experts()):
        print(expert.get('name'))

import asyncio

loop = asyncio.get_event_loop()
loop.run_until_complete(experts())
loop.close()
