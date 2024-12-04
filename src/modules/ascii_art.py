import random

def generate_ascii_art(text="Nova Terminal"):
    """
    Generates dynamic ASCII art based on the given text.
    """
    styles = ["*", "#", "+", "=", "@", "&"]
    width = len(text) * 2
    result = []

    # Add decorative border
    border = random.choice(styles) * (width + 4)
    result.append(border)

    # Add ASCII art text
    for char in text:
        row = f"{random.choice(styles)} {char} {random.choice(styles)}"
        result.append(row)

    # Add bottom border
    result.append(border)

    return "\n".join(result)


if __name__ == "__main__":
    print(generate_ascii_art("Nova Terminal"))
