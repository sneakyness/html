html
====

Deliverables of the HTML Working Group

---

Build instructions:

    ruby scripts/boilerplate.rb [2dcontext] > /tmp/html5.in
    anolis --w3c-compat --allow-duplicate-dfns --parser=lxml.html \
      /tmp/htm5.in /tmp/Overview.html
