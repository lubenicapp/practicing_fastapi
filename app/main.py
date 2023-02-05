import dotenv
from fastapi import FastAPI, Depends

from app.config import get_settings, Settings


dotenv.load_dotenv('.env')

app = FastAPI()


@app.get('/ping')
async def pong(settings: Settings = Depends(get_settings)):
    return {
        'ping': 'pong!',
        'environment': settings.environment,
        'testing': settings.testing
    }
