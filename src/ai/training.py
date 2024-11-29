import torch
import torch.nn as nn
from transformers import GPT2LMHeadModel, GPT2Tokenizer

class PoemGenerator(nn.Module):
    def __init__(self, model_name='gpt2'):
        super(PoemGenerator, self).__init__()
        self.tokenizer = GPT2Tokenizer.from_pretrained(model_name)
        self.model = GPT2LMHeadModel.from_pretrained(model_name)

    def generate_poem(self, prompt, max_length=100):
        input_ids = self.tokenizer.encode(prompt, return_tensors='pt')
        attention_mask = torch.ones(input_ids.shape, dtype=torch.long)
        
        output = self.model.generate(
            input_ids,
            attention_mask=attention_mask,
            max_length=max_length,
            num_return_sequences=1,
            no_repeat_ngram_size=2,
            do_sample=True,
            top_k=50,
            top_p=0.95,
            temperature=0.7
        )

        generated_poem = self.tokenizer.decode(output[0], skip_special_tokens=True)
        return generated_poem

# Usage example
if __name__ == "__main__":
    generator = PoemGenerator()
    prompt = "In the garden of dreams"
    poem = generator.generate_poem(prompt)
    print(poem)
