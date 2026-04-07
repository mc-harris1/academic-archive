from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
CONVERTED_DATA_DIR = DATA_DIR / "converted"


def available_datasets():
    return sorted(path.stem for path in RAW_DATA_DIR.glob("*.txt"))


def dataset_paths(dataset_name):
    input_path = RAW_DATA_DIR / (dataset_name + ".txt")
    output_path = CONVERTED_DATA_DIR / (dataset_name + ".arff")
    return input_path, output_path


def make_header(file_name, attribute_type, label_type, num_attributes):
    header = "@RELATION " + file_name + "\n\n"
    letters = list("ZYXWVUTSRQPONMLKJIHGFEDCBA")

    if attribute_type == "I":
        attribute_value_type = "INTEGER"
    elif attribute_type == "R":
        attribute_value_type = "REAL"
    else:
        attribute_value_type = "{" + ",".join(attribute_type) + "}"

    for _ in range(num_attributes - 1):
        header += "@ATTRIBUTE " + letters.pop(0) + " " + attribute_value_type + "\n"

    label_value_type = " {" + ",".join(label_type) + "}"
    header += "@ATTRIBUTE class" + label_value_type
    return header


def determine_attribute():
    attribute_kind = (
        input(
            "What data type are the attributes? "
            "Enter C for categorical, I for integer, and R for Real. "
        )
        .strip()
        .upper()
    )
    if attribute_kind in {"I", "R"}:
        return attribute_kind

    categories = []
    category_count = int(input("Enter the number of categories: ").strip())
    for index in range(category_count):
        categories.append(input("Enter category #" + str(index + 1) + ": ").strip())
    return categories


def determine_class():
    label_first = input("Is the label at first column (yes or no)? ").strip().lower() == "yes"
    class_count = int(input("How many classes are there? ").strip())
    classes = []
    for index in range(class_count):
        classes.append(input("Enter class #" + str(index + 1) + ": ").strip())

    return label_first, classes


def normalize_rows(lines, delimiter, label_first):
    normalized_rows = []
    for line in lines:
        stripped_line = line.strip()
        if not stripped_line:
            continue

        values = [value.strip() for value in stripped_line.split(delimiter)]
        if label_first:
            values = values[1:] + values[:1]
        normalized_rows.append(",".join(values))

    return normalized_rows


def convert_dataset(dataset_name, attribute_type, label_first, classes, delimiter):
    input_path, output_path = dataset_paths(dataset_name)

    if not input_path.exists():
        available = ", ".join(available_datasets())
        raise FileNotFoundError(
            "Dataset not found in data/raw: "
            + str(input_path)
            + (". Available datasets: " + available if available else "")
        )

    with input_path.open("r", encoding="utf-8") as input_file:
        lines = input_file.readlines()

    if not lines:
        raise ValueError("Dataset file is empty: " + str(input_path))

    attribute_count = len(lines[0].strip().split(delimiter)) - 1
    data_rows = normalize_rows(lines, delimiter, label_first)
    header = make_header(dataset_name + ".txt", attribute_type, classes, attribute_count + 1)

    CONVERTED_DATA_DIR.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as output_file:
        output_file.write(header)
        output_file.write("\n\n@DATA\n")
        output_file.write("\n".join(data_rows))
        output_file.write("\n")

    print("Read", input_path.name, "from", input_path.parent)
    print("Wrote", output_path.name, "to", output_path.parent)


def main():
    datasets = available_datasets()
    dataset_prompt = "Enter the dataset name you'd like to convert (without the extension): "
    if datasets:
        dataset_prompt = dataset_prompt + "[available: " + ", ".join(datasets) + "] "

    dataset_name = input(dataset_prompt).strip()
    attribute_type = determine_attribute()
    label_first, classes = determine_class()
    delimiter = input("What delimiter separates this data? ").strip()
    convert_dataset(dataset_name, attribute_type, label_first, classes, delimiter)


if __name__ == "__main__":
    main()
