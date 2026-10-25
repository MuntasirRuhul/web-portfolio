# Curl straight quotes and apostrophes in the visible text of an HTML page
# (text between tags only; <script>, <style> and attribute values are untouched).
#   python3 atelier/tools/curl-text.py atelier/page.html
import re, sys
def curl(t):
    t = re.sub(r'"([^"<>]*)"', '“\\1”', t)
    t = re.sub(r"(\w)'(\w)", "\\1’\\2", t)        # can't, Elena's
    t = re.sub(r"(\s|^)'(\w)", "\\1‘\\2", t)       # opening single quote
    return t.replace("'", "’")
for path in sys.argv[1:]:
    s = open(path).read()
    i = s.find('<body')
    head, body = s[:i], s[i:]
    parts = re.split(r'(<script.*?</script>|<style.*?</style>)', body, flags=re.S)
    out = [p if p.startswith(('<script', '<style')) else re.sub(r'>([^<]+)<', lambda m: '>' + curl(m.group(1)) + '<', p) for p in parts]
    open(path, 'w').write(head + ''.join(out))
    print(path, 'curled')
