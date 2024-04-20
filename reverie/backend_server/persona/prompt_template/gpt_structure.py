"""
Author: shuzhen Zhang (joonspk@stanford.edu)
Revised

File: gpt_structure.py
Description: Wrapper functions for calling Mixstral APIs. 
"""

import json
import random
# import openai
import time 
import anthropic
from anthropic import _tokenizers
#-------------------------------------------------------------------------------
import API as pt
#-------------------------------------------------------------------------------
import sys
sys.path.append("reverie/backend_server/")

from utils import *

# openai.api_key = openai_api_key

def temp_sleep(seconds=15):
  time.sleep(seconds)

def ChatGPT_single_request(prompt): 
  temp_sleep()

  return LLM(prompt)


# ============================================================================
# #####################[SECTION 1: CHATGPT-3 STRUCTURE] ######################
# ============================================================================

# ALL changed from GPT--------------------------------------------------------------------------------

# 1 for Mixtral, 2 for Claude, 3 for Mistral
def LLM(prompt, Model=1): 
  """
  Given a prompt and a dictionary of GPT parameters, make a request to OpenAI
  server and returns the response. 
  ARGS:
    prompt: a str prompt 
  RETURNS: 
    a str of Mixtral's response. 
  """
  temp_sleep()
  Model=2
  try: 
    prompt="In the follwoing task, give answer only, no explaination! don't be verbose! \n"+prompt
    if Model==1:
      output= (pt.Claude_3(prompt).content[0].text).rstrip()
    else:
      output= (pt.send(prompt,1)["content"]).rstrip()
    return output.strip()
  
  except: 
    print ("LLM ERROR")
    return "LLM ERROR"
  

# def ChatGPT_request(prompt): 
#   """
#   Given a prompt and a dictionary of GPT parameters, make a request to OpenAI
#   server and returns the response. 
#   ARGS:
#     prompt: a str prompt
#     gpt_parameter: a python dictionary with the keys indicating the names of  
#                    the parameter and the values indicating the parameter 
#                    values.   
#   RETURNS: 
#     a str of GPT-3's response. 
#   """
#   # temp_sleep()
#   try: 
#     output= (pt.send(prompt)["content"]).rstrip()
#     return output.strip()
  
#   except: 
#     print ("Lama ERROR")
#     return "Lama ERROR"
# ----------------------------------------------------------------------------------------------------------------

# def GPT4_safe_generate_response(prompt, 
#                                    example_output,
#                                    special_instruction,
#                                    repeat=3,
#                                    fail_safe_response="error",
#                                    func_validate=None,
#                                    func_clean_up=None,
#                                    verbose=False,
#                                    model=1): 
#   prompt = 'GPT-3 Prompt:\n"""\n' + prompt + '\n"""\n'
#   prompt += f"Output the response to the prompt above in json. {special_instruction}\n"
#   prompt += "Example output json:\n"
#   prompt += '{"output": "' + str(example_output) + '"}'

#   if verbose: 
#     print ("CHAT GPT PROMPT")
#     print (prompt)

#   for i in range(repeat): 

#     try: 
#       if i>2:
#         model=1
#       curr_gpt_response = LLM(prompt,Model=model).strip()
#       end_index = curr_gpt_response.rfind('}') + 1
#       curr_gpt_response = curr_gpt_response[:end_index]
#       curr_gpt_response = json.loads(curr_gpt_response)["output"]
      
#       if func_validate(curr_gpt_response, prompt=prompt): 
#         return func_clean_up(curr_gpt_response, prompt=prompt)
      
#       if verbose: 
#         print ("---- repeat count: \n", i, curr_gpt_response)
#         print (curr_gpt_response)
#         print ("~~~~")

#     except: 
#       pass

#   return False


def ChatGPT_safe_generate_response(prompt, 
                                   example_output,
                                   special_instruction,
                                   repeat=5,
                                   fail_safe_response="error",
                                   func_validate=None,
                                   func_clean_up=None,
                                   verbose=False,
                                   model=1): 

  # prompt = 'GPT-3 Prompt:\n"""\n' + prompt + '\n"""\n'
  prompt = '"""\n' + prompt + '\n"""\n'
  prompt += f"Output the response to the prompt above in json. {special_instruction}\n"
  prompt += "Example output json:\n"
  prompt += '{"output": "' + str(example_output) + '"}'

  if verbose: 
    print ("CHAT GPT PROMPT")
    print (prompt)

  for i in range(repeat): 

    try: 
      if i>2:
        model=1
      curr_gpt_response = LLM(prompt,Model=model).strip()
      end_index = curr_gpt_response.rfind('}') + 1
      curr_gpt_response = curr_gpt_response[:end_index]
      curr_gpt_response = json.loads(curr_gpt_response)["output"]
      # print(curr_gpt_response)
      # print ("---ashdfaf")
      # print (curr_gpt_response)
      # print ("000asdfhia")
      
      if func_validate(curr_gpt_response, prompt=prompt): 
        return func_clean_up(curr_gpt_response, prompt=prompt)
      
      if verbose: 
        print ("---- repeat count: \n", i, curr_gpt_response)
        print (curr_gpt_response)
        print ("~~~~")

    except: 
      pass

  return False


