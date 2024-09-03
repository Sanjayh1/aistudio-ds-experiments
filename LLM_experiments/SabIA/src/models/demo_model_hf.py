from transformers import AutoTokenizer, LlamaForCausalLM
from framework_classes.completion_model import CompletionModel

class DemoModelHf(CompletionModel):
    def __init__(self, model_name: str = "kaitchup/Llama-2-7b-gptq-2bit", **kwargs) -> None:
        """
        Initializes the model with a specific LLaMA model from Hugging Face.
        Parameters:
            - model_name (str): The model identifier on the Hugging Face Model Hub.
            - **kwargs: Additional parameters for text generation, such as temperature.
        Includes API token for accessing gated models.
        """
        token = "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"  # Use your Hugging Face API token
        
        # Updated to use 'token' instead of 'use_auth_token'
        self.tokenizer = AutoTokenizer.from_pretrained(model_name, token=token)
        self.model = LlamaForCausalLM.from_pretrained(model_name, token=token)
        self.generation_kwargs = kwargs

    def predict(self, message: str) -> str:
        """
        Receives an input from the user and returns the model's response.
        Parameters:
            - message (str): User input (question)
        Return:
            - Response generated by the LLM
        """
        inputs = self.tokenizer(message, return_tensors="pt")
        output_sequences = self.model.generate(
            input_ids=inputs["input_ids"],
            attention_mask=inputs["attention_mask"],
            **self.generation_kwargs
        )
        response = self.tokenizer.decode(output_sequences[0], skip_special_tokens=True)
        return response