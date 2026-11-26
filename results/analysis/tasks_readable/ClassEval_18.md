# ClassEval_18

## Skeleton (what the agent sees)

```python
class CamelCaseMap:
    """
    This is a custom class that allows keys to be in camel case style by converting them from underscore style, which provides dictionary-like functionality.
    """

    def __init__(self):
        """
        Initialize data to an empty dictionary
        """
        self._data = {}

    def __getitem__(self, key):
        """
        Return the value corresponding to the key
        :param key:str
        :return:str,the value corresponding to the key
        >>> camelize_map = CamelCaseMap()
        >>> camelize_map['first_name'] = 'John'
        >>> camelize_map.__getitem__('first_name')
        'John'
        """


    def __setitem__(self, key, value):
        """
        Set the value corresponding to the key to the specified value
        :param key:str
        :param value:str, the specified value
        :return:None
        >>> camelize_map = CamelCaseMap()
        >>> camelize_map['first_name'] = 'John'
        >>> camelize_map.__setitem__('first_name', 'new name')
        camelize_map['first_name'] = 'new name'
        """


    def __delitem__(self, key):
        """
        Delete the value corresponding to the key
        :param key:str
        :return:None
        >>> camelize_map = CamelCaseMap()
        >>> camelize_map['first_name'] = 'John'
        >>> camelize_map.__delitem__('first_name')
        >>> flag = 'first_name' in camelize_map
        flag = False
        """


    def __iter__(self):
        """
        Returning Iterateable Objects with Own Data
        :return:Iterator
        >>> camelize_map = CamelCaseMap()
        >>> camelize_map['first_name'] = 'John'
        >>> camelize_map['last_name'] = 'Doe'
        >>> camelize_map['age'] = 30
        >>> camelize_map.__iter__()
        <dict_keyiterator object at 0x0000026739977C20>
        """


    def __len__(self):
        """
        Returns the length of the own data
        :return:int, length of data
        >>> camelize_map = CamelCaseMap()
        >>> camelize_map['first_name'] = 'John'
        >>> camelize_map['last_name'] = 'Doe'
        >>> camelize_map['age'] = 30
        >>> camelize_map.__len__()
        3
        """

    def _convert_key(self, key):
        """
        convert key string into camel case
        :param key:str
        :return:str, converted key string
        >>> camelize_map = CamelCaseMap()
        >>> camelize_map._convert_key('first_name')
        'firstName'
        """

    @staticmethod
    def _to_camel_case(key):
        """
        convert key string into camel case
        :param key:str
        :return:str, converted key string
        >>> camelize_map = CamelCaseMap()
        >>> camelize_map._to_camel_case('first_name')
        'firstName'
        """
```

## Method `__getitem__`

### Docstring

```python
def __getitem__(self, key):
        """
        Return the value corresponding to the key
        :param key:str
        :return:str,the value corresponding to the key
        >>> camelize_map = CamelCaseMap()
        >>> camelize_map['first_name'] = 'John'
        >>> camelize_map.__getitem__('first_name')
        'John'
        """
```

### Reference code (`solution_code`)

```python
def __getitem__(self, key):
        return self._data[self._convert_key(key)]
```

### Tests (`CamelCaseMapTestGetitem`)

**test_getitem_1**: `stated`
- reason: The docstring's own example stores 'John' under 'first_name' and retrieves it with `__getitem__('first_name')`, which is exactly what this test checks, so a programmer following it would pass.

```python
def test_getitem_1(self):
    camelize_map = CamelCaseMap()
    camelize_map['first_name'] = 'John'
    self.assertEqual(camelize_map.__getitem__('first_name'), 'John')
```

**test_getitem_2**: `stated`
- reason: The docstring says `__getitem__` returns the value stored under the key, and this test only sets a key and reads it back, which a programmer following that description would pass.

```python
def test_getitem_2(self):
    camelize_map = CamelCaseMap()
    camelize_map['last_name'] = 'Doe'
    self.assertEqual(camelize_map.__getitem__('last_name'), 'Doe')
```

