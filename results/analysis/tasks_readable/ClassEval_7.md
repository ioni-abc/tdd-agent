# ClassEval_7

## Skeleton (what the agent sees)

```python
class BalancedBrackets:
    """
    This is a class that checks for bracket matching
    """

    def __init__(self, expr):
        """
        Initializes the class with an expression.
        :param expr: The expression to check for balanced brackets,str.
        """
        self.stack = []
        self.left_brackets = ["(", "{", "["]
        self.right_brackets = [")", "}", "]"]
        self.expr = expr

    def clear_expr(self):
        """
        Clears the expression of all characters that are not brackets.
        >>> b = BalancedBrackets("a(b)c")
        >>> b.clear_expr()
        >>> b.expr
        '()'

        """

    def check_balanced_brackets(self):
        """
        Checks if the expression has balanced brackets.
        :return: True if the expression has balanced brackets, False otherwise.
        >>> b = BalancedBrackets("a(b)c")
        >>> b.check_balanced_brackets()
        True

        """
```

## Method `clear_expr`

### Docstring

```python
def clear_expr(self):
        """
        Clears the expression of all characters that are not brackets.
        >>> b = BalancedBrackets("a(b)c")
        >>> b.clear_expr()
        >>> b.expr
        '()'

        """
```

### Reference code (`solution_code`)

```python
def clear_expr(self):
        self.expr = ''.join(c for c in self.expr if (c in self.left_brackets or c in self.right_brackets))
```

### Tests (`BalancedBracketsTestClearExpr`)

**test_clear_expr**: `stated`
- reason: The docstring says the method removes all non-bracket characters and gives the example "a(b)c" becoming '()', which is exactly what the test checks.

```python
def test_clear_expr(self):
    b = BalancedBrackets("a(b)c")
    b.clear_expr()
    self.assertEqual(b.expr, "()")
```

**test_clear_expr_2**: `stated`
- reason: The docstring says clear_expr removes every character that is not a bracket and keeps the brackets in order, so a programmer following it would produce "(){}" for "a(b){c}".

```python
def test_clear_expr_2(self):
    b = BalancedBrackets("a(b){c}")
    b.clear_expr()
    self.assertEqual(b.expr, "(){}")
```

**test_clear_expr_3**: `stated`
- reason: The docstring says to remove every character that is not a bracket, so a programmer would keep `[`, `]`, `(`, `)`, `{`, `}` and drop the letters, which yields the expected `"[](){}"`.

```python
def test_clear_expr_3(self):
    b = BalancedBrackets("[a](b){c}")
    b.clear_expr()
    self.assertEqual(b.expr, "[](){}")
```

**test_clear_expr_4**: `stated`
- reason: The docstring says all non-bracket characters are cleared, so a programmer would keep every bracket character (including `[` and `{`) and remove the letters, which gives the expected `"[(){}"`.

```python
def test_clear_expr_4(self):
    b = BalancedBrackets("[a(b){c}")
    b.clear_expr()
    self.assertEqual(b.expr, "[(){}")
```

**test_clear_expr_5**: `stated`
- reason: The docstring says all non-bracket characters are cleared, so a programmer would keep every bracket, including the unmatched `]`, which yields the expected `"(){}]"`.

```python
def test_clear_expr_5(self):
    b = BalancedBrackets("a(b){c}]")
    b.clear_expr()
    self.assertEqual(b.expr, "(){}]")
```

## Method `check_balanced_brackets`

### Docstring

```python
def check_balanced_brackets(self):
        """
        Checks if the expression has balanced brackets.
        :return: True if the expression has balanced brackets, False otherwise.
        >>> b = BalancedBrackets("a(b)c")
        >>> b.check_balanced_brackets()
        True

        """
```

### Reference code (`solution_code`)

```python
def check_balanced_brackets(self):
        self.clear_expr()
        for Brkt in self.expr:
            if Brkt in self.left_brackets:
                self.stack.append(Brkt)
            else:
                Current_Brkt = self.stack.pop()
                if Current_Brkt == "(":
                    if Brkt != ")":
                        return False
                if Current_Brkt == "{":
                    if Brkt != "}":
                        return False
                if Current_Brkt == "[":
                    if Brkt != "]":
                        return False
        if self.stack:
            return False
        return True
```

