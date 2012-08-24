html
====

Deliverables of the HTML Working Group

---

Build instructions:

    python scripts/publish.py [html|2dcontext]

    output is placed in output/[html|2dcontext]

Spec Editing Cheatsheet
===

Checking out the HTML spec

   1. the HTML spec is on GitHub https://github.com/w3c/html

   2. there are multiple branches - get master to build the spec

Pull the code from GitHub:

    $ git clone git@github.com:w3c/html.git
    $ cd html
    $ git checkout -b whatwg origin/feature/whatwg
    Check what branches you now have:
    $ git branch

Configuring git
---

   * [Dealing with line endings](https://help.github.com/articles/dealing-with-line-endings)

Installing the necessary software
---

  1. you need to have python installed

  2. install anolislib:
https://github.com/sideshowbarker/html5forAuthors/tree/master/anolis/anolislib

Get anolislib from Mike’s github repo:

    $ git clone git://github.com/sideshowbarker/html5forAuthors.git
    $ mkdir ~/opt
    $ easy_install -d ~/opt html5lib
    $ easy_install -d ~/opt lxml
        
Build the HTML spec
---

    $ cd html
    $ git checkout master
    $ export PYTHONPATH=~/opt:~/Sites/html5/html5forAuthors/anolis/
    $ python scripts/publish.py html

Resulting page is in output/html/single-page.html
Or the multipage version at output/html/spec.html



Cherry pick commits from the WHATWG spec
---

   1. the WHATWG spec is developed in SVN at the WHATWG
   2. there is a git clone of it on GitHub
https://github.com/w3c/html/tree/feature/whatwg
   3. we cherry-pick commits from the WHATWG spec into the html spec

Checkout the WHATWG spec:

    $ git checkout whatwg

Find out commit differences to html branch:

    $ git cherry master

Find a commit that you want to apply, get it’s SHA:

    $ git log

Show the SHA commit e.g.:

    $git show 56446c4536af1ec5b39bde03b402d0772625fd92

Checkout the html spec:

    $ git checkout master

Cherry pick the commit selected from before:

    $ git cherry-pick -x 56446c4536af1ec5b39bde03b402d0772625fd92

If you want to edit the commit:

    $ git cherry-pick -x -e 56446c4536af1ec5b39bde03b402d0772625fd92

Show changes to GitHub:

    $ git diff origin

Create a new feature branch:
---
[make sure your .gitconfig defaults push to upstream]

    $ git checkout master
    $ git branch feature/blah
    $ git checkout feature/blah
    $ git push --set-upstream origin feature/blah


Merging a feature branch:
---
You should not use the GitHub pull request merge feature, but instead rebase locally and push (to avoid a messy merge and get a linear history):

    $ git checkout feature/blah
    $ git rebase master

Test everything still works, then push to GitHub:

    $ git push -f

Then merge on master:

    $ git checkout master
    $ git merge feature/blah
    $ git push

If you want to delete the branch, too, remove it both on local and GitHub (the issue with the pull request will continue to exist):

    $ git branch -d feature/blah
    $ git push origin :feature/blah
