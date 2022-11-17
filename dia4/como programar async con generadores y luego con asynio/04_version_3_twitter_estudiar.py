import time
from asyncio import run, gather, sleep
async def subir_foto():
    print("s: subiendo byte 1")
    await sleep(0)
    print("s: subiendo byte 2")
    await sleep(0)
    print("s: subiendo byte 3")

#@asyncio.coroutine
async def twitter():
    print("t: leyendo a roberto")
    await sleep(0)
    print('t: discutiendo con roberto')
    await sleep(0)
    print('t: postear foto')
    await subir_foto()
    print('t: indignado por politica')

async def estudiar():
    print('e: leyendo el material')
    await sleep(0)
    print('e: armando resumen')
    await sleep(0)
    print('e: leyendo el resumnen')
    print('e: memorizando resumen')
    await sleep(0)
    print('e: llorando')

async def main():
    print('Inicio del programa')
    await gather(twitter(), estudiar())
    print('fin del programa')


run(main())