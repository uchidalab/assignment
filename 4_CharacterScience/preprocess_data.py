"""
データセットのフォントとタグの情報をcsvにまとめる
データセットのフォント画像を入力用に前処理する
"""

from pathlib import Path
import pandas as pd
from PIL import Image, ImageOps
from keras.preprocessing import image as Kimage
from tqdm import tqdm

# alphabetのリスト
alphLower = [chr(i) for i in range(97, 97 + 26)]
alphUpper = [chr(i) * 2 for i in range(65, 65 + 26)]


def collect_fontName_tagWord(fontTag_path):

    fontTag_filenames = sorted(map(str, fontTag_path.glob("*")))
    font_tag_list = []

    for filename in tqdm(fontTag_filenames):
        fontName = Path(filename).name
        tags = sorted(list(map(str, pd.read_csv(filename, sep=" ", header=None).dropna(axis=1).values[0])))
        for tag in tags:
            font_tag_list.append([fontName, tag])

    df = pd.DataFrame(data=font_tag_list, columns=["fontName", "tagWord"])
    df.to_csv("fontName_tagWord.csv", index=False)


def preprocess_fontimage(fontImage_path, resultImage_path):

    def cropImage(pil_img):
        croprange = pil_img.getbbox()
        crop_img = pil_img.crop(croprange)
        return crop_img

    def expand2square(pil_img, background_color):
        width, height = pil_img.size
        if width == height:
            return pil_img
        elif width > height:
            result = Image.new(pil_img.mode, (width, width), background_color)
            result.paste(pil_img, (0, (width - height) // 2))
            return result
        else:
            result = Image.new(pil_img.mode, (height, height), background_color)
            result.paste(pil_img, ((height - width) // 2, 0))
            return result

    def add_margin(pil_img, top, right, bottom, left, color):
        width, height = pil_img.size
        new_width = width + right + left
        new_height = height + top + bottom
        result = Image.new(pil_img.mode, (new_width, new_height), color)
        result.paste(pil_img, (left, top))
        return result

    if not resultImage_path.exists():
        resultImage_path.mkdir(parents=True)

    df = pd.read_csv("fontName_tagWord.csv")
    fontTag_fontnames = sorted(list(set(df["fontName"].values)))

    for fontName in tqdm(fontTag_fontnames):
        for alph in alphUpper+alphLower:
            img_path = fontImage_path/"{}_{}.png".format(fontName, alph)
            img = Kimage.load_img(str(img_path))
            img = ImageOps.invert(img)
            img = cropImage(img)
            img = expand2square(img, (0, 0, 0)).resize((144, 144))
            img = add_margin(img, 40, 40, 40, 40, (0, 0, 0))
            img.save(str(resultImage_path/"{}_{}.png".format(fontName, alph)))


if __name__=="__main__":

    # フォント名とタグをfontName_tagWord.csvにまとめる
    collect_fontName_tagWord(fontTag_path=Path("dataset").resolve() / "taglabel")

    # 入力用画像を作成
    preprocess_fontimage(fontImage_path=Path("dataset").resolve() / "fontimage",
                         resultImage_path=Path("dataset").resolve() / "fontimage_preprecessed")
