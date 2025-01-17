import os

def print_tree(directory):
    for root, dirs, files in os.walk(directory):
        level = root.replace(directory, '').count(os.sep)
        indent = ' ' * 4 * level
        print(f"{indent}|-- {os.path.basename(root)}")
        subindent = ' ' * 4 * (level + 1)
        for file in files:
            print(f"{subindent}|-- {file}")


# Specify the directory you want to display
root_directory = os.getcwd()
print_tree(root_directory)
