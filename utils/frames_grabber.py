import numpy as np
import cv2
from glob import glob
import os 

FLAG_USED_PRELOAD_VIDEO = False


def create_folder(name_folder:str) -> None:
    """
    Create folders with photo
    """
    if not os.path.exists(name_folder):
        os.makedirs(name_folder)


if __name__ == '__main__':
    w = 1270
    h = 720
    fps = 10
    counter = 0
    videos_path  = os.getcwd()+"/video/*.mp4"
    print(videos_path)
    if FLAG_USED_PRELOAD_VIDEO:
        list_good_match_frames = [1080,1260,1340,1590,1800,2270,2370,2400,2670,2750,2990,3200,3380,3500,3610,3750,4110,4270]

    folder_name_camera = "frames_from_camera_"
    for i in range(2):
        create_folder(folder_name_camera + str(i))

    videos_link = glob(videos_path)

    if len(videos_link) != 2:
        print(videos_link)
        print("don't find 2 videos")
        exit()

    cap1 = cv2.VideoCapture(videos_link[0])
    cap2 = cv2.VideoCapture(videos_link[1])

    while True:
        
        ret1, frame1 = cap1.read()
        ret2, frame2 = cap2.read()

        if not ret1 or not ret2:
            break
         
        if not FLAG_USED_PRELOAD_VIDEO:
            if counter % fps == 0:
                cv2.imwrite(folder_name_camera + str(0) + "/frame" + str(counter) + ".jpg", frame1)
                cv2.imwrite(folder_name_camera + str(1) + "/frame" + str(counter) + ".jpg", frame2)
        else:
            if counter in list_good_match_frames:
                cv2.imwrite(folder_name_camera + str(0) + "/frame" + str(counter) + ".jpg", frame1)
                cv2.imwrite(folder_name_camera + str(1) + "/frame" + str(counter) + ".jpg", frame2)


        counter +=1
