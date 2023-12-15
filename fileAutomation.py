import os
from openAIFileNamer import newFileName
from fileContentExtracter import contentExtracter
import shutil


def fileAutomation():
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
        "pdf": "Document",
        "docs": "Document",
        "docx": "Document"}

    for directory in directories:
        with os.scandir(directory) as files:
            for file in files:
                for ext, path in EXTS.items():
                    if file.name.endswith(ext):
                        if ext not in ("jpeg", "jpg"):
                            fileContents = contentExtracter(file,ext)
                            newName = newFileName(file.name, fileContents)
                            oldPath = file.path
                            newPath = os.path.join(directory, newName)
                            os.rename(oldPath, newPath)
                        targetFolder = os.path.join(targetPath, path)
                        if (not os.path.exists(targetFolder)):
                            os.makedirs(targetFolder)
                        shutil.move(newPath, targetFolder)


