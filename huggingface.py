from huggingface_hub import HfApi, create_repo

repo_name = "saanvitayal/mental_buddy"
# create_repo(repo_name, token="***********g")

api = HfApi()
api.upload_folder(
    folder_path="./model",
    repo_id=repo_name,
    token="***********"
)