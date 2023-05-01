from PIL import Image
import os

downloadsFolder = "D:/Users/carlos.alvarado/Downloads/"
pictureFolder = "D:/Users/carlos.alvarado/Pictures/"
executableFolder = "D:/Users/carlos.alvarado/Documents/Executables/"
csvFolder = "D:/Users/carlos.alvarado/Documents/CSV/"

if __name__ == "__main__":
    for filename in os.listdir(downloadsFolder):
        name, extension = os.path.splitext(downloadsFolder + filename)

        if extension in [".jpg", ".jpeg", ".png"]:
            picture = Image.open(downloadsFolder + filename)
            picture.save(pictureFolder + "compressed_"+filename, optimize=True, quality=60)
            os.remove(downloadsFolder + filename)
            print(name + ": " + extension)

        elif extension in [".exe"]:
            if os.path.exists(executableFolder + filename):
                os.remove(executableFolder + filename)
            os.rename(downloadsFolder + filename, executableFolder + filename)

        elif extension in [".csv"]:
            if os.path.exists(csvFolder + filename):
                os.remove(csvFolder + filename)
            os.rename(downloadsFolder + filename, csvFolder + filename)
