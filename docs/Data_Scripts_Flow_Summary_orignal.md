# Data Flow Summary

```
                                    [INPUT] PDF papers
                                           |
                                           v
                             +----------------------------+
                             |  STEP 1: pdf → markdown    |
                             |  step1_pdf_to_markdown.py  |
                             +----------------------------+
                                          |
                              [OUTPUT] Markdown files (.md)
                                          |
         +-----------------+--------------+--------------+------------------+
         v                 v              v              v                  v
  +--------------+  +--------------+      |      +-------------+  +-------------+
  |  STEP 2.1    |  |  STEP 2.2    |      |      |  STEP 2.4   |  |  STEP 2.6   |
  | extract      |  | extract      |      |      | extract     |  | extract     |
  | method       |  | tables       |      |      | authors     |  | pub. date   |
  | sections     |  | bef. method  |      |      |             |  |             |
  +--------------+  +--------------+      |      +-------------+  +-------------+
         |                  |             |              |                  |
  [OUT] *_results.md [OUT] *_tables.md    |      [OUT] *_authors.md [OUT] *_dates.md
         |                  |             |              |                  |
         +--------+---------+             |              |                  |
                  v                       |              |                  |
         +--------------+                 |              |                  |
         |  STEP 2.3    |                 |              |                  |
         | combine      |                 |              |                  |
         | methods +    |                 |              |                  |
         | tables       |                 |              |                  |
         +--------------+                 |              |                  |
                  |                       |              |                  |
         [OUT] combined.md                |              |                  |
                  |                       |              |                  |
                  +-----------------------+--------------+                  |
                                          |                                 |
                                          v                                 |
                              +----------------------------+                |
                              |  STEP 2.5                  |                |
                              |  add authors to combined   |                |
                              +----------------------------+                |
                                          |                                 |
                              [OUT] combined + authors .md                  |
                                          |                                 |
                                          +---------------------------------+
                                          |
                                          v
                              +----------------------------+
                              |  STEP 2.7                  |
                              |  add date to combined      |
                              +----------------------------+
                                          |
                              [OUT] FINAL enriched .md
                                          |
                    +---------------------+----------------------+
                    |                     |                      |
                    v                     v                      v
  +----------------------+  +----------------------------+  +--------------------------+
  |  02_icasa_template/  |  |  03_training_data/         |  |  04_manual_json/         |
  |  ICASA variable      |  |  JSONL fine-tuning         |  |  ground-truth manual     |
  |  schema (Excel)      |  |  datasets                  |  |  JSON extractions        |
  |  [read at runtime]   |  |  [used to train model]     |  |  [used to train model]   |
  +----------------------+  +----------------------------+  +--------------------------+
                    |                     |                      |
                    +---------------------+----------------------+
                                          |
                                          v
                              +----------------------------+
                              |  STEP 3                    |
                              |  LLM extract ICASA vars    |
                              |  fine-tuned GPT (OpenAI)   |
                              +----------------------------+
                                          |
                          +---------------+---------------+
                          v                               v
             [OUT] 06_llm_output_json/     [OUT] 07_llm_output_tabular/
             <cat>/<paper>_<cat>.json           <category>.xlsx
                                                          |
                                          compare <-------+
                                               v
                                  [REF] 05_manual_tabular/
                                  (human baseline Excel)
```
