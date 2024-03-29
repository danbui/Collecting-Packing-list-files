import os
import shutil
import tkinter as tk
from tkinter import filedialog

def select_source_folder():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    source_folder = filedialog.askdirectory(title="Select Source Folder")
    return source_folder

def copy_pdf_files(source_folder, destination_folder):
    # Create the destination folder if it doesn't exist
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Walk through the source folder's first-level subfolders
    for subfolder in os.listdir(source_folder):
        subfolder_path = os.path.join(source_folder, subfolder)
        if os.path.isdir(subfolder_path):
            if "THAILAND" in subfolder.upper():
                # Create a corresponding subfolder in the destination folder
                thailand_folder = os.path.join(destination_folder, subfolder)
                if not os.path.exists(thailand_folder):
                    os.makedirs(thailand_folder)
                # Extract the first three characters of the subfolder's name
                prefix = subfolder[:3]
                # Copy PDF files starting with "PL" or "PKL" to the Thailand subfolder
                for filename in os.listdir(subfolder_path):
                    if filename.lower().startswith(("pl", "pkl", "packing list")) and filename.lower().endswith(".pdf"):
                        source_path = os.path.join(subfolder_path, filename)
                        # Construct the new filename template
                        new_filename = f"{os.path.basename(source_folder)}-{prefix}_{filename}"
                        destination_path = os.path.join(thailand_folder, new_filename)
                        shutil.copyfile(source_path, destination_path)
                        print(f"Copied {filename} to {thailand_folder} as {new_filename}")
            else:
                # For other first-class subfolders, copy PDF files as before
                for foldername, _, filenames in os.walk(subfolder_path):
                    for filename in filenames:
                        if filename.lower().startswith(("pl", "pkl", "packing list")) and filename.lower().endswith(".pdf"):
                            source_path = os.path.join(foldername, filename)
                            # Construct the new filename template
                            new_filename = f"{os.path.basename(source_folder)}-{subfolder[:3]}_{filename}"
                            destination_path = os.path.join(destination_folder, new_filename)
                            shutil.copyfile(source_path, destination_path)
                            print(f"Copied {filename} to {destination_folder} as {new_filename}")
        else:
            # Copy PDF files directly under the source folder
            if filename.lower().startswith(("pl", "pkl", "packing list")) and filename.lower().endswith(".pdf"):
                source_path = os.path.join(source_folder, filename)
                # Construct the new filename template
                new_filename = f"{os.path.basename(source_folder)}_{filename}"
                destination_path = os.path.join(destination_folder, new_filename)
                shutil.copyfile(source_path, destination_path)
                print(f"Copied {filename} to {destination_folder} as {new_filename}")


def main():
    source_folder = select_source_folder()
    if source_folder:
        # Get the desktop path for the current user
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
        # Set the destination folder path to be a "Result" folder on the desktop
        destination_folder = os.path.join(desktop_path, "Result")

        # Proceed with copying the PDF files
        copy_pdf_files(source_folder, destination_folder)
        print("Task completed.")

if __name__ == "__main__":
    main()

