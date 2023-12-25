from chat import Chat
from config import config
import asyncio
import os

PRESENTATION_TEXT = """
ESCOLHA UMA DAS OPÇÕES ABAIXO
--------------------------------------------------
- Variações NUMERO ASSUNTO
- Faça um jogo para aprender ASSUNTO
- Explique ASSUNTO
- SAIR para encerrar
--------------------------------------------------
"""

async def main():

    chat = Chat(config)
    
    user_input = input(PRESENTATION_TEXT)
    os.system('cls')
    
    while (user_input != 'SAIR'):

        print('\n\nColetando informações...\n\n')
        chat_response = await chat.get_chat_response(config['SYSTEM_MESSAGE'], user_input)
        
        print(chat_response)
        user_input = input(PRESENTATION_TEXT)

if __name__ == "__main__":
    asyncio.run(main())
