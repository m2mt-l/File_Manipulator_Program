# File Manipulator Program

## Reverse

```bash
❯ cat test.txt
This is a test.
❯ python file_manipulator.py --reverse test.txt reverse.txt
❯ cat reverse.txt

.tset a si sihT
```

## Copy

```bash
❯ cat test.txt
This is a test.
❯ python file_manipulator.py --copy test.txt copy.txt
❯ cat copy.txt
This is a test.
```

## Duplicate Contents

```bash
❯ cat test.txt
This is a test.
❯ python file_manipulator.py --duplicate-contents test.txt 5
❯ cat test.txt
This is a test.
This is a test.
This is a test.
This is a test.
This is a test.
```

## Replace String

```bash
❯ cat test.txt
This is a test.
This is a test.
This is a test.
This is a test.
This is a test.
❯ python file_manipulator.py --replace-string test.txt test cat
❯ cat test.txt
This is a cat.
This is a cat.
This is a cat.
This is a cat.
This is a cat.
```
