# Create a function called get_llm_names(tools).
#
# It should:
# 1. Create an empty list called names.
# 2. Loop through the tools.
# 3. Check if the tool's type is "LLM".
# 4. If it is, add its name to names.
# 5. Return names.
#
# Expected result:
# ["ChatGPT", "Gemini"]

def get_llm_names(tools):
    names= []
    for x in tools :
      if x["type"] == "LLM":
        names.append(x["name"])
    return names

