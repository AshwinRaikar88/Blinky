import cv2


def capture_delay(output_img='result.jpg', secs=156):
    """
    To capture images from webcam and store them in the output directory after a specific time interval

    :param secs: Time in seconds after which the image will be captured (here 1 sec = 31 value, so for 5 secs = 156 )
    :param output_img: The file name of the output image (by default the image will be saved as 'result.jpg')
    :return: returns the img_new required to read and display images in cv2 and the location of the output directory
    """
    cv2.destroyAllWindows()
    out = './output/' + output_img
    webcam = cv2.VideoCapture(0)
    counter = 0
    while True:
        check, frame = webcam.read()
        cv2.imshow("Capturing", frame)
        key = cv2.waitKey(1)

        if counter == secs:
            cv2.imwrite(filename=out, img=frame)
            webcam.release()
            cv2.destroyAllWindows()
            img_new = cv2.imread(out, cv2.IMREAD_ANYCOLOR)
            cv2.imshow("Image saved!", img_new)
            cv2.waitKey(1550)
            cv2.destroyAllWindows()
            print("Image saved!")
            break

        else:
            counter += 1
            continue
