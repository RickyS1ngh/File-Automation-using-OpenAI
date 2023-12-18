import os
from openAIFileNamer import newFileName
from fileContentExtracter import contentExtracter
import shutil


def fileMove(file, targetPath, path):
    targetFolderPath = os.path.join(targetPath, path)
    if isinstance(file, os.DirEntry):
        fileName = file.name
    else:
        fileName = file.split("/")[-1]
    if (not os.path.exists(targetFolder)):  # Check if the target folder exists
        os.makedirs(targetFolder)  # Creates the directory
    targetFilePath= os.path.join(targetFolder, fileName)
    if (not os.path.exists(targetFilePath) #Checks if the path exists with the file, if it doesnt, the file is moved
        ):  # Checks if a file with the name exists in the directory
        shutil.move(file, targetFolder)  # moves file
    else:
        if os.stat(file).st_size == os.stat(targetFilePath).st_size: #Checks if the file in the target folder is the the same file. Removes the file if it is the same file
            print(f"{fileName} already exists. It will be deleted")
            os.remove(file)
        else:
            print(
                f"{fileName} cannot be moved because a file with the same name already exist")#Cannot move the file because another file with the same name exists


def fileAutomation():
    userInput = input("Would you like openAI to assist in naming your files? Yes/No or Y/N: ").lower()
    while userInput not in ("yes", "y", "no", "n"):
        userInput = input("Input was invalid. Please enter Yes/No or Y/N").lower()

    directories = ["/Users/rickysingh/Downloads", "/Users/rickysingh/Desktop"]
    targetPath = "/Users/rickysingh/Documents"
    EXTS = {
        "py": "Code/Python Code",
        "c": "Code/C Code",
        "cpp": "Code/C++ Code",
        "java": "Code/Java Code",
        "html": "Code/Html Code",
        "txt": "Text Files",
        "jpg": "Images",
        "jpeg": "Images",
        "mov": "Videos",
        "mp4": "Videos",
        "mp3": "Audio",
        "pptx": "PowerPoints",
        "pdf": "Document",
        "docs": "Document",
        "docx": "Document"}

    for directory in directories:
        with os.scandir(directory) as files:
            for file in files:
                if file.is_file():
                    extension = file.name.split(".")[-1].lower()
                    for ext, path in EXTS.items():
                        if extension == ext:
                            if ext not in (
                                    "jpeg", "jpg", "mov", "mp4", "pptx") and userInput in ("yes", "y"):
                                try:
                                    fileContents = contentExtracter(file, ext)
                                    newName = newFileName(
                                        file.name, fileContents)
                                    oldPath = file.path
                                    newPath = os.path.join(directory, newName)
                                    os.rename(oldPath, newPath)
                                    file = newPath
                                except Exception as error:
                                    print(error)
                                    print(
                                        "File will still be moved to the target destination")
                                    fileMove(file, targetPath, path)
                            fileMove(file, targetPath, path)
