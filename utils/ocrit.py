import easyocr
from PIL import Image


def run_ocr():
    images = ['img1.jpg', 'img2.jpg', 'img3.jpg']

    for img in images:
        image_path = f'static/{img}'
        extracted_text = ocr_from_image(image_path)
        print(f"extracted text: {extracted_text}")


def ocr_from_image(img_path):
    # easyocr reader instance with support for multiple langs
    reader = easyocr.Reader(['en'])  # ['en', 'hi', 'es'])

    # read the image using Pillow
    image = Image.open(img_path)

    # perform OCR on the image
    results = reader.readtext(image)

    # extract and concatenate the recognized text
    ext_text = ' '.join([result[1] for result in results])

    return ext_text


if __name__ == '__main__':
    run_ocr()
