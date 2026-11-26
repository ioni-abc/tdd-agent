# ClassEval_70

## Skeleton (what the agent sees)

```python
class PersonRequest:
    """
    This class validates input personal information data and sets invalid fields to None based to specific rules.
    """

    def __init__(self, name: str, sex: str, phoneNumber: str):
        """
        Initialize PersonRequest object with the provided information.
        :param name: str, the name of the person
        :param sex: str, the sex of the person
        :param phoneNumber: str, the phone number of the person
        """
        self.name = self._validate_name(name)
        self.sex = self._validate_sex(sex)
        self.phoneNumber = self._validate_phoneNumber(phoneNumber)


    def _validate_name(self, name: str) -> str:
        """
        Validate the name and return it. If name is empty or exceeds 33 characters in length, set to None.
        :param name: str, the name to validate
        :return: str, the validated name or None if invalid
        """


    def _validate_sex(self, sex: str) -> str:
        """
        Validate the sex and return it. If sex is not Man, Woman, or UGM, set to None.
        :param sex: str, the sex to validate
        :return: str, the validated sex or None if invalid
        """

    def _validate_phoneNumber(self, phoneNumber: str) -> str:
        """
        Validate the phone number and return it. If phoneNumber is empty or not an 11 digit number, set to None.
        :param phoneNumber: str, the phone number to validate
        :return: str, the validated phone number or None if invalid
        """
```

## Method `_validate_name`

### Docstring

```python
def _validate_name(self, name: str) -> str:
        """
        Validate the name and return it. If name is empty or exceeds 33 characters in length, set to None.
        :param name: str, the name to validate
        :return: str, the validated name or None if invalid
        """
```

### Reference code (`solution_code`)

```python
def _validate_name(self, name: str) -> str:
        if not name:
            return None
        if len(name) > 33:
            return None
        return name
```

### Tests (`PersonRequestTestValidateName`)

**test_validate_name_1**: `stated`
- reason: The docstring says an empty name is set to None, which is exactly what the test checks when it passes "" and expects `pr.name` to be None.

```python
def test_validate_name_1(self):
    pr = PersonRequest("", "Man", "12345678901")
    self.assertIsNone(pr.name)
```

**test_validate_name_2**: `stated`
- reason: The docstring says a name longer than 33 characters is set to None, and the test passes a name well over that limit and expects `pr.name` to be None, which a correct implementation would satisfy.

```python
def test_validate_name_2(self):
    pr = PersonRequest("This is a very long name that exceeds the character limit", "Man",
                       "12345678901")
    self.assertIsNone(pr.name)
```

**test_validate_name_3**: `stated`
- reason: The docstring says a valid name is returned unchanged and only empty or over-33-character names become None, so a programmer would return "aaa" for a short non-empty name, as the test expects.

```python
def test_validate_name_3(self):
    pr = PersonRequest("aaa", "Man", "12345678901")
    self.assertEqual(pr.name, 'aaa')
```

**test_validate_name_4**: `stated`
- reason: The test passes a short non-empty name ("bbb", well under 33 characters) and expects it returned unchanged, which is exactly what the docstring's "validate the name and return it" with only empty/over-33 cases set to None implies.

```python
def test_validate_name_4(self):
    pr = PersonRequest("bbb", "Man", "12345678901")
    self.assertEqual(pr.name, 'bbb')
```

**test_validate_name_5**: `stated`
- reason: The docstring says the name is returned unless it is empty or longer than 33 characters, so a short non-empty name like 'ccc' should come back unchanged, which is what the test checks.

```python
def test_validate_name_5(self):
    pr = PersonRequest("ccc", "Man", "12345678901")
    self.assertEqual(pr.name, 'ccc')
```

## Method `_validate_sex`

### Docstring

```python
def _validate_sex(self, sex: str) -> str:
        """
        Validate the sex and return it. If sex is not Man, Woman, or UGM, set to None.
        :param sex: str, the sex to validate
        :return: str, the validated sex or None if invalid
        """
```

### Reference code (`solution_code`)

```python
def _validate_sex(self, sex: str) -> str:
        if sex not in ["Man", "Woman", "UGM"]:
            return None
        return sex
```

### Tests (`PersonRequestTestValidateSex`)

**test_validate_sex_1**: `stated`
- reason: The docstring says any sex other than Man, Woman, or UGM is set to None, which is exactly what the test checks when "Unknown" is passed to the constructor.

```python
def test_validate_sex_1(self):
    pr = PersonRequest("John Doe", "Unknown", "12345678901")
    self.assertIsNone(pr.sex)
```

