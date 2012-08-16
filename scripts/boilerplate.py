import sys

def main(stdin, stdout, select='w3c-html'):
  import os, re
  os.chdir(os.path.abspath(os.path.join(__file__, '../..')))

  # select document
  if select == '2dcontext':
    header = open("boilerplate/header-w3c-html-2dcontext").read()
  else:
    header = open("boilerplate/header-w3c-html-core").read()

  # remove instructions
  header = re.compile('<!-- .*? -->\n?', re.S).sub('', header)

  # capture variables
  vars = {}
  def vset(match): 
    vars[match.group(1)]=match.group(2)
    return ''
  header = re.sub('<!--SET (\w+)=(.*?)-->\n?', vset, header)

  # include nested boiler plate
  def boilerplate(match):
    name = match.group(1)
    if os.path.exists("boilerplate/%s" % name):
      content = open("boilerplate/%s" % name).read()
    else:
      content = match.group(0)
      sys.stderr.write("Missing file: %s\n" % name)

    # substitute variables
    content = re.sub('<!--INSERT (\w+)-->', lambda n: vars[n.group(1)], content)

    # use content as the replacement
    return content
  header = re.sub('<!--BOILERPLATE ([-\w]+)-->', boilerplate, header)

  source = stdin.read()
  source = re.compile('^.*?<!--START %s-->' % select, re.DOTALL).sub('', source)

  content =  header + source

  content = re.compile('<!--END %s-->.*?<!--START %s-->' % (select,select), re.DOTALL).sub('', content)
  content = re.compile('<!--END %s-->.*' % select, re.DOTALL).sub('', content)

  content = re.sub('<!--(START|END) [-\w]+-->\n?', '', content)

  # select based on the value of PUB
  if vars['PUB'] == '1':
    content = re.compile('^<!--PUB-N-->.*?\n', re.M).sub('', content)
    content = re.compile('^<!--PUB-Y-->', re.M).sub('', content)
  else:
    content = re.compile('^<!--PUB-Y-->.*?\n', re.M).sub('', content)
    content = re.compile('^<!--PUB-N-->', re.M).sub('', content)

  stdout.write(content)

if __name__ == '__main__':
  if len(sys.argv)>1 and sys.argv[1] == '2dcontext':
    select = '2dcontext'
  else:
    select = 'w3c-html'

  main(select)
