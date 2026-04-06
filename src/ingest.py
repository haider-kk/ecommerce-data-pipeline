import os

def download_data():
    print("Starting data download from Kaggle...")

    # Step 1: Ensure raw data folder exists
    os.makedirs("data/raw", exist_ok=True)

    # Step 2: Kaggle download command
    command = "kaggle datasets download -d olistbr/brazilian-ecommerce -p data/raw --unzip"

    # Step 3: Execute command
    exit_code = os.system(command)

    # Step 4: Check result
    if exit_code == 0:
        print(" Dataset downloaded and extracted successfully!")
    else:
        print(" Error occurred while downloading dataset")

if __name__ == "__main__":
    download_data()
