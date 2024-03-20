# Theia project
 
This project pulls public companies' SEC 10-k filings to extract business summaries, core industry/themes, core products, core customer groups, and market segments. It relies on Beautiful Soup for web scraping, various Transformer models to process text, and Pandas for tabular data.

The themes.py script contains Theia's sector and industry list, but used an LLM to generate the sub-industry and themes.

The theia_project_main notebook contains the core of the project.

Things that could have been added to improve the project but were not possible for lack of time:
-  Comprehensive unit tests
- Error catching and strategies to account for missing data
- Further cleaning of financial tables, possibility to join tables from different companies in order to perform (comparative) data analysis
- Finetuning of transformers rather than reliance upon zero-shot learning
- Using more data from 10-k filings in training if using GPU

