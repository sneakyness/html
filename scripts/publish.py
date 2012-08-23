import os, sys
import bs, boilerplate
from StringIO import StringIO
from anolislib import generator, utils

if len(sys.argv)>1 and sys.argv[1] == 'html':
  select = 'w3c-html' 
  spec = 'html'
elif len(sys.argv)>1 and sys.argv[1] == '2dcontext':
  spec = select = '2dcontext'
else:
  sys.stderr.write("Usage: python %s [html|2dcontext]\n" % sys.argv[0])
  exit()

print 'parsing'
os.chdir(os.path.abspath(os.path.join(__file__, '../..')))
source = open('source')
succint = StringIO()
bs.main(source, succint)

succint.seek(0)
filtered = StringIO()
boilerplate.main(succint, filtered, select)
succint.close()

# See http://hg.gsnedders.com/anolis/file/tip/anolis
opts = {
  'allow_duplicate_dfns': True,
  'disable': None,
  'escape_lt_in_attrs': False,
  'escape_rcdata': False,
  'force_html4_id': False,
  'indent_char': u' ',
  'inject_meta_charset': False,
  'max_depth': 6,
  'min_depth': 2,
  'minimize_boolean_attributes': False,
  'newline_char': u'\n',
  'omit_optional_tags': False,
  'output_encoding': 'utf-8',
  'parser': 'lxml.html',
  'processes': set(['toc', 'xref', 'sub']),
  'profile': False,
  'quote_attr_values': False,
  'serializer': 'html5lib',
  'space_before_trailing_solidus': False,
  'strip_whitespace': None,
  'use_best_quote_char': False,
  'use_trailing_solidus': False,
  'w3c_compat_class_toc': False,
  'w3c_compat_crazy_substitutions': False,
  'w3c_compat_substitutions': False,
  'w3c_compat': True,
  'w3c_compat_xref_a_placement': False,
  'w3c_compat_xref_elements': False,
  'w3c_compat_xref_normalization': False,
}

print 'indexing'
filtered.seek(0)
tree = generator.fromFile(filtered, **opts)
filtered.close()

try:
  os.makedirs('output/%s' % spec)
except:
  pass

if spec == 'html':
  from glob import glob
  for name in glob('output/html/*.html'):
    os.remove(name)

  output = open('output/html/single-page.html', 'wb')
else:
  output = open('output/%s/Overview.html' % spec, 'wb')

generator.toFile(tree, output, **opts)
output.close()

if spec == 'html':
  print 'splitting'
  import spec_splitter
  spec_splitter.w3c = True
  spec_splitter.main('output/html/single-page.html', 'output/html')
