Code for Maine Website
======================

Easy bootstrapping!
-------------------

Powered by the ubiquitous Makefile ... this should be pretty easy:

1. make deps or make deps_mac (or even make deps_freebsd)
2. make install
3. make run
4. open your browser to: http://127.0.0.1:45000

Note, for a full local bootstrapping you will also need to install Postgres for
your platform, and grab a current working copy of the production database. In
the future, the hope is for this to all be automated via django management
commands. But in the immortal words of Homer Simpson, "I'm only one man,
Marge."

Releases
--------

This codebase is only released via signed packages uploaded to the Five Q PyPI
server. In order to create a new release you need to make sure you've installed
extra development packages from the requirements file (pip install -r
requirements.txt). This will get you wheel and twine, both of which are needed
for packaging.

Once you've got those installed, you simply run:

```
make release v="X.X.X"
```

Where X.X.X is your version number. Check the git tags to see wha the next
version should be. The project follows content semver rules for versioning.
Generally speaking, this means major.minor.bugfix(a)development, for example:

2.0.0 is an initial release after updating an outward facing part of the site,
urls, content, or major page structure changes.

2.1.0 is a minor version where a url was moved, or some CSS improvements have
been made.

2.1.1 is a bugfix, silly us, we allowed a release with something that wasn't
doing what it was supposed to.

2.1.1.dev1 is a development release, useful for pushing up to
staging sites allowing a client to test a release before we finalize it.

Note, you cannot use a hyphen in the development versions, as twine and most of
PyPI will choke on you.

Deployments
-----------

Once you've got your release packaged and up on PyPI, you're next step will be
to get it released to some sort of external server. This can be accomplished
using another make rule:

```
make stage v="X.X.X"

make deploy

make redeploy v="X.X.X"
```

It is intentional that you are allowed to specify a version for staging, but
production will always simply install the most recent stable version. This rule
will pull our Houston deployment library into a hidden directory and do some
fancy bootstrapping before just running an Ansible command against a set of
servers that are specified in Houston.

Docker images
-------------

This is a work in progress, and for Bowery does not work yet. Please take a
look and heal the horribly configuration wounds inflicted by the last dev to
try to get these setup if you're so inclined.
