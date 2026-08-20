import asyncio
import sys

# Psycopg async no funciona con ProactorEventLoop, que es el predeterminado en Windows.
if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
