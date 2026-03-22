from huggingface_hub import HfApi

api = HfApi()
# Add your HuggingFace token here
user = api.whoami(token="your_huggingface_token_here")
print(user)