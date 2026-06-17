#!/usr/bin/env cwl-runner

cwlVersion: v1.2
class: CommandLineTool

requirements:
- class: InitialWorkDirRequirement
  listing:
  - entryname: R/create_training_data.R
    entry:
      $include: ../../R/create_training_data.R
  - entryname: R/icasa_attributes_config.R
    entry: $(inputs.r_icasa_attributes_config_r)
- class: DockerRequirement
  dockerFile:
    $include: ../../Dockerfile.renv
  dockerImageId: renv-container

inputs:
- id: markdown_folder
  type: Directory
  default:
    class: Directory
    location: ../../data/02_final_processed_md
  inputBinding:
    prefix: --markdown_folder
- id: json_folder
  type: Directory
  default:
    class: Directory
    location: ../../data/04_manual_json
  inputBinding:
    prefix: --json_folder
- id: output_directory
  type: string
  default: test
  inputBinding:
    prefix: --output_directory
- id: r_icasa_attributes_config_r
  type: File
  default:
    class: File
    location: ../../R/icasa_attributes_config.R

outputs:
- id: test
  type: Directory
  outputBinding:
    glob: test/

baseCommand:
- Rscript
- R/create_training_data.R
