import pandas as pd

# Define the path to your pickle file
pickle_file_path = 'nunez-mujica-ramachandran-morris-world-bank-climate-data (1).pickle 2'

try:
    # Use pandas to load the pickle file
    data = pd.read_pickle(pickle_file_path)

    # Print the extracted data
    print("Data extracted from pickle file:")
    print(data)

except FileNotFoundError:
    print(f"Error: The file '{pickle_file_path}' was not found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")


#save data in excel file

data.to_excel('data.xlsx', index=False)
print("Data saved to 'data.xlsx' file.")
