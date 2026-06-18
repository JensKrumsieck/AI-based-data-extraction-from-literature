#!/usr/bin/env cwl-runner

cwlVersion: v1.2
class: CommandLineTool

requirements:
- class: InitialWorkDirRequirement
  listing:
  - entryname: R/json2tabular_fertilizeration_improved.R
    entry:
      $include: ../../R/json2tabular_fertilizeration_improved.R
- class: DockerRequirement
  dockerFile:
    $include: ../../Dockerfile.renv
  dockerImageId: renv-container

inputs:
- id: input_folder
  type: Directory
  default:
    class: Directory
    location: ../../data/07_llm_output_json
  inputBinding:
    prefix: --input_folder
- id: output_folder
  type: Directory
  default:
    class: Directory
    location: ../../llm_output_tabular/fertilizers
  inputBinding:
    prefix: --output_folder

outputs:
- id: llm_output_tabular
  type: Directory
  outputBinding:
    glob: llm_output_tabular/

baseCommand:
- Rscript
- R/json2tabular_fertilizeration_improved.R
