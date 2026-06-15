#!/usr/bin/env cwl-runner

cwlVersion: v1.2
class: CommandLineTool

requirements:
- class: InitialWorkDirRequirement
  listing:
  - entryname: py/step2_process_paper.py
    entry:
      $include: ../../py/step2_process_paper.py

inputs:
- id: input_folder
  type: Directory
  default:
    class: Directory
    location: ../../data/01_paper_to_md
  inputBinding:
    prefix: --input_folder
- id: output_folder
  type: string
  default: test
  inputBinding:
    prefix: --output_folder

outputs:
- id: test
  type: Directory
  outputBinding:
    glob: test/

baseCommand:
- python3
- py/step2_process_paper.py
