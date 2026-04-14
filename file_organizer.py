import os
import shutil

folder_path = input("Enter your folder path")

files = os.listdir(folder_path)

#Creating a folder for Image file type

image_folder = os.path.join(folder_path,'Images')

if not os.path.exists(image_folder):
    os.mkdir(image_folder)

#Creating a folder for Video file type

video_folder = os.path.join(folder_path,'Videos')

if not os.path.exists(video_folder):
    os.mkdir(video_folder)

#Creating a folder for other file type

other_folder = os.path.join(folder_path, 'Others')

if not os.path.exists(other_folder):
    os.mkdir(other_folder)

#Sorting file types

for filename in files:
    full_path = os.path.join(folder_path, filename)

    if os.path.isfile(full_path):

        ext = filename.split('.')[-1].lower()
        print(filename,"-->", ext)

        if ext in ['jpg','png','jpeg']:
            print(filename, "is an imagefile")

            destination = os.path.join(image_folder, filename)
            shutil.move(full_path,destination)

            print('Moved',filename)
                  
        elif ext in ['mp4','mkv']:
            print(filename, 'is a video file')

            destination = os.path.join(video_folder, filename)
            shutil.move(full_path,destination)

            print('Moved',filename)

        else:
            print (filename, 'other')
            destination = os.path.join(other_folder, filename)
            shutil.move(full_path,destination)

            print('Moved',filename)

