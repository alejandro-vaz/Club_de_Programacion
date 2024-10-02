def fmdtomd(filename):
    def replace_size(data):
        data = data.replace("/h1", "#") # Título
        data = data.replace("/h2", "##") # Sección
        return data 
    def replace_point(data):
        data = data.replace("    / ", "1. ") # Punto numerado
        data = data.replace("    . ", "   - ") # Punto sin numerar
        return data
    def replace_definition(data):
        data = data.replace("/def", ">") # Definición
        return data
    def replace_checkbox(data):
        data = data.replace("/void", "- [ ]") # Caja de verificación vacía
        data = data.replace("/done", "- [X]") # Caja de verificación con check
        return data
    def replace_code(data):
        data = data.replace("/math", "```math") # Inicio de matemáticas
        data = data.replace("/python", "```python") # Inicio de código Python
        data = data.replace("/exit", "```") # Fin de código
        data = data.replace("/ipy", "`") # Código en línea
        return data
    def add_images(data):
        count = 1
        while "/img" in data:
            data = data.replace("/img", f"![Relative](/images/{count}.png)", 1) # Añadir imagen
            count += 1
        return data
    def replace_style(data):
        data = data.replace("./", ".\n\n") # New paragraph
        data = data.replace("//", "*") # Italic
        data = data.replace("/-", "~~") # Strikethrough
        data = data.replace("/s", "~") # Subscript
        data = data.replace("/S", "^") # Superscript
        data = data.replace("'", "**") # Bold
        return data
    
    with open(filename, 'r', encoding="utf-8") as file:
        content = file.read()
        content = replace_size(content)
        content = replace_point(content)
        content = replace_definition(content)
        content = replace_checkbox(content)
        content = replace_code(content)
        content = add_images(content)
        content = replace_style(content)
    return content

if __name__ == "__main__":
    try:
        fname = f"{input("Enter the file name: ")}.fmd"
    except Exception as e:
        print("Error during conversion:\n", e)
    output = fmdtomd(fname)
    with open(fname.replace("fmd", "md"), 'w', encoding="utf-8") as file:
        file.write(output)