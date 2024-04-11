import os

header = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>File Index</title>
</head>
<body>
    <h1>File Index</h1>
    <ul>
"""

footer = """
    </ul>
</body>
</html>
"""


def sort_files_by_ext_and_name(files):
    return sorted(files, key=lambda x: (os.path.splitext(x)[1], os.path.splitext(x)[0]))


def generate_file_links(directory):
    links = []

    for foldername, subfolders, filenames in os.walk(directory):
        # Exclude folders and files starting with `.`
        subfolders[:] = [d for d in subfolders if not d.startswith('.')]
        filenames = [f for f in filenames if not f.startswith('.')]

        # Sort files by extension and then by name
        sorted_files = sort_files_by_ext_and_name(filenames)

        for filename in sorted_files:
            # Create a relative path to the file
            relative_path = os.path.relpath(
                os.path.join(foldername, filename), directory)

            # Convert OS path to web path
            web_path = relative_path.replace(os.sep, '/')

            links.append(f'<li><a href="{web_path}">{web_path}</a></li>')

    return links


def generate_html_index(path, destructive):
    print(f"Generating HTML files... {path}")
    links = generate_file_links(path)

    output_file = os.path.join(path, "index.html")
    if destructive:
        with open(output_file, "w") as index_file:
            index_file.write(header)
            index_file.write("\n".join(links))
            index_file.write(footer)

    print(f"Done generating HTML: {output_file}")


if __name__ == "__main__":
    generate_html_index(".", destructive=True)
