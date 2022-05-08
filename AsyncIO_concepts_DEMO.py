import asyncio
import random

class DBConnection:
    def __init__(self)-> None:
        self.__connectionId= random.randint(12,45)

    def get_connectionId(self)-> int :
        return self.__connectionId

async def connect_to_DB() -> int:
    DBConnection_ins= DBConnection()
    connectionId= DBConnection_ins.get_connectionId()

    await asyncio.sleep(2) # Creating DB instance and getting connectionId takes 2s
    return connectionId

async def DBQuery(key)-> int:
    connectionId= await connect_to_DB() # First Connect to DB and get connectionId 
    print( "Connection ID: {}".format(connectionId) )

    await asyncio.sleep(2) # Reading from DB takes 2s time
    value= 100 # Got value= 100 from DB

    print("Value: {}".format(value))    
    return value

async def printNumbers()-> None:
    
    # This is a background task. It runs while all other tasks are not executed by
    # the current process.

    for number in range(100000): 
        if number%100== 0: 
            # We need to give up background task execution after printg 100-length intervals
            # so that high priority processes that were once suspended may resume, if they are ready
            await asyncio.sleep(1)

        print(number)

async def asyncEntry()-> None:
    
    # Entry point for executing co-routines

    primaryKey= int(input("Enter Primary Key: "))
    DBQuery_task= asyncio.create_task(DBQuery(primaryKey))
    backgroundTask= asyncio.create_task(printNumbers())

    # Tasks got created, but we must exit from the function only when all tasks are completed
    # If we do not await for the tasks, after creation of tasks, this co-routine ends and terminates 
    # the current thread, cuz we told the current thread to run only this co-routine.
    value= await DBQuery_task
    await backgroundTask

    print(value)

# Create an event loop and put asyncEntry() in it. The remaining co-routines will get called from 
# in here !!!
asyncio.run(asyncEntry())