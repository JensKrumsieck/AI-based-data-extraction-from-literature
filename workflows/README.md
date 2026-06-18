# Workflows
This folder contains multiple CWL (Common Workflow Language) Descriptions of the given R- and Python-Scripts. CWL is used to wrap Steps into `CommandLineTool`s which are combined to multiple Workflows. However one step `fine_tune_model` requires manual work. This is representated by an abstract description of type `Operation` making all workflows that contain this step non-executable.

Some of the Workflows contained herein and described herafter are for the validation of data to circumvent the problem of the manual `fine_tune_model` step and also the `llm_extract_icasa` step which needs an API key to use the fine-tuned models on OpenAI Platform. The Results of the combination of those steps in `tune_and_use_llm_model` are stored in this repository at `/data/07_llm_output_json`.
The `marker` step which converts PDFs to markdown is also not used in most of the executable steps as the PDFs are not part of this repository due to copyright limitations. Its output is located at `data/01_paper_to_md`.

## Generate Manual Tabular Data
`generate_manual_data` contains a workflow which extracts the manual data from the ICASA Template into JSON which is than converted into a tabular format, more specifically XLSX. Its purpose is to generate the manual ground truth data which later is compared to the LLM generated data.

### Usage:
```
cwltool workflows/generate_manual_data/workflow.cwl inputs_generate_manual_data.yaml
```

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
`generate_training_data` contains a workflow which processes the extracted markdownfiles and generates training data in JSONL format by also using data from the ICASA template. This JSONL files need to be manually uploaded to OpenAIs Platform. That's why this workflow contains all needed steps up to this point and exits here. 
The `marker` step is left out on purpose on this workflow due to copyright limitations.

### Usage:
```
cwltool workflows/generate_training_data/workflow.cwl inputs_generate_training_data.yaml
```

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

The `marker` step can be used together with `generate_training_data` as subworkflow by using `workflows/generate_training_data_using_marker/workflow.cwl` which gives the opportunity to use this pipeline with different PDF files.
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
    pdf_directory(pdf_directory)
    icasa_template(icasa_template)
    training_data_dirname(training_data_dirname)
  end
  subgraph outputs[Workflow Outputs]
    direction TB
    training_data(training_data)
  end
    marker(marker)
  pdf_directory --> |pdf_directory|marker
    marker_output_dir_name(paper_to_md)
  marker_output_dir_name --> |output_dir_name|marker
    workflow(workflow)
  marker --> |markdown_papers|workflow
  icasa_template --> |icasa_template|workflow
  training_data_dirname --> |training_data_dirname|workflow
  workflow --> |training_data|training_data
  style inputs fill:#EEEEEE,stroke-width:2px;
  style pdf_directory stroke:#0f9884,fill:#6FC1B5,stroke-width:2px;
  style icasa_template stroke:#0f9884,fill:#6FC1B5,stroke-width:2px;
  style training_data_dirname stroke:#0f9884,fill:#6FC1B5,stroke-width:2px;
  style outputs fill:#EEEEEE,stroke-width:2px;
  style training_data stroke:#823909,fill:#F8CBAD,stroke-width:2px;
  style marker stroke:#385723,stroke-width:2px;
  style marker_output_dir_name font-size:9px,fill:#cfeae6, stroke:#9FD6CE,stroke-width:2px;
  style workflow stroke:#385723,stroke-width:2px;
```