# Security audit: apache/fory

Date: 2026-11-16 | Auditor: [mutsuumii](https://github.com/mutsuumii)

## Summary

Found 10 issue(s): 8 critical, 2 high.

## Findings

### 1. [CRITICAL] Insecure deserialization

**CWE-502** | `benchmarks/python/fory_benchmark.py` line 295

Deserializing untrusted data with pickle or yaml.load. Attacker executes arbitrary code.

```
pickle.loads(binary)
```

**Fix:** Use json for data, yaml.safe_load() for YAML. Never unpickle untrusted input.
---

### 2. [CRITICAL] Insecure deserialization

**CWE-502** | `benchmarks/python/fory_benchmark.py` line 303

Deserializing untrusted data with pickle or yaml.load. Attacker executes arbitrary code.

```
pickle.loads(binary)
```

**Fix:** Use json for data, yaml.safe_load() for YAML. Never unpickle untrusted input.
---

### 3. [CRITICAL] Command injection via shell=True

**CWE-78** | `python/pyfory/tests/test_reduce_serializer.py` line 88

User input passed to a shell command. Attacker can execute arbitrary OS commands.

```
return os.system, ()
```

**Fix:** Use subprocess.run(['cmd', arg], shell=False). Never build shell strings from input.
---

### 4. [CRITICAL] Command injection via shell=True

**CWE-78** | `python/pyfory/tests/test_reduce_serializer.py` line 401

User input passed to a shell command. Attacker can execute arbitrary OS commands.

```
writer.register_type(type(os.system))
```

**Fix:** Use subprocess.run(['cmd', arg], shell=False). Never build shell strings from input.
---

### 5. [CRITICAL] Command injection via shell=True

**CWE-78** | `python/pyfory/tests/test_reduce_serializer.py` line 406

User input passed to a shell command. Attacker can execute arbitrary OS commands.

```
reader.register_type(type(os.system))
```

**Fix:** Use subprocess.run(['cmd', arg], shell=False). Never build shell strings from input.
---

### 6. [HIGH] Hardcoded credentials

**CWE-798** | `python/pyfory/tests/test_reduce_serializer.py` line 143

Credentials hardcoded in source. Anyone with repo access can extract them.

```
self.secret = "hidden"
```

**Fix:** Use os.environ.get('SECRET') or a secrets manager. Never commit credentials.
---

### 7. [HIGH] Hardcoded credentials

**CWE-798** | `python/pyfory/tests/test_stateful_serializer.py` line 37

Credentials hardcoded in source. Anyone with repo access can extract them.

```
self.secret = "restored_secret"
```

**Fix:** Use os.environ.get('SECRET') or a secrets manager. Never commit credentials.
---

### 8. [CRITICAL] Insecure deserialization

**CWE-502** | `benchmarks/python/benchmark.py` line 794

Deserializing untrusted data with pickle or yaml.load. Attacker executes arbitrary code.

```
pickle.loads(binary)
```

**Fix:** Use json for data, yaml.safe_load() for YAML. Never unpickle untrusted input.
---

### 9. [CRITICAL] Format string vulnerability

**CWE-134** | `cpp/fory/util/time_util.cc` line 43

User-controlled string passed as printf format argument. Attacker reads stack memory or overwrites return addresses via %n.

```
std::snprintf(datetime_str + written_size,
```

**Fix:** Use a literal format string: printf("%s", user_input). Never pass user data as the format argument.
---

### 10. [CRITICAL] Insecure deserialization

**CWE-502** | `python/pyfory/tests/benchmark.py` line 52

Deserializing untrusted data with pickle or yaml.load. Attacker executes arbitrary code.

```
t2 = timeit.timeit(lambda: pickle.loads(pickled_data), number=iter_nums)
```

**Fix:** Use json for data, yaml.safe_load() for YAML. Never unpickle untrusted input.
---
