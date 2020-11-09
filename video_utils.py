import cv2
import numpy as np
import moviepy.editor

def save_video(filename, frames, frame_rate=24.0):
    """rank 4のNumPy配列をmp4形式の動画に保存します

    Args:
        filename (文字列): 保存するファイル名.mp4形式のみサポート
        frames (NumPy配列): rank 4の uint8 NumPy配列 (F, H, W, C)
        frame_rate (float, オプション): 動画のフレームレート。デフォルトは24.0。
    """
    if not isinstance(frames, np.ndarray):
        raise ValueError("frames にはNumPy配列を入れてください")
    if frames.ndim != 4 or frames.dtype != np.uint8:
        raise ValueError("frames にはnp.uint8型のrank4の配列を入れてください。"+
            "shapeは" + str(frames.shape) + " / " + str(frames.dtype) + "型でした")
    if not isinstance(frame_rate, float) and not isinstance(frame_rate, int):
        raise ValueError("frame_rate は数値で入力してください。 " + str(frame_rate) + " が入力されました")
    
    size = (frames.shape[2], frames.shape[1])

    fmt = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    try:
        writer = cv2.VideoWriter(filename, fmt, frame_rate, size)
        for i in range(frames.shape[0]):
            x = frames[i,:,:,::-1]  # RGB反転する
            writer.write(x)
    finally:
        writer.release()

def display_video(filename, **kwargs):
    """動画をColabで表示します

    Args:
        filename (文字列): 再生する動画のファイル名
    """
    clip = moviepy.editor.VideoFileClip(filename)
    clip.ipython_display(**kwargs)