### Tests (`BalancedBracketsTestCheckBalancedBrackets`)

**test_check_balanced_brackets**: `stated`
- reason: The docstring says the method returns True when the expression has balanced brackets, and its example shows exactly this input returning True, so a standard bracket-matching implementation passes the test.

```python
def test_check_balanced_brackets(self):
    b = BalancedBrackets("a(b)c")
    self.assertEqual(b.check_balanced_brackets(), True)
```

**test_check_balanced_brackets_2**: `stated`
- reason: The docstring says the method returns True when the expression has balanced brackets, and a programmer implementing a standard stack check would return True for "a(b){c}", which is balanced.

```python
def test_check_balanced_brackets_2(self):
    b = BalancedBrackets("a(b){c}")
    self.assertEqual(b.check_balanced_brackets(), True)
```

**test_check_balanced_brackets_3**: `stated`
- reason: The docstring says the method returns True when the expression has balanced brackets, and a standard stack-based check on "[a](b){c}" (sequential, properly nested pairs with letters in between) gives True, so a programmer following it would pass.

```python
def test_check_balanced_brackets_3(self):
    b = BalancedBrackets("[a](b){c}")
    self.assertEqual(b.check_balanced_brackets(), True)
```

**test_check_balanced_brackets_4**: `stated`
- reason: The docstring says the method returns False whenever the expression does not have balanced brackets, and an unclosed "[" makes it unbalanced, so a programmer following the docstring would return False.

```python
def test_check_balanced_brackets_4(self):
    b = BalancedBrackets("[a(b){c}")
    self.assertEqual(b.check_balanced_brackets(), False)
```

**test_check_balanced_brackets_5**: `stated`
- reason: The docstring says the method returns False whenever the brackets are not balanced, and a mismatched closing bracket like the test's "]" against an open "(" makes the brackets unbalanced, so a standard stack-based check returns False as the test expects.

```python
def test_check_balanced_brackets_5(self):
    b = BalancedBrackets("a(b{c}]")
    self.assertEqual(b.check_balanced_brackets(), False)
```

**test_check_balanced_brackets_6**: `stated`
- reason: The docstring says the method returns False whenever the expression does not have balanced brackets, and this input has an unclosed "(" and a "{" closed by "]", so a standard stack-matching implementation returns False.

```python
def test_check_balanced_brackets_6(self):
    b = BalancedBrackets("a(b{c]]")
    self.assertEqual(b.check_balanced_brackets(), False)
```

**test_check_balanced_brackets_7**: `stated`
- reason: The docstring says the method returns False when brackets are not balanced, and the test's expression has an opening "[" closed by ")", so a programmer following the docstring would return False.

```python
def test_check_balanced_brackets_7(self):
    b = BalancedBrackets("[a)(b){c}")
    self.assertEqual(b.check_balanced_brackets(), False)
```

## Tests in no method's test class

### `BalancedBracketsTestMain`

**test_main**: `no_method_info`
- reason: its test class is in no methods_info[i]['test_class']

```python
def test_main(self):
    b = BalancedBrackets("a(b)c")
    b.clear_expr()
    self.assertEqual(b.expr, "()")
    self.assertEqual(b.check_balanced_brackets(), True)
```

**test_main_2**: `no_method_info`
- reason: its test class is in no methods_info[i]['test_class']

```python
def test_main_2(self):
    b = BalancedBrackets("[a(b){c}")
    b.clear_expr()
    self.assertEqual(b.expr, "[(){}")
    self.assertEqual(b.check_balanced_brackets(), False)
```

**test_main_3**: `no_method_info`
- reason: its test class is in no methods_info[i]['test_class']

```python
def test_main_3(self):
    b = BalancedBrackets("a(b{c}]")
    b.clear_expr()
    self.assertEqual(b.expr, "({}]")
    self.assertEqual(b.check_balanced_brackets(), False)
```
