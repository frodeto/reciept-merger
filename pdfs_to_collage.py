import os
import sys
from pdf2image import convert_from_path
from PIL import Image

def pdfs_to_collage(input_folder: str, output_image_name: str):

    # Check if the folder exists
    if not os.path.exists(input_folder):
        print(f"The folder {input_folder} does not exist!")
        return
    
    # Get list of PDFs, JPGs, and PNGs
    file_extensions = ('.pdf', '.jpg', '.jpeg', '.png')
    files = [f for f in os.listdir(input_folder) if f.lower().endswith(file_extensions)]
    if not files:
        print("No PDFs, JPGs, or PNGs found in the specified folder.")
        return

    images = []

    # Convert each file to image
    for file in files:
        file_path = os.path.join(input_folder, file)
        if file.lower().endswith('.pdf'):
            images_from_pdf = convert_from_path(file_path)
            # Handle up to two pages
            if images_from_pdf:
                images.append(images_from_pdf[0])
            if len(images_from_pdf) > 1:
                images.append(images_from_pdf[1])
        else:
            img = Image.open(file_path)
            images.append(img)

    # Calculate number of rows for the collage
    imgs_per_row = 4
    total_images = len(images)
    rows = (total_images // imgs_per_row) + int(total_images % imgs_per_row != 0)

    # Calculate collage size
    width = max(img.width for img in images) * imgs_per_row
    height = max(img.height for img in images) * rows

    # Create an empty image with the calculated width and height
    collage = Image.new(mode='RGB', size=(width, height), color=(255, 255, 255))
    
    x_offset, y_offset, max_height_in_row = 0, 0, 0

    # Paste each image into the collage in a grid format
    for idx, img in enumerate(images):
        collage.paste(img, (x_offset, y_offset))
        x_offset += img.width
        max_height_in_row = max(max_height_in_row, img.height)
        
        if (idx + 1) % imgs_per_row == 0:  # Check if end of row
            x_offset = 0  # Reset x_offset
            y_offset += max_height_in_row  # Move to next row

    # Save the collage
    collage.save(output_image_name)
    print(f"Collage saved as {output_image_name}")


if __name__ == "__main__":
    pdfs_to_collage(sys.argv[1], sys.argv[2])
