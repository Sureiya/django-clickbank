# [Changelog](/releases)

## [0.1.4](/compare/0.1.3...0.1.4)

* [484df5d](/commit/484df5d) Fixed spelling on insufficient_funds signal
* [adc29c9](/commit/adc29c9) Upped number of test posts generated
* [879dd7c](/commit/879dd7c) Added resending signals when CLICKBANK_DEBUG is on, also adding logging
* [bfe0851](/commit/bfe0851) Fixed url in setup.py
* [8f7d34b](/commit/8f7d34b) Fixed indentation on README.md
* [658f2d1](/commit/658f2d1) Updated README.md with logging setup
* [9f04273](/commit/9f04273) Added migrations and admin.py to coverage exclusion
* [810066f](/commit/810066f) Added coveralls button
* [ad32a9d](/commit/ad32a9d) Added travis button to README.md
* [d551915](/commit/d551915) Added coveralls to travis config
* [5ae5524](/commit/5ae5524) Updated travis config
* [1a9efea](/commit/1a9efea) Added travis config file
* [42d3019](/commit/42d3019) Added logging for duplicate receipt

## [0.1.3](/compare/0.1.2...0.1.3)

* [eba882e](/commit/eba882e) Added duplicate test_post to test duplicate_receipt logic
* [6404f84](/commit/6404f84) Added exclusion to form validation so that ipn returns status 200 on duplicate receipt
* [0b78732](/commit/0b78732) Added index to receipt for faster lookups
* [161324f](/commit/161324f) Updated long_description for packaging

## [0.1.2](/compare/0.1.1...0.1.2)

* [e671358](/commit/e671358) Added new test_post for testing rebill notification
* [52852eb](/commit/52852eb) Updated the future_date_generator and added date_to_datetime to support future_payments format
* [3010f69](/commit/3010f69) Added sublime project files to .gitignore
* [755f9a3](/commit/755f9a3) Added build directory to makefile clean

## [0.1.1](/compare/0.1.1...0.1.1)

* [482c02d](/commit/482c02d) Updated README with links
* [ba660d1](/commit/ba660d1) Added long_description to setup.py
* [15035c0](/commit/15035c0) Added documentation to README.md
* [b72c759](/commit/b72c759) Added dist directory to make clean
* [0b8a7bd](/commit/0b8a7bd) Moved README.md to README.rst so it can be used to make pypi page as well.
* [94a89c0](/commit/94a89c0) Lowered the number of test posts generated
* [81f260c](/commit/81f260c) Updated package name
* [59870dc](/commit/59870dc) Added Makefile with clean command to remove extra files added by testing and packaging
* [490f061](/commit/490f061) Added files needed for packaging, installation, and automated testing.
* [2b7188c](/commit/2b7188c) Added .gitignore
* [900bea5](/commit/900bea5) Added README and CHANGELOG
* [618ed71](/commit/618ed71) Removed test for debug_ipn since it no longer exists
* [1dd8062](/commit/1dd8062) Added license
* [a70dc20](/commit/a70dc20) Moved to subfolder for packaging
* [b6da793](/commit/b6da793) Fixed date conversion Documentation added where missing PEP8 and flake8 run-through
* [5c26e29](/commit/5c26e29) More json fallback for missing simplejson
* [c80e3cd](/commit/c80e3cd) Fixed invalid settings
* [bbc19d8](/commit/bbc19d8) simplejson should not be required.
* [cd95914](/commit/cd95914) django_clickbank is feature complete
* [ef8467d](/commit/ef8467d) Initial commit of django_clickbank