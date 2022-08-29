# implement a program that prompts the user for the name of a file 
# then outputs that file’s media type if the file’s name ends, case-insensitively, in any of these suffixes:
# .gif,.jpg,.jpeg, .png, .pdf, .txt, .zip
# If the file’s name ends with some other suffix or has no suffix at all, output application/octet-stream instead, which is a common default.

def main():
    fileName = input("File name: ")
    # print mediaType
    print(mediaType(fileName))

def mediaType(fileName):
    # find highest index (whe multiple extends are there) of "."  and extract file extension
    # slicing starts - index at ".": ends at end: exceeds by 1
    extension = fileName[fileName.rfind(".")::1]

    # convert to lower case
    extension = extension.strip().lower()

    # match
    match extension:
        case ".gif":
            return "image/gif"
        case ".jpeg" | ".jpg":
            return "image/jpeg"
        case ".png":
            return "image/png"
        case ".pdf":
            return "application/pdf"
        case ".txt":
            return "text/plain"
        case ".zip":
            return "application/zip"
        case _:
            return "application/octet-stream"

main()
