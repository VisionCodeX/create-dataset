# input videos folder path
# output: save the videos' frames in the folder dataset

import cv2
import numpy as np
import matplotlib.pyplot as plt
import pathlib
import argparse

def video2frames(video_path:pathlib.Path, dataset_path:str, each_frames_save:int=30) -> None:
    '''
    input: video_path, dataset_path, each_seconds
    output: save the frames of the video in the dataset_path
    '''

    for path in video_path:
        # read the video with while loop
        cap = cv2.VideoCapture(str(path))
        # get the total frames of the video
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        # get the fps of the video
        fps = cap.get(cv2.CAP_PROP_FPS)
        # get the total seconds of the video
        total_seconds = total_frames / fps

        while(cap.isOpened()):
            # get the frame index
            frame_index = int(cap.get(cv2.CAP_PROP_POS_FRAMES))
            # get the current seconds
            current_seconds = frame_index / fps
            # read the frame
            ret, frame = cap.read()
            if ret == True:
                # save the frame
                print(f"video_path: {str(path)} frame_index: {frame_index}, current_seconds: {current_seconds:.2f}, total_frames: {total_frames}, total_seconds: {total_seconds:.2f}")
                if frame_index % each_frames_save == 0:
                    cv2.imwrite(dataset_path + '/' + str(path.stem) + '_' + str(frame_index) + '.jpg', frame)
            else:
                break

        cap.release()
        cv2.destroyAllWindows()

def main():
    # argparse
    parser = argparse.ArgumentParser(description='video2frames')
    parser.add_argument('--videos_path', type=str, default="videos", help='input videos folder path')
    parser.add_argument('--dataset_path', type=str, default='dataset', help='output dataset folder path')
    parser.add_argument('--each_frames_save', type=int, default=30, help='save each frames')
    args = parser.parse_args()

    # get the videos path
    video_path = list(pathlib.Path(args.videos_path).glob('*.mp4'))
    print(video_path)
    # get the dataset path
    dataset_path = args.dataset_path
    # get the each frames save
    each_frames_save = args.each_frames_save

    # video2frames
    video2frames(video_path, dataset_path, each_frames_save)


if __name__ == '__main__':
    main()

