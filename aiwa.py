from flask import Flask, request
import openai

app = Flask(__name__)

API_KEY = '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'
openai.api_key = API_KEY

model_id = 'gpt-3.5-turbo'

@app.route('/chat', methods=['POST'])
def chat():
    # Get input from Landbot
    user_input = request.form.get('user_input')

    # Create conversation list with user input
    conversation = [{'role': 'user', 'content': user_input}]

    # Get ChatGPT response
    conversation = ChatGPT_conversation(conversation)

    # Get ChatGPT response message
    response = conversation[-1]['content']

    # Return response to Landbot
    return response

def ChatGPT_conversation(conversation):
    response = openai.ChatCompletion.create(
        model=model_id,
        messages=conversation
    )
    api_usage = response['usage']
    conversation.append({'role': response.choices[0].message.role, 'content': response.choices[0].message.content})
    return conversation

if __name__ == '__main__':
    app.run()
