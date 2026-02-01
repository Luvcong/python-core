"""
chapter05_03
Python Advanced(4) - 나만의 패키지
Keyword - png(jpg) to gif, pil, image
"""
 
"""
- 패키지 작성 : 정적 이미지(JPG, PNG) -> GIF(애니메이션)이미지 변환 패키지
"""

import glob
from PIL import Image

class GifConverter() :
    """
    여러 장의 이미지를 애니메이션 효과가 있는 단일 GIF 이미지로 변경 하는 클래스
    """
    def __init__(self, path_in = None, path_out = None, resize = (320, 240)):
        """
        path_in  : 원본 여러 이미지 경로(Ex : images/*.png)
        path_out : 결과 이미지 경로(Ex : output/filename.png)
        resize   : 리사이징 크기((320,240))
        """
        self.path_in = path_in or './*.png'
        self.path_out = path_out or './output.gif'
        self.resize = resize

    def convert_gif(self) :
        """
        GIF 이미지 변환 기능 수행
        """
        print(self.path_in, self.path_out, self.resize)

        img, *images = [Image.open(f).resize(self.resize, Image.Resampling.LANCZOS) for f in sorted(glob.glob(self.path_in))]

        try :
            img.save(
                fp=self.path_out, 
                format = 'GIF', 
                append_images = images,
                save_all = True, 
                duration = 100, 
                loop = 0,
                # disposal = 2
            )
        except IOError :
            print('Cannot convner!', img)

if __name__ == '__main__' :
    # class test
    c = GifConverter('./project/images/*.png', './project/image_out/result2.gif', (320, 240))
    # 변환
    c.convert_gif()