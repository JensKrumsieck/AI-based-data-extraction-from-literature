#!/usr/bin/env cwl-runner

cwlVersion: v1.2
class: CommandLineTool

requirements:
- class: InitialWorkDirRequirement
  listing:
  - entryname: R/json_to_xlsx.R
    entry:
      $include: ../../R/json_to_xlsx.R
- class: DockerRequirement
  dockerFile:
    $include: ../../Dockerfile.renv
  dockerImageId: sciwin-container

inputs:
- id: input_folder
  type: Directory
  default:
    class: Directory
    location: ../../data/04_manual_json
  inputBinding:
    prefix: --input_folder
- id: output_folder
  type: string
  default: manual_tabular
  inputBinding:
    prefix: --output_folder

outputs:
- id: manual_tabular
  type: Directory
  outputBinding:
    glob: manual_tabular/

baseCommand:
- Rscript
- R/json_to_xlsx.R
