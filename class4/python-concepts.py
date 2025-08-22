# SOME BASICS PYTHON CONCEPTS

# import asyncio
# flate written

# with open("data.txt", "r+") as f, open("new.txt", "w") as otput_file:
#     data = f.read()
#     otput_file.write(data.upper())
#     print(data,"Data written to new.txt")



# async

# from contextlib import asynccontextmanager
# from multiprocessing.dummy import connection

# @asynccontextmanager
# async def make_connection(name):
#     print(f"Establishing connection.... {name}")
#     yield name
#     print(f"Closing connection! {name}")

# async def main():
#     async with make_connection("A") as a:
#         print(f"Using connection {a}")

# asyncio.run(main())


# async def get_connection(name):
#     class Ctx():
#         async def __aenter__(self):
#             print(f"Establishing connection.... {name}")
#             return name

#         async def __aexit__(self, exc_type, exc_val, exc_tb):
#             print(f"Closing connection! {name}")

#     return Ctx()

# async def main():
#     async with await get_connection("A") as a:
#         async with await get_connection("B") as b:
#             print(f"Using connection {a} and {b}")

# from contextlib import AsyncExitStack
# async def main():
#     async with AsyncExitStack() as stack:
#         a = await stack.enter_async_context(await get_connection("A"))
#         if a == "A":
#             b = await stack.enter_async_context(await get_connection("B"))
#             print(f"Using connection {a} and {b}")

#         async def custom_cleanup():
#             print("Custom cleanup actions")

#         stack.push_async_callback(custom_cleanup)
        # locals ka matlab hota hey agar a == "A" hamesha na ho tab bhi code crash nhi hoga blkey None ki value key sath run ho jaye ga like this 
        # Establishing connection.... A
        # Doing work with A and maybe None
        # Custom cleanup actions
        # Closing connection! A

        # while without locals  code will be crashed
#         print(f"Doing work with {a} and maybe {locals().get('b')}")
#         await asyncio.sleep(1)  # Simulate some async work

# asyncio.run(main())

