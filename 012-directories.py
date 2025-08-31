# @Author: Farhad Yusifov
# @Email: farhadyusifov@protonmail.com
# @Date: 2025-08-30

# @Description: Working with directories in Python.

from pathlib import Path


# path = Path("tools")
# path.mkdir()
# print(path.exists())
# path.rmdir()


path = Path()
for file in path.glob("*"):
    print(path)
