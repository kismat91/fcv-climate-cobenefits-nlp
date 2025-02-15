import pandas as pd


# Load the dataset
def load_dataset():
    url = "hf://datasets/lukesjordan/worldbank-project-documents/wb_project_documents.jsonl.gz"
    df = pd.read_json(url, lines=True, compression="gzip")
    return df


# Function to get project details by project_id
def get_project_details(df, project_id):
    # Filter the dataframe for the given project_id
    project_details = df[df["project_id"] == project_id]
    print(project_details.columns)
    return project_details


# Main function
if __name__ == "__main__":
    # Load the dataset
    df = load_dataset()

    # Ask the user to input a project_id
    project_id = input("Enter the project_id: ")

    # Get and print the project details
    project_details = get_project_details(df, project_id)

    if not project_details.empty:
        print(f"Details for project_id '{project_id}':")
        print(project_details)
    else:
        print(f"No project found with project_id '{project_id}'.")