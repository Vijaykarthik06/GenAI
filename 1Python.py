from PIL import Image, ImageDraw, ImageFont

def create_image_with_text(text, output_path):
    # Create an image with white background
    width, height = 800, 400
    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)

    # Specify the font and size
    font = ImageFont.load_default()

    # Calculate text size and position
    text_width, text_height = draw.textsize(text, font=font)
    x = (width - text_width) / 2
    y = (height - text_height) / 2

    # Draw the text on the image
    draw.text((x, y), text, fill="black", font=font)

    # Save the image
    image.save(output_path)
    image.show()  # This will open the image

# Example usage
create_image_with_text("Hello, World!", "text_image.png")
