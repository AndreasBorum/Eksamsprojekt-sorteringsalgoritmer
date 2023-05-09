


def import_text(path):
    with open(path) as f:
        return f.read()




home_page_text = import_text('text_docs\home_page_text.txt')
intro_page_text = import_text('text_docs\intro_page_text.txt')


