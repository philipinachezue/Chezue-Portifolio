import os
import re

# Paths
pages_dir = r"c:\Users\Mansa Mussa II\Desktop\Chezue Portifolio\pages"

def optimize_demo_page(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Performance: Add fetchpriority to any potential hero images (if they exist) or logo
    # For these demos, the header/logo is usually the first thing.
    
    # 2. Responsiveness: Fix the .shell layout
    # Current: .shell{display:grid;grid-template-columns:220px 1fr 280px;height:calc(100vh - 60px);}
    # New: We'll add a media query at the end of the first style block.
    
    responsive_css = """
/* Responsive Shell Fix */
@media (max-width: 1100px) {
  .shell { grid-template-columns: 200px 1fr; height: auto; }
  .right, .right-panel { grid-column: span 2; border-left: none; border-top: 1px solid var(--fog); height: auto; }
}
@media (max-width: 768px) {
  .shell { display: flex; flex-direction: column; height: auto; }
  .left, .ls-sidebar { width: 100%; border-right: none; border-bottom: 1px solid var(--fog); height: auto; max-height: 300px; }
  .main { height: auto; overflow: visible; }
  .header { height: auto; padding: 10px 20px; flex-wrap: wrap; }
  .back-to-portfolio { margin-bottom: 8px; }
}
"""
    # Insert before </style>
    content = content.replace('</style>', responsive_css + '</style>', 1)

    # 3. Accessibility: Ensure images have alt text and decoding="async"
    content = re.sub(r'<img\s+([^>]*?)>', r'<img \1 decoding="async">', content)
    # Fix double decoding if already present
    content = content.replace('decoding="async" decoding="async"', 'decoding="async"')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Optimized {os.path.basename(filepath)}")

# Run for all demo pages
for filename in os.listdir(pages_dir):
    if filename.endswith(".html"):
        optimize_demo_page(os.path.join(pages_dir, filename))
