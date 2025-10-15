import ast
import os

def check_missing_docstrings(base_dir='.'):
    for root, _, files in os.walk(base_dir):
        for f in files:
            if f.endswith('.py'):
                path = os.path.join(root, f)
                with open(path, encoding='utf-8') as file:
                    try:
                        tree = ast.parse(file.read(), filename=path)
                    except SyntaxError:
                        continue
                for node in ast.walk(tree):
                    if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                        if not ast.get_docstring(node):
                            print(f"⚠️ Missing docstring: {node.name} in {path}")

if __name__ == "__main__":
    check_missing_docstrings()
