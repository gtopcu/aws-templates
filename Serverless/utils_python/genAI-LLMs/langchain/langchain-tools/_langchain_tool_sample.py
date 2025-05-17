
# pip install langchain-tools
from langchain_tools import tool

class CalculatorTools:

    @tool("Make a calculator")
    def calculator(operation):
        """
        Useful to perform any mathematical calculation
        like sum, minus, multiplication, division etc.
        The input to this tool should be a mathematical
        expression, like 20*2 or 3/3+10
        """
        try:
            return eval(operation)
        except SyntaxError:
            return "Error, invalid syntax in the operation"