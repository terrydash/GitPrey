import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_DIR = os.path.join(BASE_DIR, 'logs')
HTML_DIR = os.path.join(BASE_DIR, 'html')
TEMPLATE_FILE = os.path.join(HTML_DIR, 'template.html')

def make_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)


make_dir(LOG_DIR)
make_dir(HTML_DIR)
if __name__ == "__main__":
    print(BASE_DIR)
    print(LOG_DIR)
