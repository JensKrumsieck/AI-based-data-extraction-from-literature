#!/usr/bin/env cwl-runner

cwlVersion: v1.2
class: Workflow

requirements:
- class: SubworkflowFeatureRequirement

inputs:
- id: icasa_template
  type: File

outputs:
- id: manual_tabular
  type: Directory
  outputSource: json_to_xlsx/output_directory

steps:
- id: json_to_xlsx
  in:
  - id: input_folder
    source: generate_icasa_json/icasa_json_outputs
  run: ../json_to_xlsx/json_to_xlsx.cwl
  out:
  - output_directory
- id: generate_icasa_json
  in:
  - id: template_path
    source: icasa_template
  run: ../generate_icasa_json/generate_icasa_json.cwl
  out:
  - icasa_json_outputs
