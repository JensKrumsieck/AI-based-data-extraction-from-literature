# Workflows
This folder contains multiple CWL (Common Workflow Language) Descriptions of the given R- and Python-Scripts. CWL is used to wrap Steps into `CommandLineTool`s which are combined to multiple Workflows. However one step `fine_tune_model` requires manual work. This is representated by an abstract description of type `Operation` making all workflows that contain this step non-executable.

## Generate Manual Tabular Data
`generate_manual_data` contains a workflow which extracts the manual data from the ICASA Template into JSON which is than converted into a tabular format, more specifically XLSX.

```mermaid
---
config:
  theme: base
  look: neo
  themeVariables:
    primaryColor: '#C5E0B4'
    primaryTextColor: '#231f20'
    secondaryColor: '#EEEEEE'
    lineColor: '#385723'    
    fontSize: 12px
    tertiaryTextColor: '#231f20'
    fontFamily: 'Fira Sans, trebuchet ms, verdana, arial'
---
flowchart TB
  linkStyle default stroke:#385723,stroke-width: 2px;
  subgraph inputs[Workflow Inputs]
    direction TB
    icasa_template(icasa_template)
    xlsx_dirname(xlsx_dirname)
  end
  subgraph outputs[Workflow Outputs]
    direction TB
    manual_json(manual_json)
  end
    json_to_xlsx(json_to_xlsx)
  generate_icasa_json --> |input_folder|json_to_xlsx
  xlsx_dirname --> |output_folder|json_to_xlsx
    generate_icasa_json(generate_icasa_json)
  icasa_template --> |template_path|generate_icasa_json
    generate_icasa_json_json_folder_name(manual_json)
  generate_icasa_json_json_folder_name --> |json_folder_name|generate_icasa_json
    generate_icasa_json_icasa_attributes(../../R/icasa_attributes_config.R)
  generate_icasa_json_icasa_attributes --> |icasa_attributes|generate_icasa_json
  json_to_xlsx --> |manual_json|manual_json
  style inputs fill:#EEEEEE,stroke-width:2px;
  style icasa_template stroke:#0f9884,fill:#6FC1B5,stroke-width:2px;
  style xlsx_dirname stroke:#0f9884,fill:#6FC1B5,stroke-width:2px;
  style outputs fill:#EEEEEE,stroke-width:2px;
  style manual_json stroke:#823909,fill:#F8CBAD,stroke-width:2px;
  style json_to_xlsx stroke:#385723,stroke-width:2px;
  style generate_icasa_json stroke:#385723,stroke-width:2px;
  style generate_icasa_json_json_folder_name font-size:9px,fill:#cfeae6, stroke:#9FD6CE,stroke-width:2px;
  style generate_icasa_json_icasa_attributes font-size:9px,fill:#cfeae6, stroke:#9FD6CE,stroke-width:2px;
```

## Generate Training Data
`generate_training_data` contains a workflow which processes the extracted markdownfiles and generates training data in JSONL format by also using data from the ICASA template.

```mermaid
---
config:
  theme: base
  look: neo
  themeVariables:
    primaryColor: '#C5E0B4'
    primaryTextColor: '#231f20'
    secondaryColor: '#EEEEEE'
    lineColor: '#385723'    
    fontSize: 12px
    tertiaryTextColor: '#231f20'
    fontFamily: 'Fira Sans, trebuchet ms, verdana, arial'
---
flowchart TB
  linkStyle default stroke:#385723,stroke-width: 2px;
  subgraph inputs[Workflow Inputs]
    direction TB
    markdown_papers(markdown_papers)
    icasa_template(icasa_template)
    training_data_dirname(training_data_dirname)
  end
  subgraph outputs[Workflow Outputs]
    direction TB
    training_data(training_data)
  end
    create_training_data(create_training_data)
  process_paper --> |markdown_folder|create_training_data
  generate_icasa_json --> |json_folder|create_training_data
  training_data_dirname --> |output_directory_name|create_training_data
    create_training_data_icasa_attributes(../../R/icasa_attributes_config.R)
  create_training_data_icasa_attributes --> |icasa_attributes|create_training_data
    process_paper(process_paper)
  markdown_papers --> |input_folder|process_paper
    process_paper_output_folder(data/02_final_processed_md)
  process_paper_output_folder --> |output_folder|process_paper
    generate_icasa_json(generate_icasa_json)
  icasa_template --> |template_path|generate_icasa_json
    generate_icasa_json_json_folder_name(manual_json)
  generate_icasa_json_json_folder_name --> |json_folder_name|generate_icasa_json
    generate_icasa_json_icasa_attributes(../../R/icasa_attributes_config.R)
  generate_icasa_json_icasa_attributes --> |icasa_attributes|generate_icasa_json
  create_training_data --> |training_data|training_data
  style inputs fill:#EEEEEE,stroke-width:2px;
  style markdown_papers stroke:#0f9884,fill:#6FC1B5,stroke-width:2px;
  style icasa_template stroke:#0f9884,fill:#6FC1B5,stroke-width:2px;
  style training_data_dirname stroke:#0f9884,fill:#6FC1B5,stroke-width:2px;
  style outputs fill:#EEEEEE,stroke-width:2px;
  style training_data stroke:#823909,fill:#F8CBAD,stroke-width:2px;
  style create_training_data stroke:#385723,stroke-width:2px;
  style create_training_data_icasa_attributes font-size:9px,fill:#cfeae6, stroke:#9FD6CE,stroke-width:2px;
  style process_paper stroke:#385723,stroke-width:2px;
  style process_paper_output_folder font-size:9px,fill:#cfeae6, stroke:#9FD6CE,stroke-width:2px;
  style generate_icasa_json stroke:#385723,stroke-width:2px;
  style generate_icasa_json_json_folder_name font-size:9px,fill:#cfeae6, stroke:#9FD6CE,stroke-width:2px;
  style generate_icasa_json_icasa_attributes font-size:9px,fill:#cfeae6, stroke:#9FD6CE,stroke-width:2px;
```