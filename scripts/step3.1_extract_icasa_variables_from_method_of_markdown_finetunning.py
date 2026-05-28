# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 13:54:53 2025

@author: xinxin
"""

import os
import re
import requests
import pandas as pd
from io import BytesIO
import openai


# put your own api
openai.api_key = os.getenv('api')
client = openai.OpenAI()


# Function to read markdown files
def read_markdown_file(md_file_path):
    try:
        with open(md_file_path, "r", encoding="utf-8") as file:
            return file.read()
    except Exception as e:
        print(f"Error reading markdown file {md_file_path}: {e}")
        return ""


# Function to save extracted content to a file
def save_to_file(file_path, content):
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
    except Exception as e:
        print(f"Error saving content to {file_path}: {e}")

# Function to send a message to OpenAI and process the response
def send_message(messages, new_message):
    messages.append({"role": "user", "content": new_message})
    try:
        response = client.chat.completions.create(
        #put your fine tuned model, replace this model here is the example for experiment metadata
        model="ft:gpt-4.1-mini-2025-04-14:personal:exp-v040526:DbkEyIz7",
         messages=messages,
            temperature=0 
        )
        assistant_message = response.choices[0].message.content
        messages.append({"role": "assistant", "content": assistant_message})
        return assistant_message, messages
    except Exception as e:
        print(f"Error communicating with OpenAI API: {e}")
        return "", messages



# Function to process markdown and extract ICASA variables
def process_markdown_and_extract_icasa(md_file_path, specific_columns, output_path, category):
    markdown_content = read_markdown_file(md_file_path)
    del md_file_path
    if not markdown_content:
        return

    content = markdown_content
   
    del markdown_content
    
    system_message = {"role": "system", "content": "You are an expert in agriculture."}
    messages = [system_message]

    combined_dict = {row['Code_Display']: (row['Description'], row['Unit_or_type']) for _, row in specific_columns.iterrows()}


    del specific_columns
   
    if category == "fertilizers" :
           user_message = (
             f"Understanding and extract the ICASA fertiliz_app_name,fertilization_date,fertilizer_material,application_depth_fert,fertilizer_total_amount,N_in_applied_fertilizer,phosphorus_applied_fert,fertilizer_K_applied, fertilizer_applic_notes, et al variables from this content: {content}"
           )
    elif category == "irrigation":
           user_message = (
             f"Extract icasa irrigation applied events variables from {content}")

    elif category == "plantings":
           user_message = (
             f"Understanding and extract the ICASA planting_level_name, planting_date, transplant_date, emergence_date, plant_pop_at_planting, plant_pop_at_emergence, planting_material, planting_distribution, plant_spacing, row_spacing, planting_depth, planting_material_weight, planting_method, planting_notes et al variables from this content:{content}" )
         
    elif category == "genotypes":
             user_message = (
               f"Understanding and extract the ICASA experiment_ID, crop_ident_ICASA,cultivar_name,crop_intended_use,cultivar_notes et al variables from this content: {content}" )

            
    elif category == "harvests":
           user_message = (
             f"extract the ICASA Harvest events variables from this content {content}" )
        
    elif category == "obs_summary_pa1"  or category == "obs_summary_pa2":
           user_message = (
             f"Extract all values for each variable in'{combined_dict}' from:{content},do not use table format or fake example data")
       
    elif category == "SOIL_PROFILES":
            user_message = (
             f"must extract all detailed values for each variable in '{combined_dict}'from {content} with different layers" )
       
    # elif category == "soil_plot_details":
    #         user_message = (
             
    #          f"Extract all values for each variable in'{combined_dict}' from data:{content},do not use table format or fake example data" )
     
    # # elif category == "weather_metadata":
    #         user_message = (
    #          f"Extract all values for variable '{combined_dict}' from data:{content},consider different month have different values.do not use table format or false data "   )
       
    # elif category == "weather_daily":
    #         user_message = (
             
    #          f"Extract all values for variable '{combined_dict}' from data:{content},do not use table format")
         
            
    elif category == "plot_details" :
            user_message = (         
             f"Extract all values for variable '{combined_dict}' from data:{content},do not use table format or fake example data")      
          
    elif  category == "fields":
            user_message = (         
             #f"Extract all values for variable '{combined_dict}' from data:{content},do not use table format or fake example data")      
          f"Understanding and extract the ICASA field_name, field_id,field_country,field_sub_country,field_sub_sub_country, field_latitude, field_longitude, field_elevation, field_soil_texture et al variables from this content:{content}")      
              
    elif  category == "exp_metadata":
            user_message = (         
             #f"Extract all values for variable '{combined_dict}' from data:{content},do not use table format or fake example data")      
          f"Understanding and extract the ICASA experiment_ID,name_of_experiment,experiment_type,management_type,number_of_replicates,number_of_treatments,experimental_design,main_experiment_factor,experimental_factor_comb,experiment_duration variables from this content:{content}")      
              
            
    else:
            user_message = (
              f"Extract all values for variable '{combined_dict}' from data:{content},do not use table format or fake example data"
        )
    try:
            response, messages = send_message(messages, user_message)         
            del messages
            save_to_file(output_path, response)  # Save as one file          
            del response
            system_message = {"role": "system", "content": f"You are an expert in agriculture."}
            messages = [system_message]
    except Exception as e:
            print(f"Error processing ICASA variable : {e}")

 

    del content
    del user_message
    del category
    del messages     
    del combined_dict        
  
  

# Function to process all markdown files in a folder
def process_all_markdown_files(folder_path, specific_columns, output_folder):
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".md") or file_name.endswith(".MD"):
            md_file_path = os.path.join(folder_path, file_name)
            output_path = os.path.join(output_folder, f"{os.path.splitext(file_name)[0]}.txt")
            print(f"Processing file: {md_file_path}")
            process_markdown_and_extract_icasa(md_file_path, specific_columns, output_path)

def fetch_icasa_variables(category):
    url = "https://raw.githubusercontent.com/DSSAT/ICASA-Dictionary/refs/heads/main/XLSX/ICASA_Data_Dictionary.xlsx"

    response = requests.get(url)

    if response.status_code == 200:
        excel_data = BytesIO(response.content)
        del response
        # Determine the correct sheet name based on the category

        if category == "plantings" or category == "genotypes"  or category == "fields" :
            sheet_name = "Management_info"                 
                      
        elif category == "fertilizers":
            sheet_name = "Management_info"              
                        
        elif category == "irrigation":
            sheet_name = "Management_info"

        elif category == "obs_summary_pa1" or category == "obs_summary_pa2":
            sheet_name = "Measured_data"
            
            
        elif category == "SOIL_PROFILES":
            sheet_name = "Soils_data"
            

        elif category == "plot_details":
            sheet_name = "Metadata" 
            
        elif category == "harvests":
            sheet_name = "Management_info" 
    
        elif category == "exp_metadata":
            sheet_name = "Metadata"    
            
        # elif category == "weather_daily":
        #     sheet_name = "Weather_data"           
        # elif category == "weather_metadata":
        #     sheet_name = "Weather_data"           


            
        else:
            sheet_name = "xx"

        df = pd.read_excel(excel_data, sheet_name=sheet_name, engine="openpyxl")
        del excel_data
        del sheet_name
       
        if category == "plantings":
            variables_of_interest = ["planting_level_name","planting_date", "transplant_date", "emergence_date","plant_pop_at_planting",
                                     "plant_pop_at_emergence","planting_material","plant_spacing","row_spacing", "planting_depth", "planting_material", "planting_method","planting_notes"
                                     ]
            specific_rows = df[df["Variable_Name"].isin(variables_of_interest)]
     
        elif category == "harvests":
            variables_of_interest = ["harvest_ops_level_name","harvest_operations_date", "harvest_notes"
                                     ]
            specific_rows = df[df["Variable_Name"].isin(variables_of_interest)]
     
        
     
        elif category == "genotypes":
            variables_of_interest = ["crop_id", "genotype_name","genotype_notes","crop_ident_ICASA","crop_intended_use" ]
            specific_rows = df[df["Variable_Name"].isin(variables_of_interest)]
     


        elif category == "fertilizers":
            variables_of_interest = ["fertilizer_level_name", "fert_#_tot",  "fert_applics_tot", "fertilizer_season", "fertilizer_notes",
                                     "fertiliz_app_name", "planting_year", "planting_date","fertilization_date", "fertilizer_material", "fertilizer_applic_method",
                                     "application_depth_fert","fertilizer_total_amount",
                                     "phosphorus_applied_fert", "fertilizer_K_applied"
                                       ]
            specific_rows = df[df["Variable_Name"].isin(variables_of_interest)]


    
        elif category == "irrigation":
            variables_of_interest = [  "irrigation_level_name","irrig_applied", "irrigation_applics_season", "irrigation_season","irrigation_notes",
             "irrigation_operation_name", "planting_year","planting_date","irrigation_date","irrigation_operation","irrig_amount_depth", "irrigation_applic_depth",  "irrigation_H2O_N_conc",
              "irrigation_operation_notes" ]
            specific_rows = df[df["Variable_Name"].isin(variables_of_interest)]

      
        elif category == "obs_summary_pa1":
            specific_rows = pd.concat([df.iloc[[8]], df.iloc[[10]],df.iloc[[14]],  df.iloc[[16]], df.iloc[[17]],df.iloc[[32]], df.iloc[[35]]])
        
        
        elif category == "obs_summary_pa2":                               
            specific_rows = pd.concat([ df.iloc[[64]] ,  df.iloc[[90]] , df.iloc[[98]] , df.iloc[[300]]]) # Single row 50   


        elif category == "SOIL_PROFILES":     
           
            variables_of_interest = [ "soil_layer_top_depth", "soil_layer_base_depth",
      "soil_clay_fraction","soil_silt_fraction","soil_sand_fraction","soil_coarse_fraction",
      "soil_organic_C_perc_layr",  "soil_pH_in_water", "soil_bulk_density_moist","soil_water_lower_limit",
      "soil_water_wilting_pt","soil_water_field_cap_1", "soil_water_field_cap_2", "soil_wat_drned_upper_lim","soil_water_saturated", "sat_hydraul_conductivity",
     "soil_organic_matter_layer"]
            specific_rows = df[df["Variable_Name"].isin(variables_of_interest)]
       
             #"soil_classific_system", "soil_albedo","soil_N_total_conc",  "soil_organic_N_conc",
             
        elif category == "plot_details":     
         variables_of_interest = ["plot_length","plot_width","plot_area","plot_harvest_area","plot_layout" ]
         specific_rows = df[df["Variable_Name"].isin(variables_of_interest)]
  
        elif category == "exp_metadata":     
         variables_of_interest = ["experiment_duration" ]
         specific_rows = df[df["Variable_Name"].isin(variables_of_interest)]
 




        elif category == "fields":     
         variables_of_interest = [ "field_name","field_country", "field_sub_country","field_sub_sub_country", "field_latitude",
      "field_longitude","field_elevation","wsta_distance","field_notes"]
         specific_rows = df[df["Variable_Name"].isin(variables_of_interest)]
      

                          
             
        # elif category == "weather_daily":     
        #      specific_rows = pd.concat([df.iloc[85:97]])     
        # elif category == "weather_metadata":     
        #      specific_rows = pd.concat([df.iloc[32:45], df.iloc[47:53] ])    
   
        else:
            raise ValueError(f"Unknown: {category}")

        
        return specific_rows[['Code_Display', 'Description', 'Unit_or_type']]
        del df

    else:
        raise Exception(f"Failed to fetch")

        
def process_all_markdown_files(category, markdown_folder, output_folder):
    specific_columns = fetch_icasa_variables(category)

    # for file_name in os.listdir(markdown_folder):
    #     if file_name.endswith(".md") or file_name.endswith(".MD"):
    #         markdown_file_path = os.path.join(markdown_folder, file_name)
    #         output_path = os.path.join(output_folder, f"{os.path.splitext(file_name)[0]}_{category}_output.txt")

    #         print(f"Processing file: {markdown_file_path} for category: {category}")
    #         # Ensure category is passed correctly
    #         process_markdown_and_extract_icasa(markdown_file_path, specific_columns, output_path, category)
    for root, _, files in os.walk(markdown_folder):
        for file_name in files:
            if file_name.lower().endswith(".md"):
               markdown_file_path = os.path.join(root, file_name)

               # Maintain the same subfolder structure in the output
               relative_path = os.path.relpath(root, markdown_folder)
               sub_output_folder = os.path.join(output_folder, relative_path)
               os.makedirs(sub_output_folder, exist_ok=True)

               output_path = os.path.join(sub_output_folder, f"{os.path.splitext(file_name)[0]}_{category}.txt")

               print(f"Processing file: {markdown_file_path} for category: {category}")
               process_markdown_and_extract_icasa(markdown_file_path, specific_columns, output_path, category)

def main():
    categories = ["exp_metadata"]#  "plantings","harvests","fields","irrigation","plot_details",,"fertilizers"

    markdown_folder = 'C:/Users/xinxin/OneDrive - Leibniz-Zentrum für Agrarlandschaftsforschung (ZALF) e.V/Desktop/FAIRagro_fine_tunning/data/0_training_set_version2/0_tokenized_pdfs_tables_and_methods_combined_titleauthor_addyear'
    base_output_folder = 'C:/Users/xinxin/OneDrive - Leibniz-Zentrum für Agrarlandschaftsforschung (ZALF) e.V/Desktop/FAIRagro_fine_tunning/data/0_training_set_version2/genotype_gpt-4.1-mini_finetuning_output_v040526_exp_metadata_v97'

    for category in categories:
        output_folder = os.path.join(base_output_folder)
        os.makedirs(output_folder, exist_ok=True)
        # Pass category explicitly
        process_all_markdown_files(category, markdown_folder, output_folder)

if __name__ == "__main__":
     main()
    
    