**test_getitem_3**: `stated`
- reason: The docstring says the method returns the value stored under the key, and a programmer following that would return the stored 30 for the key 'age', which is what the test checks.

```python
def test_getitem_3(self):
    camelize_map = CamelCaseMap()
    camelize_map['age'] = 30
    self.assertEqual(camelize_map.__getitem__('age'), 30)
```

**test_getitem_4**: `unstated`
- reason: The docstring only says the method returns the value for the key, so a programmer would do a plain lookup, which fails when the test reads back 'first_Name' after storing 'first_name' and expects 'John'.
- missing: The docstring should say that keys are normalized before lookup (for example, converted to camelCase form), so that any key spelling that normalizes to the same form returns the same stored value.

```python
def test_getitem_4(self):
    camelize_map = CamelCaseMap()
    camelize_map['first_name'] = 'John'
    self.assertEqual(camelize_map.__getitem__('first_Name'), 'John')
```

**test_getitem_5**: `unstated`
- reason: The docstring only says the method returns the value for a key, so a programmer would look up the exact key, while the test expects a lookup under a differently formatted key to find the value stored under another format.
- missing: The docstring should state that keys are normalized (converted to the class's canonical key format) both when storing and when looking up, so that any key spelled in a different convention that normalizes to the same form returns the stored value.

```python
def test_getitem_5(self):
    camelize_map = CamelCaseMap()
    camelize_map['first_name'] = 'John'
    self.assertEqual(camelize_map.__getitem__('firstName'), 'John')
```

## Method `__setitem__`

### Docstring

```python
def __setitem__(self, key, value):
        """
        Set the value corresponding to the key to the specified value
        :param key:str
        :param value:str, the specified value
        :return:None
        >>> camelize_map = CamelCaseMap()
        >>> camelize_map['first_name'] = 'John'
        >>> camelize_map.__setitem__('first_name', 'new name')
        camelize_map['first_name'] = 'new name'
        """
```

### Reference code (`solution_code`)

```python
def __setitem__(self, key, value):
        self._data[self._convert_key(key)] = value
```

### Tests (`CamelCaseMapTestSetitem`)

**test_setitem_1**: `stated`
- reason: The docstring says `__setitem__` sets the value for a key to the specified value, and the test checks exactly that: after overwriting 'first_name' with 'newname', the lookup returns 'newname'.

```python
def test_setitem_1(self):
    camelize_map = CamelCaseMap()
    camelize_map['first_name'] = 'John'
    camelize_map.__setitem__('first_name', 'newname')
    self.assertEqual(camelize_map['first_name'], 'newname')
```

**test_setitem_2**: `stated`
- reason: The docstring says __setitem__ sets the value for the key, and the test only sets a key and reads it back under the same key, which a programmer following the docstring would pass.

```python
def test_setitem_2(self):
    camelize_map = CamelCaseMap()
    camelize_map['first_name'] = 'John'
    camelize_map.__setitem__('first_name', 'John')
    self.assertEqual(camelize_map['first_name'], 'John')
```

**test_setitem_3**: `unstated`
- reason: The test expects `'first_Name'` and `'first_name'` to address the same stored entry, which requires the key to be normalised by the class's camel-case conversion, but the docstring only says it sets "the value corresponding to the key" and never mentions this conversion.
- missing: The docstring should state that every key is converted to its camel-case form before storage, so any two keys that normalise to the same camel-case name refer to the same entry, and a later assignment overwrites the earlier one.

```python
def test_setitem_3(self):
    camelize_map = CamelCaseMap()
    camelize_map['first_name'] = 'John'
    camelize_map.__setitem__('first_Name', 'newname')
    self.assertEqual(camelize_map['first_name'], 'newname')
```

**test_setitem_4**: `unstated`
- reason: The docstring says only that the value is set for the key, so a programmer would store 'firstName' as a separate entry, but the test expects it to update 'first_name' because the class normalizes keys.
- missing: The docstring should say that keys are normalized (for example, camelCase keys are converted to snake_case) before storing, so that differently-spelled keys that map to the same normalized name refer to the same entry.

```python
def test_setitem_4(self):
    camelize_map = CamelCaseMap()
    camelize_map['first_name'] = 'John'
    camelize_map.__setitem__('firstName', 'newname')
    self.assertEqual(camelize_map['first_name'], 'newname')
```

**test_setitem_5**: `stated`
- reason: The docstring says `__setitem__` sets the value for the key to the specified value (a `str`), so a programmer would store an empty string and read it back unchanged, which is what the test checks.

```python
def test_setitem_5(self):
    camelize_map = CamelCaseMap()
    camelize_map['first_name'] = 'John'
    camelize_map.__setitem__('first_name', '')
    self.assertEqual(camelize_map['first_name'], '')
```

## Method `__delitem__`

### Docstring

```python
def __delitem__(self, key):
        """
        Delete the value corresponding to the key
        :param key:str
        :return:None
        >>> camelize_map = CamelCaseMap()
        >>> camelize_map['first_name'] = 'John'
        >>> camelize_map.__delitem__('first_name')
        >>> flag = 'first_name' in camelize_map
        flag = False
        """
```

### Reference code (`solution_code`)

```python
def __delitem__(self, key):
        del self._data[self._convert_key(key)]
```

### Tests (`CamelCaseMapTestDelitem`)

**test_delitem_1**: `stated`
- reason: The docstring says deleting a key removes its value, and a programmer following it would only remove that one entry, so the other key still maps to 'Doe' and the test passes.

```python
def test_delitem_1(self):
    camelize_map = CamelCaseMap()
    camelize_map['first_name'] = 'John'
    camelize_map['last_name'] = 'Doe'
    camelize_map.__delitem__('first_name')
    self.assertEqual(camelize_map['last_name'], 'Doe')
```

**test_delitem_2**: `stated`
- reason: The docstring's example deletes `'first_name'` and then shows that `'first_name' in camelize_map` is False, which is exactly what the test checks, so a programmer following it would pass.

```python
def test_delitem_2(self):
    camelize_map = CamelCaseMap()
    camelize_map['first_name'] = 'John'
    camelize_map.__delitem__('first_name')
    self.assertEqual('first_name' in camelize_map, False)
```

**test_delitem_3**: `unstated`
- reason: The docstring only shows deleting an exact key, but the test expects a differently cased key to delete the stored entry, which only works if keys are normalized before lookup, and the docstring does not say so.
- missing: The docstring should state that keys are normalized by the same conversion used on assignment and lookup, so that deleting any key variant that normalizes to the same form removes the stored entry.

```python
def test_delitem_3(self):
    camelize_map = CamelCaseMap()
    camelize_map['first_name'] = 'John'
    camelize_map.__delitem__('first_Name')
    self.assertEqual('first_name' in camelize_map, False)
```

**test_delitem_4**: `unstated`
- reason: The docstring says only "Delete the value corresponding to the key," so a programmer would look up the key as given, and the test expects `'firstName'` to delete the entry stored under `'first_name'`, which that plain lookup would not do.
- missing: The docstring should say that keys are normalized to the map's canonical form before lookup, so any key spelling that maps to the same canonical name (for example camelCase versus snake_case) refers to the same entry for deletion.

```python
def test_delitem_4(self):
    camelize_map = CamelCaseMap()
    camelize_map['first_name'] = 'John'
    camelize_map.__delitem__('firstName')
    self.assertEqual('first_name' in camelize_map, False)
```

**test_delitem_5**: `stated`
- reason: The docstring says `__delitem__` deletes the value for the key, and its example shows the key is no longer `in` the map afterward, which is exactly what the test checks even though it uses an empty-string value.

```python
def test_delitem_5(self):
    camelize_map = CamelCaseMap()
    camelize_map['first_name'] = ''
    camelize_map.__delitem__('first_name')
    self.assertEqual('first_name' in camelize_map, False)
```

## Method `__iter__`

### Docstring

```python
def __iter__(self):
        """
        Returning Iterateable Objects with Own Data
        :return:Iterator
        >>> camelize_map = CamelCaseMap()
        >>> camelize_map['first_name'] = 'John'
        >>> camelize_map['last_name'] = 'Doe'
        >>> camelize_map['age'] = 30
        >>> camelize_map.__iter__()
        <dict_keyiterator object at 0x0000026739977C20>
        """
```

### Reference code (`solution_code`)

```python
def __iter__(self):
        return iter(self._data)
```

### Tests (`CamelCaseMapTestIter`)

**test_iter_1**: `unstated`
- reason: The docstring only says the method returns an iterator over the object's own data and shows an opaque iterator repr, so it never says the yielded keys are transformed, while the test expects keys in a converted form.
- missing: The docstring should state that keys are stored and yielded in the transformed (converted) form applied when they were assigned, not in the original spelling the caller used.

```python
def test_iter_1(self):
    camelize_map = CamelCaseMap()
    camelize_map['first_name'] = 'John'
    camelize_map['last_name'] = 'Doe'
    camelize_map['age'] = 30
    lst = ['firstName', 'lastName', 'age']
    iter = camelize_map.__iter__()
    i = 0
    for key in iter:
        self.assertEqual(key, lst[i])
        i += 1
```

**test_iter_2**: `stated`
- reason: The docstring says the method returns an iterator and its example shows a `dict_keyiterator`, so a programmer would naturally return an iterator over the stored keys in dict order, which is the insertion order this test checks.

```python
def test_iter_2(self):
    camelize_map = CamelCaseMap()
    camelize_map['firstname'] = 'John'
    camelize_map['lastname'] = 'Doe'
    camelize_map['age'] = 30
    lst = ['firstname', 'lastname', 'age']
    iter = camelize_map.__iter__()
    i = 0
    for key in iter:
        self.assertEqual(key, lst[i])
        i += 1
```

**test_iter_3**: `unstated`
- reason: The docstring never says that keys are transformed when stored, so a programmer following it would iterate over the keys as given and fail the test, which expects the converted camelCase keys.
- missing: The docstring should state that keys are converted to camelCase when they are assigned, so that iteration yields the converted keys rather than the originals.

```python
def test_iter_3(self):
    camelize_map = CamelCaseMap()
    camelize_map['first_Name'] = 'John'
    camelize_map['last_Name'] = 'Doe'
    camelize_map['age'] = 30
    lst = ['firstName', 'lastName', 'age']
    iter = camelize_map.__iter__()
    i = 0
    for key in iter:
        self.assertEqual(key, lst[i])
        i += 1
```

**test_iter_4**: `unstated`
- reason: The docstring only says `__iter__` returns an iterator over the object's data, but the test expects keys in camelCase form (`first_Name` comes back as `firstName`), a conversion the docstring never mentions.
- missing: The docstring should say that keys are stored and returned in the converted form, e.g. underscore-separated words are joined and capitalised after the first, so iteration yields the converted keys rather than the raw keys as originally assigned.

```python
def test_iter_4(self):
    camelize_map = CamelCaseMap()
    camelize_map['first_Name'] = 'John'
    camelize_map['last_Name'] = 'Doe'
    lst = ['firstName', 'lastName']
    iter = camelize_map.__iter__()
    i = 0
    for key in iter:
        self.assertEqual(key, lst[i])
        i += 1
```

**test_iter_5**: `unstated`
- reason: The test expects iteration to yield the camelCased key 'firstName' for an input key 'first_Name', but the docstring only says it returns an iterator and never mentions that keys are converted on assignment, so a faithful implementation of the docstring could yield the raw key.
- missing: The docstring should state that keys are converted to camelCase when they are stored (underscore-separated segments are merged and each following segment's first letter is capitalized), so that iterating yields the converted keys rather than the originals.

```python
def test_iter_5(self):
    camelize_map = CamelCaseMap()
    camelize_map['first_Name'] = 'John'
    lst = ['firstName']
    iter = camelize_map.__iter__()
    i = 0
    for key in iter:
        self.assertEqual(key, lst[i])
        i += 1
```

## Method `__len__`

### Docstring

```python
def __len__(self):
        """
        Returns the length of the own data
        :return:int, length of data
        >>> camelize_map = CamelCaseMap()
        >>> camelize_map['first_name'] = 'John'
        >>> camelize_map['last_name'] = 'Doe'
        >>> camelize_map['age'] = 30
        >>> camelize_map.__len__()
        3
        """
```

### Reference code (`solution_code`)

```python
def __len__(self):
        return len(self._data)
```

### Tests (`CamelCaseMapTestLen`)

**test_len_1**: `stated`
- reason: The docstring says __len__ returns the length of the stored data, so a programmer would return the count of stored items, which gives 1 after setting one key and matches the test's expected value.

```python
def test_len_1(self):
    camelize_map = CamelCaseMap()
    camelize_map['first_name'] = 'John'
    self.assertEqual(camelize_map.__len__(), 1)
```

**test_len_2**: `stated`
- reason: The docstring says `__len__` returns the length of the stored data, so a programmer would return the number of keys in the internal store, which gives 1 after one assignment, as the test expects.

```python
def test_len_2(self):
    camelize_map = CamelCaseMap()
    camelize_map['last_name'] = 'Doe'
    self.assertEqual(camelize_map.__len__(), 1)
```

**test_len_3**: `stated`
- reason: The docstring says `__len__` returns the length of the stored data, so a programmer would return the count of stored items, which is 1 after one assignment, matching the test.

```python
def test_len_3(self):
    camelize_map = CamelCaseMap()
    camelize_map['age'] = 30
    self.assertEqual(camelize_map.__len__(), 1)
```

**test_len_4**: `stated`
- reason: The docstring says `__len__` returns the length of the stored data, and the test inserts three distinct keys and expects 3, which is what a programmer following the docstring would return.

```python
def test_len_4(self):
    camelize_map = CamelCaseMap()
    camelize_map['first_name'] = 'John'
    camelize_map['last_Name'] = 'Doe'
    camelize_map['age'] = 30
    self.assertEqual(camelize_map.__len__(), 3)
```

**test_len_5**: `stated`
- reason: The docstring says `__len__` returns the length of the stored data, so a fresh empty map should report 0, which is exactly what the test checks.

```python
def test_len_5(self):
    camelize_map = CamelCaseMap()
    self.assertEqual(camelize_map.__len__(), 0)
```

## Method `_convert_key`

### Docstring

```python
def _convert_key(self, key):
        """
        convert key string into camel case
        :param key:str
        :return:str, converted key string
        >>> camelize_map = CamelCaseMap()
        >>> camelize_map._convert_key('first_name')
        'firstName'
        """
```

### Reference code (`solution_code`)

```python
def _convert_key(self, key):
        if isinstance(key, str):
            return self._to_camel_case(key)
        return key
```

### Tests (`CamelCaseMapTestConvertKey`)

**test_convert_key_1**: `stated`
- reason: The docstring says the method converts a key string to camel case, and its example ('first_name' to 'firstName') shows the same snake_case-to-camelCase rule the test checks ('aaa_bbb' to 'aaaBbb').

```python
def test_convert_key_1(self):
    camelize_map = CamelCaseMap()
    self.assertEqual(camelize_map._convert_key('aaa_bbb'), 'aaaBbb')
```

**test_convert_key_2**: `stated`
- reason: The docstring's own example converts 'first_name' to 'firstName', which is exactly the input and expected output the test checks, so a programmer following it would pass.

```python
def test_convert_key_2(self):
    camelize_map = CamelCaseMap()
    self.assertEqual(camelize_map._convert_key('first_name'), 'firstName')
```

**test_convert_key_3**: `stated`
- reason: The docstring says to convert a key string to camel case and gives the snake_case-to-camelCase example 'first_name' to 'firstName', which is the same rule the test applies to 'last_name' expecting 'lastName'.

```python
def test_convert_key_3(self):
    camelize_map = CamelCaseMap()
    self.assertEqual(camelize_map._convert_key('last_name'), 'lastName')
```

**test_convert_key_4**: `stated`
- reason: The docstring says to convert a key string into camel case with an example ('first_name' to 'firstName'), so a programmer would produce 'cccDdd' from 'ccc_ddd' by capitalising the segment after each underscore.

```python
def test_convert_key_4(self):
    camelize_map = CamelCaseMap()
    self.assertEqual(camelize_map._convert_key('ccc_ddd'), 'cccDdd')
```

**test_convert_key_5**: `stated`
- reason: The docstring says the method converts a key string to camel case and gives the `first_name` to `firstName` example, so a programmer would produce `eeeFff` for `eee_fff`.

```python
def test_convert_key_5(self):
    camelize_map = CamelCaseMap()
    self.assertEqual(camelize_map._convert_key('eee_fff'), 'eeeFff')
```

**test_convert_key_6**: `unstated`
- reason: The docstring only describes string keys and says nothing about non-string input, so a programmer could reasonably raise an error, convert the value to a string, or return it unchanged, and only the last matches the test.
- missing: The docstring should say that any key that is not a string is returned exactly as given, without conversion or error.

```python
def test_convert_key_6(self):
    camelize_map = CamelCaseMap()
    self.assertEqual(camelize_map._convert_key(1234), 1234)
```

## Method `_to_camel_case`

### Docstring

```python
@staticmethod
    def _to_camel_case(key):
        """
        convert key string into camel case
        :param key:str
        :return:str, converted key string
        >>> camelize_map = CamelCaseMap()
        >>> camelize_map._to_camel_case('first_name')
        'firstName'
        """
```

### Reference code (`solution_code`)

```python
@staticmethod
    def _to_camel_case(key):
        parts = key.split('_')
        return parts[0] + ''.join(part.title() for part in parts[1:])
```

### Tests (`CamelCaseMapTestToCamelCase`)

**test_to_camel_case_1**: `stated`
- reason: The docstring says to convert a key string to camel case with an example (`first_name` to `firstName`), so a programmer would split on underscores, capitalise the following parts and keep the first part as is, which gives `aaaBbb` for `aaa_bbb`.

```python
def test_to_camel_case_1(self):
    self.assertEqual(CamelCaseMap._to_camel_case('aaa_bbb'), 'aaaBbb')
```

**test_to_camel_case_2**: `stated`
- reason: The docstring says to convert a key string into camel case and gives the example 'first_name' -> 'firstName', which is exactly what this test checks, so a programmer following it would pass.

```python
def test_to_camel_case_2(self):
    self.assertEqual(CamelCaseMap._to_camel_case('first_name'), 'firstName')
```

**test_to_camel_case_3**: `stated`
- reason: The docstring says to convert a key string into camel case with an underscore-separated example (`first_name` to `firstName`), so a programmer would split on underscores and capitalise the following parts, which yields `lastName` for this test.

```python
def test_to_camel_case_3(self):
    self.assertEqual(CamelCaseMap._to_camel_case('last_name'), 'lastName')
```

**test_to_camel_case_4**: `stated`
- reason: The docstring says to convert a snake_case key into camel case, and its example ('first_name' to 'firstName') shows the same pattern the test checks ('ccc_ddd' to 'cccDdd'), so a programmer following it would produce the expected output.

```python
def test_to_camel_case_4(self):
    self.assertEqual(CamelCaseMap._to_camel_case('ccc_ddd'), 'cccDdd')
```

**test_to_camel_case_5**: `stated`
- reason: The docstring says to convert a key string to camel case with the example `first_name` to `firstName`, so a programmer would produce `eeeFff` for `eee_fff`, matching the test.

```python
def test_to_camel_case_5(self):
    self.assertEqual(CamelCaseMap._to_camel_case('eee_fff'), 'eeeFff')
```

## Tests in no method's test class

### `CamelCaseMapTest`

**test_CamelCaseMap**: `no_method_info`
- reason: its test class is in no methods_info[i]['test_class']

```python
def test_CamelCaseMap(self):
    camelize_map = CamelCaseMap()
    camelize_map['first_name'] = 'John'
    self.assertEqual(camelize_map.__getitem__('first_name'), 'John')

    camelize_map = CamelCaseMap()
    camelize_map['first_name'] = 'John'
    camelize_map.__setitem__('first_name', 'newname')
    self.assertEqual(camelize_map['first_name'], 'newname')
```
