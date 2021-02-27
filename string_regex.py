import re

print(bool(re.match('[A-Za-z0-9]+$','abcd123')))
# bool(re.match(‘[A-Za-z0-9]+$','abcd@123’)) #return False

"""
True
"""