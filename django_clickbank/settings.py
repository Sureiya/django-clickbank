## Setting debug to True turns off things like secret key verification
CLICKBANK_DEBUG = False

## If set to true raw post data will be stored regardless of CLICKBANK_DEBUG
CLICKBANK_STORE_POSTS = True

## If set to true, app will still log notifications when verification fails
CLICKBANK_KEEP_INVALID = True

## When set to true, app will still send signal when invalid notification recieved.
CLICKBANK_SIGNAL_INVALID = False

## Send 200 status when a transaction is received that already exists. Mostly for debugging
CLICKBANK_IGNORE_DUPLICATES = False

## Allow resending signals in admin
CLICKBANK_RESEND_SIGNALS = False