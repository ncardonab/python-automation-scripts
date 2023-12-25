import re, os

project_path = f"{os.getcwd()}/src/cypress/ui/cypress/e2e/"
filename_to_save = "tests_descriptions.md"
file_to_write = open("tests_descriptions.md", "w")

for path, subdirs, files in os.walk(project_path):
    for filename in files:
        file_path = os.path.join(path, filename)

        with open(file_path, "r") as file:
            test_str = file.read()

        substitution = " "
        regex = r"\\\n\s+"
        tests_descriptions_withtout_backslashes = re.sub(regex, substitution, test_str, 100, re.MULTILINE)

        its_descriptions = [ description for _, description in re.findall("it\((\n\s+)?'(.+)'", tests_descriptions_withtout_backslashes) ]
        # ?:describe\((?:\n\s+)?'(.+)'(?:[\s\S]+?)\b|)(

        file_to_write.write("<details>")
        file_to_write.write(f"<summary>{filename}</summary>\n\n")

        for description in its_descriptions:
            file_to_write.write(f"- [ ] { description } \n")

        file_to_write.write("</details>")

file_to_write.close()