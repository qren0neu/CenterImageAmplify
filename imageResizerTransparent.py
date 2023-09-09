import sys
import os
from PIL import Image
from datetime import datetime


def resize_and_fill_center(image_path, new_width, new_height, background_color=(255, 255, 255, 0)):
    original_image = Image.open(image_path)
    original_width, original_height = original_image.size

    # Create a new blank canvas
    canvas = Image.new('RGBA', (new_width, new_height), background_color)

    # Calculate the position to paste the image
    x_offset = (new_width - original_width) // 2
    y_offset = (new_height - original_height) // 2

    # Paste the original image onto the canvas
    canvas.paste(original_image, (x_offset, y_offset))

    return canvas


def main():
    if len(sys.argv) != 4:
        print("Usage: python script.py input_image_path output_width output_height")
        return

    input_image_path = sys.argv[1]
    output_width = int(sys.argv[2])
    output_height = int(sys.argv[3])

    output_folder = os.path.dirname(input_image_path)  # Output to the same folder as the input image

    output_image = resize_and_fill_center(input_image_path, output_width, output_height)

    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    output_image_name = f"output_{timestamp}.png"
    output_image_path = os.path.join(output_folder, output_image_name)

    output_image.save(output_image_path)
    print(f"Processed image saved at: {output_image_path}")


if __name__ == "__main__":
    main()
