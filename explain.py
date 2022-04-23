"""
This modue is intended to assist with clarifying any data or variables that are present in the notebook.

It consists of a function that returns information based on key/value pairs. The key is the variable name, 
and the value is the explanation of that variable. This is not a comprehensive dictionary of all variables, 
but will return the primary variables.

The indicator before the variable explanation (i.e. "DF -->") refers to the type of object that is referenced.

To use the function, just call explain.what_is() with no parameters.
"""

def what_is():
    """ Takes no parameters. Accepts user input and prints a response. """
    
    df_information = {
        'grouped_tables': """
DF -->  The variable ['grouped_tables'] references a dataframe consisting of
             all possible variables in the 4 datasets available in the ABS datahold.
             
             It is useful for determining which variables are in each dataset.
             """,
        'possible_merge_options': """
DF -->  The variable ['possible_merge_options'] references a dataframe consisting of
             a smaller subset of the grouped_tables dataframe. It's purpose is to assist
             with determining which variables are common in all tables.
             """
    }
    user_query = input('Blank Input returns all information.\nWhich dataframe are you asking about? (partial and complete matches returned) >> ')
    requested_vars = []
    for key in df_information:
        if user_query.lower() in key.lower():
            requested_vars.append(df_information[key])
    if len(requested_vars) == 0:
        print(f'No matches found.\nSome of the possibilities are {", ".join(_ for _ in df_information.keys)} ')
    else:
        if len(requested_vars) > 1:
            print('\nMultiple Matches Found')
        return_string = "\n" + "\n".join(requested_vars)
        print(f'{return_string}')