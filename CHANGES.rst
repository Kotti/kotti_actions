History
=======

0.1.1 (2015-03-19)
------------------

- Updated README.
  [davidemoro]

- Fixed Travis CI build
  [davidemoro]

- Added target column on LinkAction objects (optional).
  We provides a select with empty option (default) or _blank (new window).

  *IMPORTANT*: required migration from 0.1 version
  ``kotti-migrate yourconfigfile.ini upgrade --scripts=kotti_actions:alembic``
  [davidemoro]

- Now the link attribute on LinkAction items supports also emails mailto:example@email.com
  [davidemoro]


0.1 (2015-02-24)
----------------

- Prerelease tag.
  [davidemoro]
