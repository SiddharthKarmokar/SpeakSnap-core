from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from src.speaksnap import logger
from src.speaksnap.constants import MODEL_NAME, SYSTEM_MESSAGE
from src.speaksnap.utils.common import load_json
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()


class Model:
    def __init__(self, path_to_schema:Path):
        self.chat = ChatGoogleGenerativeAI(model=MODEL_NAME)
        model_schema = load_json(path_to_schema)
        self.model = self.chat.with_structured_output(model_schema)
        self.template = ChatPromptTemplate([
            ('system', SYSTEM_MESSAGE),
            MessagesPlaceholder(variable_name="chat_history"),
            ('human', '{query}')
        ])
        self.chain = self.template | self.model
        logger.info(f"Chain setup complete with response schema\n{model_schema}")

    def invoke_chain(self, query:str, chat_history: str = ""):
        result = self.chain.invoke({"chat_history":[chat_history], "query":query})
        return result
                
