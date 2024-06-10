#KerbalBot V1 - the original code, plus some error handling
#----------------------------------------------

#from keep_alive import keep_alive
# the os module helps us access environment variables
# i.e., our API keys
#import os

# these modules are for querying the Hugging Face model
#import json
#import requests

# the Discord Python API
#import discord

# this is my Hugging Face profile link
#API_URL = 'https://api-inference.huggingface.co/models/MisguidedKerbal/'

#class MyClient(discord.Client):

#def __init__(self, model_name):
# adding intents module to prevent intents error in __init__ method in newer versions of Discord.py
#intents = discord.Intents.default(
#)  # Select all the intents in your bot settings as it's easier
#intents.message_content = True

#super().__init__(intents=intents)
#self.api_endpoint = API_URL + model_name
# retrieve the secret API token from the system environment
#huggingface_token = os.environ['HUGGINGFACE_TOKEN']
# format the header in our request to Hugging Face
#self.request_headers = {
#'Authorization': 'Bearer {}'.format(huggingface_token)
#}

#def query(self, payload):

#make request to the Hugging Face model API

#data = json.dumps(payload)
#response = requests.request('POST',
#self.api_endpoint,
#headers=self.request_headers,
#data=data)
#ret = json.loads(response.content.decode('utf-8'))
#return ret

#def query(self, payload):
#make request to the Hugging Face model API

#data = json.dumps(payload)
#response = requests.request('POST',
#self.api_endpoint,
#headers=self.request_headers,
#data=data)
# Check if the request was successful (status code 200)
#if response.status_code == 200:
#try:
#ret = json.loads(response.content.decode('utf-8'))
#return ret
#except json.JSONDecodeError as e:
#print(f"Error decoding JSON response: {e}")
#print(f"Response content: {response.content}")
#return {'error': 'Error decoding JSON response.'}
#else:
#print(f"API request failed with status code:     {response.status_code}")
#print(f"Response content: {response.content}")
#return {
#'error':
#f'API request failed with status code: {response.status_code}. {response.content}'
#}

#async def on_ready(self):
# print out information when the bot wakes up
#print('Logged in as')
#print(self.user.name)
#print(self.user.id)
#print('------')

# send a request to the model without caring about the   response, just so that the model wakes up and starts loading
#self.query({'inputs': {'text': 'Hello!'}})

#async def on_message(self, message):
#this function is called whenever the bot sees a message in a channel

# ignore the message if it comes from the bot itself
#if message.author.id == self.user.id:
#return

# form query payload with the content of the message
#payload = {'inputs': {'text': message.content}}

# while the bot is waiting on a response from the model
# set the its status as typing for user-friendliness
#async with message.channel.typing():
#response = self.query(payload)
#bot_response = response.get('generated_text', None)

# we may get ill-formed response if the model hasn't fully loaded or has timed out
#if not bot_response:
#if 'error' in response:
#bot_response = '`Error: {}`'.format(response['error'])
#else:
#bot_response = 'Hmm... something is not right.'

# send the model's response to the Discord channel
#await message.channel.send(bot_response)

#def main():
# DialoGPT-kerbalV2 is my model name
#client = MyClient('DialoGPT-medium-kerbal')
#client = MyClient('DialoGPT-kerbalV2')
#client = MyClient('DialoGPT-kerbalV3')

#keep_alive()
#client.run(os.environ['DISCORD_TOKEN'])

#if __name__ == '__main__':
#  main()
#----------------------------------------------

#KerbalBot V2 - appears to have fixed huggingface API call exceptions, but results in some strange behavior.
#----------------------------------------------

#from keep_alive import keep_alive
#import os
#import json
#import requests
#import discord

#API_URL = 'https://api-inference.huggingface.co/models/MisguidedKerbal/'

#class MyClient(discord.Client):

#def __init__(self, model_name):
#intents = discord.Intents.default()
#intents.message_content = True
#super().__init__(intents=intents)
#self.api_endpoint = API_URL + model_name
#huggingface_token = os.environ['HUGGINGFACE_TOKEN']
#self.request_headers = {
#'Authorization': 'Bearer {}'.format(huggingface_token),
#'Content-Type': 'application/json'
#}

