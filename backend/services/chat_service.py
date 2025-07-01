from clients.openai_client import client

class Chatservice:

    async def generar_chat(self):
        completion = client.chat.completions.create(
            model= "gpt-4.1-nano",
            messages=[
                {"role": "developer", "content": "Te llamas Nina, eres una asistente de la empesa AdserIQ, presentate como tal"},
                {"role": "user", "content": "Hola, como estas"}
            ],
            stream= False
        )
        """
        for chunk in completion:
            return (chunk.choices[0].delta)
        """
        return (completion.choices[0].message.content)