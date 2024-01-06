import spacy

def download_model(model_name):
    spacy.cli.download(model_name)

if __name__ == "__main__":
    model_name = "en_core_web_lg"  # or any other model you need
    download_model(model_name)
