02_icasa_template/
ICASA variable  schema (Excel)
[read at runtime]
=> this icasa template was created by colleague based on icasa dictionary available online



03_training_data/
JSONL fine-tuning
datasets
[used to train model] 
=> Then use a R script we could create a jsonL file from template, I will send you the Rscript. but for each categories it is different. so for this step i have eight for eight categories. Theis jsonl files consist 55 items, part of them will be used for training the model.


04_manual_json/
ground-truth manual 
JSON extractions 
 [used to train model] 
=> The 03 folder template could also convert to json file separate for each paper this was using the same R script which i use for 03



| STEP 3 | | LLM extract ICASA vars | | LLM extract ICASA vars | | fine-tuned GPT (OpenAI) | 
=> the 03 jsonL data will be uploaded in OPENAI platform, then I could get the fine tuned model, then I call in Pzthon script 3.1 then I can get the LLm output


[OUT] 07_llm_output_tabular/
<category>.xlsx
=>  the LLM output json could convert to tabular then compare with 04 what we manuallz extract json to tabular then compare.