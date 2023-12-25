import re, os
from pathlib import Path
import argparse
from argparse import RawDescriptionHelpFormatter

def get_first_camelcase_word(camelcase_str):
    pattern = r'^[a-z]+'
    match = re.match(pattern, camelcase_str)

    if match:
        first_word = match.group()
        return first_word
    
def sort_list_by_given_order(list_to_sort, order):
    return sorted(list_to_sort, key=lambda x: (get_first_camelcase_word(x) not in order, order.index(get_first_camelcase_word(x)) if get_first_camelcase_word(x) in order else float('inf')))

def find_file(base_path, filename):
    for path in Path(base_path).rglob('*.js'):
        if filename in path.name:
            return path

def main():    
    description = """
    Script to sort javascript class methods.
    Example usage:
    $ python sort-js-class-methods.py LinearPlanPage.js descending --actions_order get click intercept wait
    Here we are sorting the LinearPlanPage.js class methods in descending order
    Structure:
    $ python <path where saved script>/sort-js-class-methods.py <Page Object to sort> <order> --actions_order <keyword1> <keyword2> ...
    """
    parser = argparse.ArgumentParser(description=description, formatter_class=RawDescriptionHelpFormatter)
    parser.add_argument('file_to_sort', help="Receives the filename to be sorted (has to be a javascript class)")
    parser.add_argument('order', choices=("descending, ascending"), default="descending", help="If you want to sort it alphabetically descending or ascending")
    parser.add_argument('--actions_order', nargs='+', help="The order that you want the methods to be ordered")
    args = parser.parse_args()

    print(args.actions_order)

    root_path = f"{os.getcwd()}/src/cypress/ui/cypress/pageObjects"
    file_path = find_file(root_path, args.file_to_sort)

    with open(file_path, "r") as file:
        data = file.read()

    class_sliced_into_groups = re.search("([\s\S]+)(export default class \w+ extends \w+ {)([\s\S]+)(})", data)

    imports = class_sliced_into_groups.group(1)
    class_definition = class_sliced_into_groups.group(2)
    class_methods = class_sliced_into_groups.group(3)
    class_closing_bracket = class_sliced_into_groups.group(4)

    # in line comments turned into block comments 
    class_methods = re.sub(r"\/\/(.*)$", "/*\\g<1> */", class_methods, 0, re.MULTILINE)
    # replaced double jump line by ||||
    class_methods = re.sub(r"^\s{4}(\w+\()", "||||\\g<1>", class_methods, 0, re.MULTILINE) 

    class_methods = class_methods.split("||||")

    # removed jump line to turn the function into a single line function
    class_methods = [x.replace("\n", "") for x in class_methods]

    is_sorted_descending = True if args.order == "descending" else False 
    class_methods.sort(reverse=is_sorted_descending)
    class_methods_sorted_by_given_order = sort_list_by_given_order(class_methods, args.actions_order)

    with open(file_path, "w") as file:
        file.write(imports+class_definition+"\n\n".join(class_methods_sorted_by_given_order)+"\n"+class_closing_bracket)

if __name__ == "__main__":
    main()
