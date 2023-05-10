

def import_text(path):
    with open(path, encoding="utf8") as f:
        return f.read()


home_page_text = import_text('text_docs\home_page_text.txt')
intro_page_text = import_text('text_docs\intro_page_text.txt')
bubble_page_text = import_text(r'text_docs\bubble_page_text.txt')
quick_page_text = import_text(r'text_docs\quick_page_text.txt')
bigo_page_text = import_text(r'text_docs\bigo_page_text.txt')
