import os
from dotenv import load_dotenv

if __name__ == "__main__":
    load_dotenv()
    print("I'm the main program")
    print(os.getenv("COOL_API_KEY"))
