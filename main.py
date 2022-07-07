import pandas as pd
import sys
csv_file_input = sys.argv[1]
json_file = csv_file_input[:-4] + ".json"
print(f"This is the json output: {json_file}")

# Create pandas dataframe with csv file
csv_file = pd.DataFrame(pd.read_csv(csv_file_input, sep=",", header=0, index_col=False))

# Output the dataframe for testing
print(csv_file)

# Convert the dataframe to a json file
csv_file.to_json(json_file, orient="records", date_format="epoch", double_precision=10, force_ascii=False,
                 date_unit="ms", default_handler=None)
