#!/usr/bin/env cwl-runner

cwlVersion: v1.2
class: CommandLineTool

requirements:
- class: InitialWorkDirRequirement
  listing:
  - entryname: R/assemble_training_set.R
    entry:
      $include: ../../R/assemble_training_set.R
  - entryname: data/03_icasa_template/icasa_template_allColumns.xlsm
    entry: $(inputs.data_03_icasa_template_icasa_template_allcolumns_xlsm)
- class: DockerRequirement
  dockerFile:
    $include: ../../Dockerfile.renv
  dockerImageId: sciwin-container
- class: NetworkAccess
  networkAccess: true

inputs:
- id: data_03_icasa_template_icasa_template_allcolumns_xlsm
  type: File
  default:
    class: File
    location: ../../data/03_icasa_template/icasa_template_allColumns.xlsm

outputs:
- id: 03_manual_json
  type: Directory
  outputBinding:
    glob: data/03_manual_json/

baseCommand:
- Rscript
- R/assemble_training_set.R
