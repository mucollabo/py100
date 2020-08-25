from mailmerge import MailMerge
import os
from datetime import datetime as dt

cwd = os.getcwd()
template_filename = 'fax_cover_template.docx'
template_filepath = os.path.join(cwd, 'data', template_filename)

document = MailMerge(template_filepath)

respondent1 = {
    'name' : '안철현',
    'fax' : '02-813-0901',
    'phone' : '010-9545-7547',
    'date' : '%s년 %s월 %s일' %(dt.now().year, dt.now().month, dt.now().day),
    'title' : '세금계산서 재발행 요청의 건',
    'memo' : '2020년 8월분',
}

respondent2 = {
    'name' : '안정민',
    'fax' : '02-123-4567',
    'phone' : '010-9876-5432',
    'date' : '%s년 %s월 %s일' %(dt.now().year, dt.now().month, dt.now().day),
    'title' : '재정 감사',
    'memo' : '2020년 12월 예',
}

respondents_list = [respondent1, respondent2]
document.merge_templates(respondents_list, separator='page_break')

output_filepath = os.path.join(cwd, 'output', 'fax_cover_output_multi_pages.docx')
document.write(output_filepath)