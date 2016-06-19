# -*- coding: utf-8 -*-
import numpy as np
import cv2


# def drawing_figure():
#     # create a black image
#     img = np.zeros((512,512,3), np.uint8)
#
#     # draw a diagonal blue line with thickness of 5 px
#     img = cv2.line(img,(0,0),(511,511),(255,0,0),5)
#
#     # cv2.circle(img, center, radius, color, thickness=1, linetype=8, shift=0)
#
#     cv2.imshow('drawing_figure', img)
#
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
    

def drawing_figure(frame):

    # draw a diagonal blue line with thickness of 5 px
    frame = cv2.rectangle(frame,(0,0),(100,100),(255,0,0),5)

    return frame


def capture_camera(mirror=True, size=None):
    """Capture video from camera"""
    # カメラをキャプチャする
    cap = cv2.VideoCapture(0) # 0はカメラのデバイス番号

    while True:
        # retは画像を取得成功フラグ
        ret, frame = cap.read()

        # 鏡のように映るか否か
        if mirror is True:
            frame = frame[:,::-1]

        # フレームをリサイズ
        # sizeは例えば(800, 600)
        if size is not None and len(size) == 2:
            frame = cv2.resize(frame, size)


        cv2.rectangle(frame, (0, 50), (50, 100), (0, 255, 0), 2)


        # フレームを表示する
        cv2.imshow('camera capture', frame)

        k = cv2.waitKey(1) # 1msec待つ
        if k == 27: # ESCキーで終了
            break

    # キャプチャを解放する
    cap.release()
    cv2.destroyAllWindows()


def main():
    capture_camera()
    # drawing_figure()


if __name__ == '__main__':
    main()
