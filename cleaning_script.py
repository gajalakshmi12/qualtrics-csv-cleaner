import pandas as pd
import requests
import os
from tkinter import Tk, filedialog, messagebox

def clean_minimal_and_download(input_csv, output_folder="output"):
    # Load CSV and remove metadata rows
    raw_df = pd.read_csv(input_csv)
    cleaned_df = raw_df.iloc[2:].reset_index(drop=True)

    # Rename columns for clarity
    cleaned_df = cleaned_df.rename(columns={
        "Q1": "Assessment Type",
        "Q2": "Program Name",
        "Q3": "Program College",
        "Q4": "Department",
        "Q5": "Submitter Name",
        "Q6": "Section",
        "Q6_Name": "Program Doc Name",     
        "Q6_Url": "Program Doc URL",
        "Q7_Name": "DDC Doc Name",         
        "Q7_Url": "DDC Doc URL",
        "Q2.1": "DDC College",
        "Q3.1": "Category",
        "Q4.1": "Course Number",
        "Q5.1": "Instructor Name",
        "EndDate": "Date Submitted"
    })

    # Separate rows by assessment type
    program_df = cleaned_df[cleaned_df["Assessment Type"] == "Program Assessment"]
    ddc_df = cleaned_df[cleaned_df["Assessment Type"] == "DDC Assessment"]

    # Keep required columns
    program_filtered = program_df[[
        "Date Submitted", "Program Name", "Program College", "Department", "Submitter Name",
        "Program Doc Name", "Program Doc URL"
    ]]
    ddc_filtered = ddc_df[[
        "Date Submitted", "DDC College", "Category", "Course Number", "Instructor Name", "Section",
        "DDC Doc Name", "DDC Doc URL"
    ]]

    # Create output folders
    program_dir = os.path.join(output_folder, "downloads", "program")
    ddc_dir = os.path.join(output_folder, "downloads", "ddc")
    os.makedirs(program_dir, exist_ok=True)
    os.makedirs(ddc_dir, exist_ok=True)

    # Save Excel with both sheets
    excel_path = os.path.join(output_folder, "assessment_cleaned.xlsx")
    with pd.ExcelWriter(excel_path) as writer:
        program_filtered.to_excel(writer, sheet_name="Program Assessment", index=False)
        ddc_filtered.to_excel(writer, sheet_name="DDC Assessment", index=False)

    # Download Program files
    for _, row in program_filtered.iterrows():
        file_name, file_url = row["Program Doc Name"], row["Program Doc URL"]
        if pd.notna(file_name) and pd.notna(file_url):
            try:
                response = requests.get(file_url)
                with open(os.path.join(program_dir, file_name), "wb") as f:
                    f.write(response.content)
            except Exception as e:
                print(f"Failed to download Program file {file_name}: {e}")

    # Download DDC files
    for _, row in ddc_filtered.iterrows():
        file_name, file_url = row["DDC Doc Name"], row["DDC Doc URL"]
        if pd.notna(file_name) and pd.notna(file_url):
            try:
                response = requests.get(file_url)
                with open(os.path.join(ddc_dir, file_name), "wb") as f:
                    f.write(response.content)
            except Exception as e:                
                messagebox.showerror("Download Failed", f"Failed to download file {file_name}:\n{e}")
   
    messagebox.showinfo(
    "Success",
    f"Processing complete!\n\nExcel saved to:\n{excel_path}\n\nProgram files: {program_dir}\nDDC files: {ddc_dir}"
    )


# Run file picker
if __name__ == "__main__":
    root = Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(
        title="Select Assessment CSV File",
        filetypes=[("CSV Files", "*.csv")]
    )
    if file_path:
        clean_minimal_and_download(file_path)





