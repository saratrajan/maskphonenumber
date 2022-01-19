# Summary

This quick utility takes the root folder of desired path as input and then scans through all files to check if phone numbers are present and then replaces the numbers (masks them) with asterisks.

e.g. 123-000-1234 is replaced (masked) with `***-***-****`

## Input

Currently target root folder is set as `files/` and it has two files within as below:

```shell
├── files
│   ├── data.txt
│   └── sample.txt
```

## Output

It replaces identified phone numbers with asterisks at the end of execution.

## Execution

Clone the repo and change directory to root of repo before running `python main.py`
