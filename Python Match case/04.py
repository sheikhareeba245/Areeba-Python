# Problem:
# Input a filename like "report.pdf", "photo.jpg", "script.py"
# Extract the extension and use match-case to print:
# .pdf → "PDF Document"
# .jpg or .jpeg → "Image File"
# .py → "Python Script"
# .txt → "Text File" Else → "Unknown file type"
filename=input("Enter your filename with the reccommended extensions /report.pdf,/photo.jpg,/script.py,/.txt: ")
match filename:
    case "report.pdf":
        print("Your report is in  a pdf format: ")
    case "photo.jpg":
        print("Your image in a jpg format: ")
    case "script.py":
        print("Your script in a python language: ")
    case ".txt":
        print("Your file in a text document: ")
    case _:
        print("Invalid extension: ")
        