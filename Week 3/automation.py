import os
import shutil
from pathlib import Path


def organize_folder(target_path):
    # 1. Define category mappings using file extensions
    FILE_CATEGORIES = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"],
        "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx", ".csv"],
        "Music": [".mp3", ".wav", ".aac", ".flac", ".ogg", ".m4a"],
        "Videos": [".mp4", ".mkv", ".avi", ".mov", ".flv", ".wmv"],
        "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    }

    # Convert the string path to a robust Path object
    directory = Path(target_path)

    # Safety check: Ensure the folder actually exists
    if not directory.exists():
        print(f"Error: The directory '{target_path}' does not exist.")
        return

    print(f"Scanning: {directory}...\n")

    # 2. Iterate through all items in the target directory
    for item in directory.iterdir():
        # Skip folders so we don't accidentally move existing directories
        if item.is_dir():
            continue

        # Get the file extension in lowercase (e.g., '.jpg')
        file_extension = item.suffix.lower()

        # Track if the file matched a defined category
        moved = False

        # 3. Match the file extension to a category folder
        for category_name, extensions in FILE_CATEGORIES.items():
            if file_extension in extensions:
                # Create the category folder if it doesn't exist yet
                category_folder = directory / category_name
                category_folder.mkdir(exist_ok=True)

                # Define the new destination path
                destination = category_folder / item.name

                # Move the file safely
                try:
                    shutil.move(str(item), str(destination))
                    print(f"Moved: {item.name} -> [{category_name}]")
                except Exception as e:
                    print(f"Error moving {item.name}: {e}")

                moved = True
                break  # Stop checking other categories for this file

        # 4. Optional: Handle unknown file types (e.g., .exe, .ini)
        if not moved and file_extension != "":
            others_folder = directory / "Others"
            others_folder.mkdir(exist_ok=True)
            try:
                shutil.move(str(item), str(others_folder / item.name))
                print(f"Moved: {item.name} -> [Others]")
            except Exception as e:
                print(f"Error moving {item.name}: {e}")

    print("\nOrganization complete!")


# --- How to Run It ---
if __name__ == "__main__":
    # Replace this with the actual path to your messy folder
    # Windows example: r"C:\Users\YourName\Downloads"
    # Mac/Linux example: "/Users/YourName/Downloads"
    TARGET_DIRECTORY = r"./my_messy_folder"

    organize_folder(TARGET_DIRECTORY)
