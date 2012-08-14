Dir.chdir File.expand_path('../..', __FILE__)

# select document
if ARGV.first == '2dcontext'
  header = File.read("boilerplate/header-w3c-html-2dcontext")
  select = '2dcontext'
else
  header = File.read("boilerplate/header-w3c-html-core")
  select = 'w3c-html'
end

# remove instructions
header.gsub! /<!-- .*? -->\n?/m, ''

# capture variables
vars = {}
header.gsub! /<!--SET (\w+)=(.*?)-->\n?/ do
  vars[$1] = $2
  ''
end

# include nested boiler plate
header.gsub! /<!--BOILERPLATE ([-\w]+)-->/ do |content|
  if File.exist? "boilerplate/#{$1}"
    content = File.read("boilerplate/#{$1}")
  else
    STDERR.puts "Missing file: #{$1}"
  end

  # substitute variables
  content.gsub!(/<!--INSERT (\w+)-->/) { vars[$1] }

  # use content as the replacement
  content
end

source = File.read('source')
source.sub! /\A.*?<!--START #{select}-->/m, ''

content =  header + source

content.gsub! /<!--END #{select}-->.*?<!--START #{select}-->/m, ''
content.sub! /<!--END #{select}-->.*\Z/m, ''

content.gsub! /<!--(START|END) [-\w]+-->/, ''

# select based on the value of PUB
if vars['PUB'] == '1'
  content.gsub! /^<!--PUB-N-->.*\n?/, ''
  content.gsub! /^<!--PUB-Y-->/, ''
else
  content.gsub! /^<!--PUB-Y-->.*\n?/, ''
  content.gsub! /^<!--PUB-N-->/, ''
end

puts content
