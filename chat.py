import os
from groq import Groq

from dotenv import load_dotenv
load_dotenv()

# in pytohn class names are in CamelCase;
# non-class names (e.g. functions/variables) are in snake_case
class Chat:
    '''
    >>> chat = Chat()
    >>> chat.send_message('my name is bob', temperature=0.0)
    "Hello Bob, it's nice to meet you."
    >>> def monkey_input(prompt, user_inputs=['Hello, I am monkey.', 'Goodbye.']):
    ...     try:
    ...         user_input = user_inputs.pop(0)
    ...         print(f'{prompt}{user_input}')
    ...         return user_input
    ...     except IndexError:
    ...         raise KeyboardInterrupt
    >>> import builtins
    >>> builtins.input = monkey_input
    >>> repl(temperature=0.0)
    chat> Hello, I am monkey.
    Hello Monkey, it's nice to meet you.
    chat> Goodbye.
    Goodbye Monkey, have a great day.
    <BLANKLINE>
    '''
    client = Groq()
    def __init__(self):
        self.messages = [
                {
                    # most important content for sys prompt is length of response
                    "role": "system",
                    "content": "Write the output in 1-2 sentences."
                },
            ]
    def send_message(self, message, temperature=0.8):
        self.messages.append(
            {
                'role': 'user',
                'content': message
            }
        )
        chat_completion = self.client.chat.completions.create(
            messages=self.messages,
            model="llama-3.1-8b-instant",
            temperature=temperature,
        )
        result = chat_completion.choices[0].message.content
        self.messages.append({
            'role': 'assistant',
            'content': result
        })
        return result

def repl(temperature=0.8):
    import readline
    chat = Chat()
    try:
        while True:
            user_input = input('chat> ')
            response = chat.send_message(user_input, temperature = temperature)
            print(response)
    except KeyboardInterrupt:
        print()

if __name__ == '__main__':
    repl()