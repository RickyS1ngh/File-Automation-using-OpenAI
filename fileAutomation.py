import os
import shutil

def fileAutomation():
    downloadsPath = "/Users/rickysingh/Downloads"
    targetPath = "/Users/rickysingh/Documents"
    EXTS = {
        "py": "Python Code",
        "c": "C Code",
        "cpp": "C++ Code",
        "java": "Java Code",
        "html": "Html Code",
        "jpg": "Images",
        "jpeg": "Images",
        "pdf": "Document",
        "docs": "Document",
        "docx": "Document"}

    with os.scandir(downloadsPath) as files:
        for file in files:
            for ext, path in EXTS.items():
                if file.name.endswith(ext):
                    targetFolder = os.path.join(targetPath, path)
                    if (not os.path.exists(targetFolder)):
                        os.makedirs(targetFolder)
                    shutil.move(file, targetFolder)
