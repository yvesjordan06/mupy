import os
def write_to_file(file_path, mode, content, comment=None, isComment=False):
    # Create the destination folder if it doesn't exist
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    with open(file_path, mode) as file:
        if comment:
            file.write(f"# {comment}\n")
        if isComment:
            file.write(f'"""{content}"""\n')
        else:
            file.write(content)
        file.write("\n\n")
