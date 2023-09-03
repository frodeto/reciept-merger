import os
import sys
from pdf2image import convert_from_path
from PIL import Image

def pdfs_to_collage(input_folder: str, output_image_name: str):

    # Check if the folder exists
    if not os.path.exists(input_folder):
        print(f"The folder {input_folder} does not exist!")
        return
    
    # Get list of PDFs
    pdf_files = [f for f in os.listdir(input_folder) if f.lower().endswith('.pdf')]
    if not pdf_files:
        print("No PDFs found in the specified folder.")
        return

    images = []

    # Convert each PDF to image
    for pdf_file in pdf_files:
        pdf_path = os.path.join(input_folder, pdf_file)
        images_from_pdf = convert_from_path(pdf_path)

        # We're only dealing with single-page PDFs so just get the first image
        if images_from_pdf:
            images.append(images_from_pdf[0])

    # Calculate number of rows for the collage
    imgs_per_row = 4
    total_images = len(images)
    rows = (total_images // imgs_per_row) + int(total_images % imgs_per_row != 0)

    # Calculate collage size
    width = max(img.width for img in images) * imgs_per_row
    height = max(img.height for img in images) * rows

    # Create an empty image with the calculated width and height
    collage = Image.new(mode='RGB', size=(width, height), color=(255, 255, 255))
    
    x_offset, y_offset = 0, 0

    # Paste each image into the collage in a grid format
    for idx, img in enumerate(images):
        collage.paste(img, (x_offset, y_offset))
        x_offset += img.width
        
        if (idx + 1) % imgs_per_row == 0:  # Check if end of row
            x_offset = 0  # Reset x_offset
            y_offset += img.height  # Move to next row

    # Save the collage
    collage.save(output_image_name)
    print(f"Collage saved as {output_image_name}")


if __name__ == "__main__":
    pdfs_to_collage(sys.argv[1], sys.argv[2])
