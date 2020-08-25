from mailmerge import MailMerge
import os
from datetime import datetime as dt

cwd = os.getcwd()
template_filename = 'fax_cover_template.docx'
template_filepath = os.path.join(cwd, 'data', template_filename)

document = MailMerge(template_filepath)

document.merge(
    name = '안철현',
    fax = '031-777-7777',
    phone = '010-9545-7547',
    date = '%s년 %s월 %s일' %(dt.now().year, dt.now().month, dt.now().day),
    title = '세금계산서 재발행 요청의 건',
    memo = '2020년 8월분',
)

output_filepath = os.path.join(cwd, 'output', 'fax_cover_output.docx')
document.write(output_filepath)
