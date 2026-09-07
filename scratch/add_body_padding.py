for f in ["src/olywork/web/catalog.css", "src/olywork/web/legal.css", "src/olywork/web/usecase.css"]:
    with open(f, "r") as file:
        content = file.read()
    if "padding-top: 80px" not in content:
        content = content.replace("body{", "body{padding-top: 80px; ")
    with open(f, "w") as file:
        file.write(content)
