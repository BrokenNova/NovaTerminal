class NovaAI:
    def __init__(self, name="Nova Terminal"):
        self.name = name

    def respond(self, message):
        return f"{self.name} says: 'I'm here to assist with {message}'"

# Example usage:
if __name__ == "__main__":
    ai = NovaAI()
    print(ai.respond("your inquiries"))
