from transformers import AutoTokenizer, AutoModel

def print_tokens(tokenizer, input_ids_tensor):
    token_texts = [tokenizer.decode([token_id], skip_special_tokens=True) for token_id in input_ids_tensor[0]]
    header = f"{'Token':<10} | {'ID':<8}"
    print(f"{'='*30}\n{'Tokens and their IDs':^30}\n{'='*30}")
    print(header)
    print(f"{'-'*10}-+-{'-'*17}")

    for idx, token_id in enumerate(input_ids_tensor[0]):
        token_text = token_texts[idx]
        print(f"{token_text:<10} | {token_id:<20}")

    print(f"{'='*30}")

model_name = 'nvidia/Llama3-ChatQA-1.5-8B'
tokenizer = AutoTokenizer.from_pretrained(model_name)

print("fThe vocab size is", tokenizer.vocab_size)

inputs = tokenizer(['LGTM'], return_tensors='pt')
input_ids = inputs['input_ids']

print_tokens(tokenizer, input_ids)

