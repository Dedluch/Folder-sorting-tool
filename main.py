import os
from pathlib import Path
from sys import argv

#All relevant file formats I could find, used for sorting purposes, feel free to add any formats as you wish
ext = {
    "documents": ["pdf", "csv", "ppt", "pptx", "doc", "docx", 
                "rtf", "gdoc", "html", "htm", "md", "odt", 
                "xml", "txt", "xls", "xlsx", "xml", "xlr", 
                "ots", "ods", "gsheet"],

    "archives": ["7z", "ace", "alz", "deb", "gz", "rar", 
                "zip", "iso", "bz2", "Z", "xz", "lzh", 
                "cab", "arj"],

    "executables": ["exe", "bat", "msi", "com", "cmd", "inf", 
                    "ipa", "osx", "pif", "run", "wsh", "sh"],

    "images": ["bmp", "png", "jpg", "jpeg", "jp2", "jps", 
            "pbm", "ico", "gif", "psd", "pdd", "raw", 
            "tif", "tiff", "webp", "cdr", "ai", "cmx", 
            "svg", "x3d", "odg"],

    "sound_files": ["aiff", "aif", "aifc", "aup3", "wav", "wave", 
                    "thd", "psf", "la", "wv", "mp1", "mp2", "mp3", 
                    "wma", "swa", "ogg", "ac3", "midi", "jam", "m4a"],

    "videos": ["aaf", "avi", "mpv", "mp4", "mov", "wmv", 
            "m4v", "mkv"]
}

def main():
    cwd = Path.cwd()
    directories = ["documents", "sound_files", "videos", "images", "archives", "executables", "other", "directories"]
    direcotryLookup = directories.copy()
    
    #Creating directories used for sorting
    for folder in directories:
        if not (cwd / folder).exists():
            os.system(f"mkdir {cwd}\\{folder}")
    #Removing "other" and "directories" so they are not used for file extension lookup
    directories.pop(-1)
    directories.pop(-1)

    #Listing every file in current directory
    for file in os.listdir(cwd):
        filepath = (cwd / file)
        if filepath.is_file():
            extension = file.split(".")[-1]
            #Checking if current file is itself so it doesn't move itself
            if str(filepath) == __file__ or str(filepath) == argv[0]:
                continue
            #Moving file to a directory based on its file extension
            for directory in directories:
                if extension in ext[directory]:
                    filepath.rename((cwd / directory / file))
                    break
            else:
                filepath.rename((cwd / "other" / file))
        #Moving directories to "directories" but skipping the ones created by the program
        elif file not in direcotryLookup:
            filepath.rename((cwd / "directories" / file))


if __name__ == "__main__":
    main()