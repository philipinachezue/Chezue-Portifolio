import os

pages_dir = r"c:\Users\Mansa Mussa II\Desktop\Chezue Portifolio\pages"

def fix_back_links(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Change ../index.html to ../index.html#work for demos to return to the Work section
    # and for specialized pages, point to their respective sections if appropriate.
    
    if "va-proof-case-studies.html" in filepath or "testimonials.html" in filepath:
        # Case studies and testimonials might want to go to the results or testimonials section
        content = content.replace('href="../index.html"', 'href="../index.html#results"')
    else:
        # Standard demos go to #work
        content = content.replace('href="../index.html"', 'href="../index.html#work"')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated back links for {os.path.basename(filepath)}")

for filename in os.listdir(pages_dir):
    if filename.endswith(".html"):
        fix_back_links(os.path.join(pages_dir, filename))
