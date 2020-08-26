from mailmerge import MailMerge
import os
from datetime import datetime as dt
import pandas as pd

cwd = os.getcwd()
template_filename = 'fax_cover_template.docx'
template_filepath = os.path.join(cwd, 'data', template_filename)

document = MailMerge(template_filepath)

respondents_filename = 'fax_respondents_list.xlsx'
respondents_filepath = os.path.join(cwd, 'data', respondents_filename)

respondents = pd.read_excel(respondents_filepath)

respondents_list = []
today = '%s년 %s월 %s일' %(dt.now().year, dt.now().month, dt.now().day)

for index in respondents.index:
    new_respondent = {}
    new_respondent['name'] = respondents.loc[index, 'name']
    new_respondent['fax'] = respondents.loc[index, 'fax']
    new_respondent['phone'] = respondents.loc[index, 'phone']
    new_respondent['date'] = today
    new_respondent['title'] = respondents.loc[index, 'title']
    new_respondent['memo'] = respondents.loc[index, 'memo']
    respondents_list.append(new_respondent)
    
document.merge_templates(respondents_list, separator='page_break')

output_filepath = os.path.join(cwd, 'output', 'fax_cover_multi_pages_excel_data.docx')
document.write(output_filepath)
