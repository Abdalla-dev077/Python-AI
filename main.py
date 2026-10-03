# Import the ai_tools list from data.py
# Import the get_llm_names function from tools.py
# Use the function with ai_tools
# Print the result

from data import Ai_tools
from tools import get_llm_names

names = get_llm_names(Ai_tools)
print(names)