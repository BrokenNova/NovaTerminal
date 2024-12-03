import argparse
from ai_core import NovaAI

def main():
    parser = argparse.ArgumentParser(description="Nova Terminal CLI")
    parser.add_argument("--message", type=str, help="Message to send to Nova Terminal")
    args = parser.parse_args()

    ai = NovaAI()
    response = ai.respond(args.message if args.message else "default input")
    print(response)

if __name__ == "__main__":
    main()
