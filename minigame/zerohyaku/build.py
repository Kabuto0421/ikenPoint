"""src/game.html + src/TegakiFont.ttf -> index.html (フォント埋め込み済み・単体で動く)"""
import base64, pathlib
here = pathlib.Path(__file__).parent
src = (here / 'src' / 'game.html').read_text(encoding='utf-8')
b64 = base64.b64encode((here / 'src' / 'TegakiFont.ttf').read_bytes()).decode()
body = src.replace('__FONT_B64__', b64)
(here / 'index.html').write_text(
    '<!doctype html>\n<html lang="ja">\n<head>\n<meta charset="utf-8">\n'
    '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
    + body + '\n</html>\n', encoding='utf-8')
# artifact 用 (doctype なしの断片)
out = pathlib.Path(__import__('sys').argv[1]) if len(__import__('sys').argv) > 1 else None
if out: out.write_text(body, encoding='utf-8')
print('ok', len(body))
