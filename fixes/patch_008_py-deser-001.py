# Insecure deserialization
# CWE-502 | Severity: CRITICAL
# File: benchmarks/python/benchmark.py line 794

**Risk:** Deserializing untrusted data with pickle or yaml.load. Attacker executes arbitrary code.

**Fix:** Use json for data, yaml.safe_load() for YAML. Never unpickle untrusted input.
