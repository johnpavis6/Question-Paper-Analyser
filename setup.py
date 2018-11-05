import json


def _read(filename):
    with open('./categories/%s' % (filename,), 'r') as fp:
        data = fp.read()
        words = [s.strip() for s in data.splitlines()]
        categories[filename] = words


categories, filenames = {}, ['application', 'knowledge',
                             'evaluation', 'comprehension',
                             'synthesis', 'analysis']
for filename in filenames:
    _read(filename)

with open('categories.json', 'w+') as fp:
    fp.write(json.dumps(categories))

with open('categories.json', 'r') as fp:
    content = fp.read()
    print type(json.loads(content)), type(content)
