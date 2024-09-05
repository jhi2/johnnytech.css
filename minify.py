import os
from csscompressor import compress
from jsmin import jsmin

def minify_css_files(directory, output_file,rescue_imports):
    combined_css = ""
    page = []
    for filename in os.listdir(directory):
        if filename.endswith('.css'):
            with open(os.path.join(directory, filename), 'r') as infile:
                print(f"Minifying {filename}")
                for line in infile.read().splitlines():
                    if line.startswith("@import"):
                        if line in rescue_imports:
                            page.append(line)
                        else:
                            print("Import detected:skipping line")
                    else:
                        page.append(line)
            

                combined_css += "\n".join(page)
    minified_css = compress(combined_css)
    with open(output_file, 'w') as outfile:
        outfile.write(minified_css)
def minify_js_files(directory, output_file):
    combined_js = ""
    page = []
    for filename in os.listdir(directory):
        if filename.endswith('.js'):
            with open(os.path.join(directory, filename), 'r') as infile:
                print(f"Minifying {filename}")
                for line in infile.read().splitlines():
                    page.append(line)
            combined_js += "\n".join(page)
    minified_js = jsmin(combined_js)
    with open(output_file, 'w') as outfile:
        outfile.write(minified_js)
            
if __name__ == "__main__":
    directory = r'C:\Users\johnd\OneDrive\Documents\johnnytech.css\framework'  # Replace with your directory
    output_file_css = 'dist.css'  # Name of the output file
    output_file_js = 'dist.js'  # Name of the output file
    resc_imports = ["@import url('https://fonts.googleapis.com/css2?family=SUSE:wght@100..800&display=swap');"]
    minify_css_files(directory, output_file_css,resc_imports)
    print(f"All CSS files in {directory} have been minified and combined into {output_file_css}")
    minify_js_files(directory, output_file_js)
    print(f"All JS files in {directory} have been minified and combined into {output_file_js}")
