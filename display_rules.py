def display_rules(file_path):
    try:
        with open(file_path, 'r') as file:
            rules = file.readlines()
            for rule in rules:
                print(rule.strip())
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    file_path = "rules.txt"
    display_rules(file_path)
