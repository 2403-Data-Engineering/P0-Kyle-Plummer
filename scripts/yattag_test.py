from yattag import Doc

headers = ['ID', 'Name', 'Email', 'Department', 'Salary']
rows = [
    ['1', 'Alice Johnson', 'alice@example.com', 'Engineering', '$95,000'],
    ['2', 'Bob Smith', 'bob@example.com', 'Marketing', '$78,000'],
    ['3', 'Carol Lee', 'carol@example.com', 'Finance', '$88,000'],
    ['4', 'Dave Patel', 'dave@example.com', 'Engineering', '$102,000'],
]



doc, tag, text = Doc().tagtext()

doc.asis('<!DOCTYPE html>')
with tag('html'): # <html>
    with tag('head'):
        with tag('title'): # <title>
            text("This is the Enrollment Report")
        # Title block closes here, so title tag gets closed here - </title>
    with tag('body'):
        with tag('h1'):
            text("Student: " + "Plummer, Kyle")
        with tag('table', border='1', cellpadding='5', cellspacing='0'):
            with tag('tr'):
                for h in headers:
                    with tag('th'):
                        text(h)
            for row in rows:
                with tag('tr'):
                    for cell in row:
                        with tag('td'):
                            text(cell)
 
        doc.stag('img', src='photo.jpg', alt='A photo')
        with tag('a', href='https://example.com'):
            text('Visit Example')

result = doc.getvalue()
with open("report.html", "w") as f:
    f.write(result)