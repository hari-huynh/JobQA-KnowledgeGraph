import yaml

if __name__ == "__main__":
    with open("prompts/cypher_examples.yaml", "r") as file:
        examples = yaml.safe_load(file)

    print(examples)

