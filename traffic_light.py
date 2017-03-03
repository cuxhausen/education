"""
списал
"""
from datetime import datetime
print("Green" if (datetime.now().minute%5) < 3 else "Red")
