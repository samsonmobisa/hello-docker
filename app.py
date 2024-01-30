# app.py
# print("Hello, Docker!")
# print("Hello, Welocome to Docker!")


# app.py
import sys

if len(sys.argv) > 1:
    name = sys.argv[1]
    print(f"Hello, {name}! Welcome to Docker!")
else:
    print("Hello Sam")
