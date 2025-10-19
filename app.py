def greet(name="Developer"):
    message = f"Hello {name}, welcome to the GitHub CI Pipeline!"
    print(message)
    return message


if __name__ == "__main__":
    greet("waleed")
