import gdown
import os

def download_weights_if_needed(weight_path, drive_url):
    if not os.path.exists(weight_path):
        print(f"Downloading weights from {drive_url}...")
        gdown.download(drive_url, weight_path, quiet=False)
    else:
        print("Weights already downloaded.")
