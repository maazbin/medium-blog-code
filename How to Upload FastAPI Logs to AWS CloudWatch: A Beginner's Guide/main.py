from fastapi import FastAPI

app = FastAPI()

@app.get("/logging")
async def hello_logging():

    # Generate some log messages
    logger.info("----------This is an info message!")
    logger.error("This is an error message!")

    return {"message": "Hello, CloudWatch logging!"}
