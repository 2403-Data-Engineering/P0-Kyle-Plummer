from yattag import Doc

doc, tag, text = Doc().tagtext()

doc.asis('<!DOCTYPE html>')
with tag('html'):
    with tag('head'):
        with tag('title'):
            text('My Page')
    with tag('body'):
        with tag('h1'):
            text('Hello, World!')
        with tag('p', id='main-paragraph'):
            text('This is a paragraph created with ')
            with tag('strong'):
                text('yattag')
            text('.')
        with tag('ul'):
            for item in ['Apple', 'Banana', 'Cherry']:
                with tag('li'):
                    text(item)
        doc.stag('img', src='photo.jpg', alt='A photo')
        with tag('a', href='https://example.com'):
            text('Visit Example')

result = doc.getvalue()
with open("report.html", "w") as f:
    f.write(result)