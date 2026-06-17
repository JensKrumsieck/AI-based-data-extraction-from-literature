#!/usr/bin/env cwl-runner

cwlVersion: v1.2
class: CommandLineTool

requirements:
- class: InitialWorkDirRequirement
  listing:
  - entryname: R/generate_icasa_json.R
    entry:
      $include: ../../R/generate_icasa_json.R
  - entryname: R/icasa_attributes_config.R
    entry: $(inputs.r_icasa_attributes_config_r)
- class: DockerRequirement
  dockerFile:
    $include: ../../Dockerfile.renv
  dockerImageId: renv-container

inputs:
- id: template_path
  type: File
  default:
    class: File
    location: ../../data/03_icasa_template/icasa_template_allColumns.xlsm
  inputBinding:
    prefix: --template_path
- id: json_folder
  type: string
  default: test
  inputBinding:
    prefix: --json_folder
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
- R/generate_icasa_json.R
