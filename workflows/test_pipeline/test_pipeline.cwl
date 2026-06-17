#!/usr/bin/env cwl-runner

cwlVersion: v1.2
class: Workflow

requirements:
- class: SubworkflowFeatureRequirement

inputs:
- id: icasa_template
  type: File
- id: markdown_folder
  type: Directory

outputs:
- id: manual_tabular
  type: Directory
  outputSource: json_to_xlsx/output_directory
- id: trainingdaata
  type: Directory
  outputSource: assemble_training_set/training_data

steps:
- id: process_paper
  in:
  - id: input_folder
    source: markdown_folder
  run: ../process_paper/process_paper.cwl
  out:
  - output_directory
- id: assemble_training_set
  in:
  - id: markdown_folder
    source: process_paper/output_directory
  - id: template_path
    source: icasa_template
  run: ../assemble_training_set/assemble_training_set.cwl
  out:
  - json_data
  - training_data
- id: json_to_xlsx
  in:
  - id: input_folder
    source: assemble_training_set/json_data
  run: ../json_to_xlsx/json_to_xlsx.cwl
  out:
  - output_directory
