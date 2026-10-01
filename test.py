import os

# Check whether index.html exists
assert os.path.exists("index.html"), "index.html does not exist"

# Read HTML file
with open("index.html", "r", encoding="utf-8") as file:
    html = file.read().lower()

# Required elements
required_elements = [
    "<html",
    "<head",
    "<title>",
    "<body",
    "<form",
    "<input",
    "<select",
    "<button",
    "student registration"
]

# Check required elements
for element in required_elements:
    assert element in html, f"Missing required element: {element}"

print("All tests passed successfully!")