# [Changelog](https://github.com/sureiya/django-clickbank/releases)

## [0.2.5](https://github.com/sureiya/django-clickbank/compare/0.2.4...0.2.5)

* [47d454d](https://github.com/sureiya/django-clickbank/commit/47d454d) Added configuration setting for admin signal resend action

## [0.2.4](https://github.com/sureiya/django-clickbank/compare/0.2.3...0.2.4)

* [afb1fb3](https://github.com/sureiya/django-clickbank/commit/afb1fb3) Fixed MultipleReturns on duplicate notification

## [0.2.3](https://github.com/sureiya/django-clickbank/compare/0.2.2...0.2.3)

* [539af5d](https://github.com/sureiya/django-clickbank/commit/539af5d) Added search fields to notification admin
* [191be6a](https://github.com/sureiya/django-clickbank/commit/191be6a) Fixed links on changelog
* [635fa48](https://github.com/sureiya/django-clickbank/commit/635fa48) Added __url__

## [0.2.2](https://github.com/sureiya/django-clickbank/compare/0.2.0...0.2.2)

* [08fa085](https://github.com/sureiya/django-clickbank/commit/08fa085) Fixed keyerror on form error handling
* [60ed80a](https://github.com/sureiya/django-clickbank/commit/60ed80a) Changed CANCELLED -> CANCELED. Thanks America.
* [3a23c08](https://github.com/sureiya/django-clickbank/commit/3a23c08) Version bump
* [1aa055c](https://github.com/sureiya/django-clickbank/commit/1aa055c) Updated CHANGELOG.md

## [0.2.0](https://github.com/sureiya/django-clickbank/compare/0.1.4...0.2.0)

* [7239324](https://github.com/sureiya/django-clickbank/commit/7239324) Add tox to normal requirements to appease changes
* [9900b22](https://github.com/sureiya/django-clickbank/commit/9900b22) Added admin action "resend_signals"
* [e25b2f9](https://github.com/sureiya/django-clickbank/commit/e25b2f9) Re-added notification duplication detection
* [6d0867f](https://github.com/sureiya/django-clickbank/commit/6d0867f) Added refund_parent method to get a refunds parent notification
* [4fc2024](https://github.com/sureiya/django-clickbank/commit/4fc2024) Added new rebill_parent_receipt field and methods to retrieve parent notifications
* [ba3982a](https://github.com/sureiya/django-clickbank/commit/ba3982a) Removed uniqueness from receipt, added unique_together
* [5fdc954](https://github.com/sureiya/django-clickbank/commit/5fdc954) Cleaned up admin interface
* [a4a7077](https://github.com/sureiya/django-clickbank/commit/a4a7077) Add a Bitdeli badge to README

## [0.1.4](https://github.com/sureiya/django-clickbank/compare/0.1.3...0.1.4)

* [484df5d](https://github.com/sureiya/django-clickbank/commit/484df5d) Fixed spelling on insufficient_funds signal
* [adc29c9](https://github.com/sureiya/django-clickbank/commit/adc29c9) Upped number of test posts generated
* [879dd7c](https://github.com/sureiya/django-clickbank/commit/879dd7c) Added resending signals when CLICKBANK_DEBUG is on, also adding logging
* [bfe0851](https://github.com/sureiya/django-clickbank/commit/bfe0851) Fixed url in setup.py
* [8f7d34b](https://github.com/sureiya/django-clickbank/commit/8f7d34b) Fixed indentation on README.md
* [658f2d1](https://github.com/sureiya/django-clickbank/commit/658f2d1) Updated README.md with logging setup
* [9f04273](https://github.com/sureiya/django-clickbank/commit/9f04273) Added migrations and admin.py to coverage exclusion
* [810066f](https://github.com/sureiya/django-clickbank/commit/810066f) Added coveralls button
* [ad32a9d](https://github.com/sureiya/django-clickbank/commit/ad32a9d) Added travis button to README.md
* [d551915](https://github.com/sureiya/django-clickbank/commit/d551915) Added coveralls to travis config
* [5ae5524](https://github.com/sureiya/django-clickbank/commit/5ae5524) Updated travis config
* [1a9efea](https://github.com/sureiya/django-clickbank/commit/1a9efea) Added travis config file
* [42d3019](https://github.com/sureiya/django-clickbank/commit/42d3019) Added logging for duplicate receipt

## [0.1.3](https://github.com/sureiya/django-clickbank/compare/0.1.2...0.1.3)

* [eba882e](https://github.com/sureiya/django-clickbank/commit/eba882e) Added duplicate test_post to test duplicate_receipt logic
* [6404f84](https://github.com/sureiya/django-clickbank/commit/6404f84) Added exclusion to form validation so that ipn returns status 200 on duplicate receipt
* [0b78732](https://github.com/sureiya/django-clickbank/commit/0b78732) Added index to receipt for faster lookups
* [161324f](https://github.com/sureiya/django-clickbank/commit/161324f) Updated long_description for packaging

## [0.1.2](https://github.com/sureiya/django-clickbank/compare/0.1.1...0.1.2)

* [e671358](https://github.com/sureiya/django-clickbank/commit/e671358) Added new test_post for testing rebill notification
* [52852eb](https://github.com/sureiya/django-clickbank/commit/52852eb) Updated the future_date_generator and added date_to_datetime to support future_payments format
* [3010f69](https://github.com/sureiya/django-clickbank/commit/3010f69) Added sublime project files to .gitignore
* [755f9a3](https://github.com/sureiya/django-clickbank/commit/755f9a3) Added build directory to makefile clean

## [0.1.1](https://github.com/sureiya/django-clickbank/compare/0.1.1...0.1.1)

* [482c02d](https://github.com/sureiya/django-clickbank/commit/482c02d) Updated README with links
* [ba660d1](https://github.com/sureiya/django-clickbank/commit/ba660d1) Added long_description to setup.py
* [15035c0](https://github.com/sureiya/django-clickbank/commit/15035c0) Added documentation to README.md
* [b72c759](https://github.com/sureiya/django-clickbank/commit/b72c759) Added dist directory to make clean
* [0b8a7bd](https://github.com/sureiya/django-clickbank/commit/0b8a7bd) Moved README.md to README.rst so it can be used to make pypi page as well.
* [94a89c0](https://github.com/sureiya/django-clickbank/commit/94a89c0) Lowered the number of test posts generated
* [81f260c](https://github.com/sureiya/django-clickbank/commit/81f260c) Updated package name
* [59870dc](https://github.com/sureiya/django-clickbank/commit/59870dc) Added Makefile with clean command to remove extra files added by testing and packaging
* [490f061](https://github.com/sureiya/django-clickbank/commit/490f061) Added files needed for packaging, installation, and automated testing.
* [2b7188c](https://github.com/sureiya/django-clickbank/commit/2b7188c) Added .gitignore
* [900bea5](https://github.com/sureiya/django-clickbank/commit/900bea5) Added README and CHANGELOG
* [618ed71](https://github.com/sureiya/django-clickbank/commit/618ed71) Removed test for debug_ipn since it no longer exists
* [1dd8062](https://github.com/sureiya/django-clickbank/commit/1dd8062) Added license
* [a70dc20](https://github.com/sureiya/django-clickbank/commit/a70dc20) Moved to subfolder for packaging
* [b6da793](https://github.com/sureiya/django-clickbank/commit/b6da793) Fixed date conversion Documentation added where missing PEP8 and flake8 run-through
* [5c26e29](https://github.com/sureiya/django-clickbank/commit/5c26e29) More json fallback for missing simplejson
* [c80e3cd](https://github.com/sureiya/django-clickbank/commit/c80e3cd) Fixed invalid settings
* [bbc19d8](https://github.com/sureiya/django-clickbank/commit/bbc19d8) simplejson should not be required.
* [cd95914](https://github.com/sureiya/django-clickbank/commit/cd95914) django_clickbank is feature complete
* [ef8467d](https://github.com/sureiya/django-clickbank/commit/ef8467d) Initial commit of django_clickbank