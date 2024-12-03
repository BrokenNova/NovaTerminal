from PIL import Image, ImageDraw, ImageFont

def generate_banner(output_path, text="Nova Terminal"):
    width, height = 800, 200
    image = Image.new("RGB", (width, height), "black")
    draw = ImageDraw.Draw(image)
    
    font = ImageFont.truetype("arial.ttf", size=36)
    text_width, text_height = draw.textsize(text, font=font)
    text_position = ((width - text_width) // 2, (height - text_height) // 2)

    draw.text(text_position, text, fill="white", font=font)
    image.save(output_path)

if __name__ == "__main__":
    generate_banner("nova_banner_generated.png", "Welcome to Nova Terminal")
