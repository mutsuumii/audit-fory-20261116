# Hardcoded credentials
# CWE-798 | Severity: HIGH
# File: python/pyfory/tests/test_stateful_serializer.py line 37

**Risk:** Credentials hardcoded in source. Anyone with repo access can extract them.

**Fix:** Use os.environ.get('SECRET') or a secrets manager. Never commit credentials.
