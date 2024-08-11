import os
import random

def delete_files(folder_path, percentage_to_delete=10):
    """
    Randomly deletes a percentage of files from the specified folder.

    Args:
        folder_path (str): The path to the folder from which files will be deleted.
    """
    try:
        # List all files in the folder
        files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
        
        if not files:
            print("No files found in the specified folder.")
            return

        # Calculate the number of files to delete
        num_files_to_delete = max(1, int(len(files) * (percentage_to_delete / 100)))
        
        # Randomly select files to delete
        files_to_delete = random.sample(files, num_files_to_delete)
        
        # Delete the selected files
        for file in files_to_delete:
            file_path = os.path.join(folder_path, file)
            os.remove(file_path)
            print(f"Deleted: {file_path}")

    except Exception as e:
        print(f"An error occurred: {e}")

def test():
    print("taser on")