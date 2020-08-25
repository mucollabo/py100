from mailmerge import MailMerge
import os

# MS Word 템플릿 파일 경로 지정하기
cwd = os.getcwd()
template_filename = 'greetings_template.docx'
template_filepath = os.path.join(cwd, 'data', template_filename)

document = MailMerge(template_filepath)
print(document.get_merge_fields())