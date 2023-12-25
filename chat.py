from openai import OpenAI
from config import config


class Chat:
    
    def __init__(self, config: dict):
        self.__client = OpenAI(api_key=config['OPENAI_API_KEY'])
        self.__model = config['GPT_MODEL']
        self.__max_tokens = config['MAX_TOKENS']

  
    async def get_chat_response(self, system_message: str, user_request: str, seed: int = None):
        try:
            messages = [
                {"role": "system", "content": system_message},
                {"role": "user", "content": user_request},
            ]
            
            response = self.__client.chat.completions.create(
                model=self.__model,
                messages=messages,
                seed=seed,
                max_tokens=self.__max_tokens,
                temperature=0.7
            )
            
            return response.choices[0].message.content
        
        except Exception as e:
            print(f"An error occurred: {e}")
            
            return None