def ChatGPT_safe_generate_response_OLD(prompt, 
                                   repeat=3,
                                   fail_safe_response="error",
                                   func_validate=None,
                                   func_clean_up=None,
                                   verbose=False,
                                   model=1): 
  if verbose: 
    print ("CHAT GPT PROMPT")
    print (prompt)

  for i in range(repeat): 
    try: 
      if i>2:
        model=1
      curr_gpt_response = LLM(prompt,Model=model).strip()
      if func_validate(curr_gpt_response, prompt=prompt): 
        return func_clean_up(curr_gpt_response, prompt=prompt)
      if verbose: 
        print (f"---- repeat count: {i}")
        print (curr_gpt_response)
        print ("~~~~")

    except: 
      pass
  print ("FAIL SAFE TRIGGERED") 
  return fail_safe_response


# ============================================================================
# ###################[SECTION 2: ORIGINAL GPT-3 STRUCTURE] ###################
# ============================================================================

# def GPT_request(prompt): 
#   """
#   Given a prompt and a dictionary of GPT parameters, make a request to OpenAI
#   server and returns the response. 
#   ARGS:
#     prompt: a str prompt
#     gpt_parameter: a python dictionary with the keys indicating the names of  
#                    the parameter and the values indicating the parameter 
#                    values.   
#   RETURNS: 
#     a str of GPT-3's response. 
#   """
#   temp_sleep()
#   try: 
#     output= (pt.send(prompt)["content"]).rstrip()
#     return output.strip()
#   except: 
#     print ("Llama ERROR")
#     return "Llama ERROR"


def generate_prompt(curr_input, prompt_lib_file): 
  """
  Takes in the current input (e.g. comment that you want to classifiy) and 
  the path to a prompt file. The prompt file contains the raw str prompt that
  will be used, which contains the following substr: !<INPUT>! -- this 
  function replaces this substr with the actual curr_input to produce the 
  final promopt that will be sent to the GPT3 server. 
  ARGS:
    curr_input: the input we want to feed in (IF THERE ARE MORE THAN ONE
                INPUT, THIS CAN BE A LIST.)
    prompt_lib_file: the path to the promopt file. 
  RETURNS: 
    a str prompt that will be sent to OpenAI's GPT server.  
  """
  if type(curr_input) == type("string"): 
    curr_input = [curr_input]
  curr_input = [str(i) for i in curr_input]

  f = open(prompt_lib_file, "r")
  prompt = f.read()
  f.close()
  for count, i in enumerate(curr_input):   
    prompt = prompt.replace(f"!<INPUT {count}>!", i)
  if "<commentblockmarker>###</commentblockmarker>" in prompt: 
    prompt = prompt.split("<commentblockmarker>###</commentblockmarker>")[1]
  return prompt.strip()


def safe_generate_response(prompt, 
                           repeat=5,
                           fail_safe_response="error",
                           func_validate=None,
                           func_clean_up=None,
                           verbose=False,
                           model=1): 
  if verbose: 
    print (prompt)

  for i in range(repeat): 
    if i>2:
      model=1
    curr_gpt_response = LLM(prompt,Model=model)
    print("Detect:----------------------------------",curr_gpt_response)
    if func_validate(curr_gpt_response,prompt=prompt): 
      print("PASS") 
      return func_clean_up(curr_gpt_response,prompt=prompt)
    if verbose: 
      print ("---- repeat count: ", i, curr_gpt_response)
      print (curr_gpt_response)
      print ("~~~~")
  return fail_safe_response

# ============================================================================ changed tokenizer 
from transformers import AutoTokenizer
def get_embedding(text, model="mistralai/Mixtral-8x7B-Instruct-v0.1", Claude="claude-3-haiku-20240307"):
  text = text.replace("\n", " ")
  # if LLM == 1:
  tokenizer = AutoTokenizer.from_pretrained(model)
  # elif LLM == 2:
  #   tokenizer = _tokenizers.get_tokenizer(Claude)
  if not text: 
    text = "this is blank"
  
  return tokenizer(text, return_tensors="pt")['input_ids'][0].tolist()
  #--------------------------------------------------
  # return openai.Embedding.create(
  #         input=[text], model=model)['data'][0]['embedding']

# test="tell me a 50 words story"
# print(LLM(test,Model=1))
# print(LLM(test,Model=2))


if __name__ == '__main__':
  curr_input = ["driving to a friend's house"]
  prompt_lib_file = "reverie/backend_server/persona/prompt_template/v1/test_prompt_July5.txt"
  prompt = generate_prompt(curr_input, prompt_lib_file)

  def __func_validate(gpt_response): 
    if len(gpt_response.strip()) <= 1:
      return False
    if len(gpt_response.strip().split(" ")) > 1: 
      return False
    return True
  def __func_clean_up(gpt_response):
    cleaned_response = gpt_response.strip()
    return cleaned_response

  output = safe_generate_response(prompt, 
                                 5,
                                 "rest",
                                 __func_validate,
                                 __func_clean_up,
                                 True)

  print (output)




















