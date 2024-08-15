from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.http import JsonResponse
import re

# Global variable to store the current input as a list of strings
my_list = []

def index(request):
    """
    Renders the index page.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: The rendered HTML page for the index view.
    """
    return render(request, 'index.html')

def button(request, pk):
    """
    Handles the button clicks and updates the input field.

    Args:
        request: The HTTP request object.
        pk: The value associated with the button clicked (can be a number or special key).

    Returns:
        HttpResponse: The updated HTML for the input field.
    """
    global my_list

    if request.method == "POST":
        # Convert pk to string to ensure consistent type handling
        pk = str(pk)

        if pk == '123':
            # If pk is '123', treat it as a decimal point '.'
            pk = '.'
            # Join the current list to form the complete input string
            input_str = "".join(my_list)
            
            # Split the input string by operators to get the individual number parts
            parts = re.split(r'([+\-*/])', input_str)
            
            # Ensure the decimal point is only added if not already present in the current number
            if parts and not re.search(r'[+\-*/]$', input_str):
                last_part = parts[-1]  # The last segment (current number)
                if '.' not in last_part:
                    my_list.append(pk)
        else:
            # Append the button value to the list
            my_list.append(pk)

        # Join the list to form the complete input string
        inputField = "".join(my_list)

        # Generate the HTML for the updated input field
        html = f"""
        <input type="text" id="inputField" 
            class="w-full h-12 text-right p-2 mb-4 text-xl border border-gray-300 rounded" 
            value="{inputField}" disabled>
        """

        return HttpResponse(html)

def string_button(request, my_string):
    """
    Handles the string button clicks and updates the input field.

    Args:
        request: The HTTP request object.
        my_string: The value associated with the button clicked (can be an operator or special string).

    Returns:
        HttpResponse: The updated HTML for the input field.
    """
    global my_list

    if request.method == 'POST':

        # Convert special strings to corresponding operators if necessary
        if my_string == "divide":
            my_string = "/"

        # Append the string value to the list
        my_list.append(my_string)

        # Join the list to form the complete input string
        inputField = "".join(my_list)

        # Generate the HTML for the updated input field
        html = f"""
        <input type="text" id="inputField" 
            class="w-full h-12 text-right p-2 mb-4 text-xl border border-gray-300 rounded" 
            value="{inputField}" disabled>
        """

        return HttpResponse(html)

def delete_button(request):
    """
    Clears the input field.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: The updated HTML for the cleared input field.
    """
    global my_list

    if request.method == 'POST':
        # Clear the global list
        my_list.clear()
        
        # Generate the HTML for the cleared input field
        inputField = "".join(my_list)
        html = f"""
        <input type="text" id="inputField" 
            class="w-full h-12 text-right p-2 mb-4 text-xl border border-gray-300 rounded" 
            value="{inputField}" disabled>
        """
        return HttpResponse(html)

def solve(request):
    """
    Evaluates the expression and returns the result.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: The updated HTML for the input field with the solution.
    """
    global my_list

    if request.method == "POST":
        # Evaluate the expression formed by joining the list items
        solution = eval("".join(my_list))

        # Clear the global list and store the result
        my_list.clear()
        my_list.append(str(solution))

        # Generate the HTML for the input field displaying the solution
        html = f"""
        <input type="text" id="inputField" 
            class="w-full h-12 text-right p-2 mb-4 text-xl border border-gray-300 rounded" 
            value="{solution}" disabled>
        """
        return HttpResponse(html)
