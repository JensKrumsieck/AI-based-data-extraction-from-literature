#!/usr/bin/env cwl-runner

cwlVersion: v1.2
class: CommandLineTool

requirements:
- class: InitialWorkDirRequirement
  listing:
  - entryname: R/assemble_training_set.R
    entry:
      $include: ../../R/assemble_training_set.R
- class: DockerRequirement
  dockerFile:
    $include: ../../Dockerfile.renv
  dockerImageId: renvContainer
- class: NetworkAccess
  networkAccess: true

inputs:
- id: template_path
  type: File
  default:
    class: File
    location: ../../data/03_icasa_template/icasa_template_allColumns.xlsm
  inputBinding:
    prefix: --template_path
- id: markdown_folder
  type: Directory
  default:
    class: Directory
    location: ../../data/02_final_processed_md
  inputBinding:
    prefix: --markdown_folder
- id: json_folder
  type: string
  default: data/04_manual_json
  inputBinding:
    prefix: --json_folder
- id: output_directory
  type: string
  default: test
  inputBinding:
    prefix: --output_directory

outputs:
- id: json_data
  type: Directory
  outputBinding:
    glob: $(inputs.json_folder)
- id: output_directory
  type: Directory
  outputBinding:
    glob: $(inputs.output_directory)

baseCommand:
- Rscript
- R/assemble_training_set.R