**test_validate_sex_2**: `stated`
- reason: The docstring says "UGM" is a valid sex that should be returned unchanged, so a programmer following it would keep "UGM" and pass this test.

```python
def test_validate_sex_2(self):
    pr = PersonRequest("John Doe", "UGM", "12345678901")
    self.assertEqual(pr.sex, "UGM")
```

**test_validate_sex_3**: `stated`
- reason: The docstring says valid values (Man, Woman, UGM) are returned as-is, and the test checks that a valid "Man" is kept on the request's sex attribute, which a programmer following the docstring would pass.

```python
def test_validate_sex_3(self):
    pr = PersonRequest("John Doe", "Man", "12345678901")
    self.assertEqual(pr.sex, "Man")
```

**test_validate_sex_4**: `stated`
- reason: The docstring says valid sexes (Man, Woman, UGM) are returned unchanged, so a programmer following it would return "Woman" for this input and pass.

```python
def test_validate_sex_4(self):
    pr = PersonRequest("John Doe", "Woman", "12345678901")
    self.assertEqual(pr.sex, "Woman")
```

**test_validate_sex_5**: `stated`
- reason: The docstring says any sex other than Man, Woman, or UGM becomes None, which is what the test checks for the invalid value "khsigy" on the stored attribute.

```python
def test_validate_sex_5(self):
    pr = PersonRequest("John Doe", "khsigy", "12345678901")
    self.assertIsNone(pr.sex)
```

## Method `_validate_phoneNumber`

### Docstring

```python
def _validate_phoneNumber(self, phoneNumber: str) -> str:
        """
        Validate the phone number and return it. If phoneNumber is empty or not an 11 digit number, set to None.
        :param phoneNumber: str, the phone number to validate
        :return: str, the validated phone number or None if invalid
        """
```

### Reference code (`solution_code`)

```python
def _validate_phoneNumber(self, phoneNumber: str) -> str:
        if not phoneNumber:
            return None
        if len(phoneNumber) != 11 or not phoneNumber.isdigit():
            return None
        return phoneNumber
```

### Tests (`PersonRequestTestValidatePhoneNumber`)

**test_validate_phoneNumber_1**: `stated`
- reason: The docstring says an empty phone number should be set to None, and the test passes an empty string and expects None, which a programmer following the docstring would produce.

```python
def test_validate_phoneNumber_1(self):
    pr = PersonRequest("John Doe", "Man", "")
    self.assertIsNone(pr.phoneNumber)
```

**test_validate_phoneNumber_2**: `stated`
- reason: The docstring says a phone number that is empty or not 11 digits becomes None, and the test passes a 5-digit number and expects None, which is exactly that rule.

```python
def test_validate_phoneNumber_2(self):
    pr = PersonRequest("John Doe", "Man", "12345")
    self.assertIsNone(pr.phoneNumber)
```

**test_validate_phoneNumber_3**: `stated`
- reason: The docstring says a non-empty, non-11-digit input becomes None, so a programmer following it would return None for the short non-numeric string this test passes in.

```python
def test_validate_phoneNumber_3(self):
    pr = PersonRequest("John Doe", "Man", "jgdjrj")
    self.assertIsNone(pr.phoneNumber)
```

**test_validate_phoneNumber_4**: `stated`
- reason: The docstring says a valid 11-digit phone number is returned unchanged, and the test passes an 11-digit number and expects it back, so a programmer following the docstring would pass.

```python
def test_validate_phoneNumber_4(self):
    pr = PersonRequest("John Doe", "Man", "12345678901")
    self.assertEqual(pr.phoneNumber, "12345678901")
```

**test_validate_phoneNumber_5**: `stated`
- reason: The docstring says a phone number that is an 11-digit number is returned unchanged, and the test passes an 11-digit string and expects it back, so a programmer following the docstring would pass.

```python
def test_validate_phoneNumber_5(self):
    pr = PersonRequest("John Doe", "Man", "11111111111")
    self.assertEqual(pr.phoneNumber, "11111111111")
```

## Tests in no method's test class

### `PersonRequestTest`

**test_PersonRequest**: `no_method_info`
- reason: its test class is in no methods_info[i]['test_class']

```python
def test_PersonRequest(self):
    pr = PersonRequest("", "Man", "12345678901")
    self.assertIsNone(pr.name)

    pr = PersonRequest("John Doe", "Unknown", "12345678901")
    self.assertIsNone(pr.sex)

    pr = PersonRequest("John Doe", "Man", "")
    self.assertIsNone(pr.phoneNumber)
```
