from video_prediction import StartApplication

if __name__ == "__main__":
    input_vid_path = "test-input/CCTV_ Truck slams into residential building in NW China, 5 dead.mp4"
    output_vid_path = "output_video-1.mp4"
    
    StartApplication(input_vid_path, output_vid_path)