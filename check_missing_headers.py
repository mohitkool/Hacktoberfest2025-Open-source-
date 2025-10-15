import os

def check_missing_headers(base_dir='.'):
    for root, _, files in os.walk(base_dir):
        for f in files:
            if f.endswith('.py'):
                path = os.path.join(root, f)
                with open(path, encoding='utf-8') as file:
                    first_two = [next(file, '').strip() for _ in range(2)]
                    if not any(line.startswith('#!') for line in first_two):
                        print(f"⚠️ {path} missing shebang (#!)")
                    if not any('coding' in line for line in first_two):
                        print(f"⚠️ {path} missing encoding declaration")

if __name__ == "__main__":
    check_missing_headers()
