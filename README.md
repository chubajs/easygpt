# EasyGPT Module README.md

## Overview

The EasyGPT module serves as a convenient Python interface to interact with OpenAI's GPT-3 and GPT-4 models. It simplifies the process of making API requests and interpreting the responses. The module is designed for both developers who are experienced with GPT-3 and those who are just getting started.

**Author:** Sergey Bulaev  
**License:** MIT

- Supports multiple versions of GPT models (GPT-3.5 Turbo, GPT-4)
- In-built token counting with Tiktoken
- Automatic or manual setting of temperature
- Logging support
- Easy-to-use methods for asking questions with or without context
- Price calculation for API usage
- Ability to clear or update context between questions

## Installation

To install this module, you can download the source code and import it into your Python environment. Make sure you also install the required dependencies:
- `openai`
- `tiktoken`
- `logging`

`pip install openai tiktoken`

To install module from GitHub you can use either:

`pip install git+https://github.com/chubajs/easygpt.git`

or 

`pip install git+ssh://git@github.com:chubajs/easygpt.git`


## Usage

### Initialization
Initialize the EasyGPT class by providing the openai instance and the GPT model name you intend to use. You can also optionally set a system message and temperature for the model.

```
import os
import openai
from easygpt import EasyGPT

openai.api_key = os.environ.get('OPENAI_API_KEY')
easy_gpt = EasyGPT(openai, model_name="gpt-4")
```

### Setting Context
If you want to set a context for the conversation, you can do so like this:

`easy_gpt.create_context("Hello, how are you?")`

### Asking Questions
For making queries, you can use `ask` for one-off questions or `ask_with_context` for a series of questions with a set context.

`response, input_price, output_price = easy_gpt.ask("What is the weather?")`

### Processing Responses
Responses can be processed to return the assistant's message, input price, and output price.

`message, input_price, output_price = easy_gpt.process_response(response)`

### Token Calculations
You can calculate the number of tokens required for any message string.

`num_tokens = easy_gpt.tokens_in_string("Your message here")`

## Constants and Pricing
The module contains constants for default stops and system messages, as well as pricing information for different GPT models.

## Supported Models

The module supports a variety of GPT models, including:

- GPT-4
- GPT-4 (32k tokens)
- GPT-3.5 Turbo
- GPT-3.5 Turbo (16k tokens)

For detailed information on each model's pricing, max tokens, temperature, and window size, refer to the `SUPPORTED_MODELS` dictionary in the gptmodels.py.