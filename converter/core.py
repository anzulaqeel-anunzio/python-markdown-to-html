# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel

import re

class MarkdownConverter:
    def convert(self, md_text):
        html = md_text
        
        # Headers
        html = re.sub(r'###### (.*)', r'<h6>\1</h6>', html)
        html = re.sub(r'##### (.*)', r'<h5>\1</h5>', html)
        html = re.sub(r'#### (.*)', r'<h4>\1</h4>', html)
        html = re.sub(r'### (.*)', r'<h3>\1</h3>', html)
        html = re.sub(r'## (.*)', r'<h2>\1</h2>', html)
        html = re.sub(r'# (.*)', r'<h1>\1</h1>', html)
        
        # Bold
        html = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', html)
        html = re.sub(r'__(.*?)__', r'<strong>\1</strong>', html)
        
        # Italic
        html = re.sub(r'\*(.*?)\*', r'<em>\1</em>', html)
        html = re.sub(r'_(.*?)_', r'<em>\1</em>', html)
        
        # Code
        html = re.sub(r'`(.*?)`', r'<code>\1</code>', html)
        
        # Links
        html = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', html)
        
        # Lists (Unordered) - Simple implementation
        # Note: robust list parsing is hard with regex alone, doing line-by-line processing often better
        # But for "basic" converter, let's just do simple replacements.
        
        lines = html.split('\n')
        new_lines = []
        in_list = False
        
        for line in lines:
            stripped = line.strip()
            if stripped.startswith('- ') or stripped.startswith('* '):
                if not in_list:
                    new_lines.append('<ul>')
                    in_list = True
                content = stripped[2:]
                new_lines.append(f'  <li>{content}</li>')
            else:
                if in_list:
                    new_lines.append('</ul>')
                    in_list = False
                
                # Paragraphs: if line is not empty and not a tag (roughly)
                if stripped and not stripped.startswith('<'):
                    new_lines.append(f'<p>{line}</p>')
                else:
                    new_lines.append(line)
        
        if in_list:
            new_lines.append('</ul>')
            
        html = '\n'.join(new_lines)
        
        return html

    def convert_file(self, input_path, output_path):
        with open(input_path, 'r', encoding='utf-8') as f:
            md_content = f.read()
            
        html_content = self.convert(md_content)
        
        full_html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Markdown Export</title>
    <style>
        body {{ font-family: sans-serif; line-height: 1.6; max-width: 800px; margin: 0 auto; padding: 20px; }}
        code {{ background: #f4f4f4; padding: 2px 5px; border-radius: 3px; }}
        pre {{ background: #f4f4f4; padding: 15px; overflow-x: auto; }}
        img {{ max-width: 100%; }}
    </style>
</head>
<body>
{html_content}
</body>
</html>"""
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(full_html)

# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel
