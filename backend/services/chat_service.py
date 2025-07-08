import json

from clients.openai_client import client

class Chatservice:

    async def generar_chat(self):
        completion = client.chat.completions.create(
            model= "gpt-4.1-nano",
            messages=[
                {"role": "developer", "content": "Te llamas Nina, eres una asistente de la empesa AdserIQ, presentate como tal"},
                {"role": "user", "content": "Hola, como estas"}
            ],
            stream= True
        )

        respuesta = ""
        for chunk in completion:
            delta = chunk.choices[0].delta
            finish_reason = chunk.choices[0].finish_reason

            if delta.content:
                respuesta += delta.content
                print(respuesta)
                yield json.dumps({"content": delta.content}) + "\n"
            if finish_reason is not None:
                yield json.dumps({"finish_reason" : finish_reason}) + "\n"
                break

        #return (completion.choices[0].message.content)