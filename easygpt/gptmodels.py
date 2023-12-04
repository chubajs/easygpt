"""
GPTModel Module for EasyGPT

This module defines the GPTModel class for managing GPT models, their
associated costs, and other parameters.

Author: Sergey Bulaev
License: MIT
"""

# Constants
DEFAULT_STOP = None
GPT_DEFAULT_SYSTEM_MESSAGE = ("You are an AI Model trained to serve as a universal assistant "
                              "for helping people find answers to their questions. "
                              "You are working for the project Flashbacks.ai.")

# GPT Model Pricing Information
GPT4_INPUT_PRICE = 0.00003
GPT4_OUTPUT_PRICE = 0.00006
GPT4_32_INPUT_PRICE = 0.00006
GPT4_32_OUTPUT_PRICE = 0.00012

GPT4_PREVIEW_INPUT_PRICE = 0.00001
GPT4_PREVIEW_OUTPUT_PRICE = 0.00003

GPT3_INPUT_PRICE = 0.0000015
GPT3_OUTPUT_PRICE = 0.000002
GPT3_16_INPUT_PRICE = 0.000003
GPT3_16_OUTPUT_PRICE = 0.000004

# Supported Models
SUPPORTED_MODELS = {
    "gpt-4": {
        "input_price": GPT4_INPUT_PRICE,
        "output_price": GPT4_OUTPUT_PRICE,
        "max_tokens": 8000,
        "temperature": 0.7,
        "max_window_size": 7000
    },
    "gpt-4-1106-preview": {
        "input_price": GPT4_PREVIEW_INPUT_PRICE,
        "output_price": GPT4_PREVIEW_OUTPUT_PRICE,
        "max_tokens": 20000,
        "temperature": 0.7,
        "max_window_size": 18000
    },
    "gpt-4-32": {
        "input_price": GPT4_32_INPUT_PRICE,
        "output_price": GPT4_32_OUTPUT_PRICE,
        "max_tokens": 32000,
        "temperature": 0.7,
        "max_window_size": 30000
    },
    "gpt-3.5-turbo": {
        "input_price": GPT3_INPUT_PRICE,
        "output_price": GPT3_OUTPUT_PRICE,
        "max_tokens": 4000,
        "temperature": 0.7,
        "max_window_size": 3000
    },
    "gpt-3.5-turbo-16k": {
        "input_price": GPT3_16_INPUT_PRICE,
        "output_price": GPT3_16_OUTPUT_PRICE,
        "max_tokens": 16000,
        "temperature": 0.7,
        "max_window_size": 14000
    }
}


class GPTModel:
    """
    GPTModel Class

    This class provides an interface to manage different GPT models.
    """

    def __init__(self, model="gpt-3.5-turbo"):
        """Constructor for GPTModel class."""
        # print(f"Initializing GPTModel with model {model}")
        if model in SUPPORTED_MODELS:
            self._initialize_model_properties(model)
        else:
            raise ValueError(f"Model {model} not supported.")

    def _initialize_model_properties(self, model):
        """Private method to initialize model properties."""
        self.name = model
        self.max_tokens = SUPPORTED_MODELS[model]["max_tokens"]
        self.temperature = SUPPORTED_MODELS[model]["temperature"]
        self.max_window_size = SUPPORTED_MODELS[model]["max_window_size"]
        self.stop = DEFAULT_STOP
        self.system_message = GPT_DEFAULT_SYSTEM_MESSAGE
        self.input_price = SUPPORTED_MODELS[model]["input_price"]
        self.output_price = SUPPORTED_MODELS[model]["output_price"]

    # Getter Methods
    def get_name(self):
        """Returns the model name."""
        return self.name

    def get_max_window_size(self):
        """Returns the maximum window size."""
        return self.max_window_size

    def get_temperature(self):
        """Returns the temperature setting."""
        return self.temperature

    def get_stop(self):
        """Returns the stop setting."""
        return self.stop

    def get_max_tokens(self):
        """Returns the maximum token limit."""
        return self.max_tokens

    def get_system_message(self):
        """Returns the system message."""
        return self.system_message

    # Calculation Methods
    def count_answer_size(self):
        """Calculates the answer size."""
        return self.max_tokens - self.max_window_size

    def count_input_price(self, tokens):
        """Calculates the input price for a given token count."""
        return self.input_price * tokens

    def count_output_price(self, tokens):
        """Calculates the output price for a given token count."""
        return self.output_price * tokens

    # Setter Methods
    def set_model(self, model):
        """Sets the model and updates relevant settings."""
        if model in SUPPORTED_MODELS:
            self._initialize_model_properties(model)
            return True
        return False

    def set_temperature(self, temperature):
        """Sets the temperature."""
        self.temperature = temperature

    def set_max_window_size(self, max_window_size):
        """Sets the maximum window size."""
        self.max_window_size = max_window_size

    def set_stop(self, stop):
        """Sets the stop tokens."""
        self.stop = stop

    def set_max_tokens(self, max_tokens):
        """Sets the maximum token limit."""
        self.max_tokens = max_tokens

    def set_system_message(self, system_message):
        """Sets the system message."""
        self.system_message = system_message
