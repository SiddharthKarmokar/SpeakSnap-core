import os
from pathlib import Path
from fastapi import APIRouter
from src.speaksnap.utils.common import create_directories
from src.speaksnap.utils.langchain_support import save_chat_history, load_chat_history
from src.speaksnap.constants import PATH_TO_CHAT_HISTORY, PATH_TO_MODEL_SCHEMA
from src.speaksnap.entity.user_schemas import TextInput, SummaryResponse
from src.speaksnap.components.model import Model
from src.speaksnap import logger

router = APIRouter()

@router.post("/", response_model=SummaryResponse)
def summarize_text(data: TextInput):
    try:
        if os.path.exists(os.path.join(PATH_TO_CHAT_HISTORY, data.userid, data.sessionid + ".json")):
            chat_history = load_chat_history(os.path.join(PATH_TO_CHAT_HISTORY, data.userid, data.sessionid + ".json"))["chat_history"]
        else:
            create_directories([os.path.join(PATH_TO_CHAT_HISTORY, data.userid)])
            chat_history = ""
        model = Model(PATH_TO_MODEL_SCHEMA)
        response = model.invoke_chain(data.text, chat_history)
        chat_history = response['summary']
        save_chat_history(os.path.join(PATH_TO_CHAT_HISTORY, data.userid, data.sessionid + ".json"), chat_history)
        return SummaryResponse(userid=data.userid, sessionid=data.sessionid, response=response)
    except Exception as e:
        logger.exception(f"exceptions occured while summarizing text: \n{e}")
        raise e