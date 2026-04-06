import re
import json

def minify_css(css):
    css = re.sub(r'/\*.*?\*/', '', css, flags=re.DOTALL)
    css = re.sub(r'\s+', ' ', css)
    css = re.sub(r'\s*([\{\};:,])\s*', r'\1', css)
    return css.strip()

def minify_js(js):
    # Very simple minifier
    js = re.sub(r'//.*', '', js)
    js = re.sub(r'\s+', ' ', js)
    return js.strip()

with open('css/style.css', 'r', encoding='utf-8') as f:
    css_content = f.read()

with open('css/style.min.css', 'w', encoding='utf-8') as f:
    f.write(minify_css(css_content))

with open('js/theme.js', 'r', encoding='utf-8') as f:
    js_content = f.read()

with open('js/theme.min.js', 'w', encoding='utf-8') as f:
    f.write(minify_js(js_content))

print("Minification complete.")