#def query(self, payload):
#data = json.dumps(payload)
#response = requests.post(self.api_endpoint,
#headers=self.request_headers,
#data=data)
#if response.status_code == 200:
#try:
#ret = json.loads(response.content.decode('utf-8'))
#return ret
#except json.JSONDecodeError as e:
#print(f"Error decoding JSON response: {e}")
#print(f"Response content: {response.content}")
#return {'error': 'Error decoding JSON response.'}
#else:
#print(f"API request failed with status code: {response.status_code}")
#print(f"Response content: {response.content}")
#return {
#'error':
#f'API request failed with status code: {response.status_code}. {response.content}'
#}

#async def on_ready(self):
#print('Logged in as')
#print(self.user.name)
#print(self.user.id)
#print('------')
#self.query({'inputs': 'Hello!'})

#async def on_message(self, message):
#if message.author.id == self.user.id:
#return
#payload = {'inputs': message.content}
#async with message.channel.typing():
#response = self.query(payload)
#if isinstance(response, list) and len(response) > 0:
#bot_response = response[0].get('generated_text', None)
#else:
#bot_response = None
#if not bot_response:
#if 'error' in response:
#bot_response = '`Error: {}`'.format(response['error'])
#else:
#bot_response = 'Hmm... something is not right.'
#await message.channel.send(bot_response)

#def main():
#client = MyClient('DialoGPT-kerbalV3')
#keep_alive()
#client.run(os.environ['DISCORD_TOKEN'])

#if __name__ == '__main__':
#main()
#----------------------------------------------

#KerbalBot V3 - many fixes, most important being new message formatting + proper prompting of the model
#----------------------------------------------

from keep_alive import keep_alive
import os
import json
import requests
import discord

API_URL = 'https://api-inference.huggingface.co/models/MisguidedKerbal/'


class MyClient(discord.Client):

  def __init__(self, model_name):
    intents = discord.Intents.default()
    intents.message_content = True
    super().__init__(intents=intents)
    self.api_endpoint = API_URL + model_name
    huggingface_token = os.environ['HUGGINGFACE_TOKEN']
    self.request_headers = {
      'Authorization': 'Bearer {}'.format(huggingface_token),
      'Content-Type': 'application/json'
    }

  def query(self, prompt):
    payload = {'inputs': prompt}
    data = json.dumps(payload)
    response = requests.post(self.api_endpoint,
                             headers=self.request_headers,
                             data=data)
    if response.status_code == 200:
      try:
        ret = json.loads(response.content.decode('utf-8'))
        return ret
      except json.JSONDecodeError as e:
        print(f"Error decoding JSON response: {e}")
        print(f"Response content: {response.content}")
        return {'error': 'Error decoding JSON response.'}
    else:
      print(f"API request failed with status code: {response.status_code}")
      print(f"Response content: {response.content}")
      return {
        'error':
        f'API request failed with status code: {response.status_code}. {response.content}'
      }

  async def on_ready(self):
    print('Logged in as')
    print(self.user.name)
    print(self.user.id)
    print('------')
    self.query('Hello!')

  async def on_message(self, message):
    if message.author.id == self.user.id:
      return
    username = message.author.name  # Get the username of the message author
    prompt = f"{message.content}\n"
    async with message.channel.typing():
      response = self.query(prompt)
      print(f"API response: {response}")  # Log the API response
    if isinstance(response, list) and len(response) > 0:
      bot_response = response[0].get('generated_text', None)
    else:
      bot_response = None
    if not bot_response:
      if 'error' in response:
        bot_response = '`Error: {}`'.format(response['error'])
      else:
        bot_response = 'Hmm... something is not right.'
    # Format the response to include the username
    bot_response = f"{username}: {bot_response}"
    await message.channel.send(bot_response)


def main():
  client = MyClient('DialoGPT-kerbalV3')
  keep_alive()
  client.run(os.environ['DISCORD_TOKEN'])


if __name__ == '__main__':
  main()
