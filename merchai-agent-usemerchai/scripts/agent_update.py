# Simple agent updater for MerchAI site
import re, os
html_path = "index.html"
issue_path = os.environ.get("ISSUE_BODY_FILE","issue_body.txt")
def set_block(tag,new_text,html):
    return re.sub(rf"(<!--AGENT:{tag}-->)(.*?)(<!--/AGENT:{tag}-->)",rf"\1{new_text}\3",html,flags=re.S)
body=open(issue_path).read() if os.path.exists(issue_path) else ""
with open(html_path) as f: html=f.read()
for tag in ["TITLE","DESCRIPTION","OGTITLE","OGDESC","CTA","HERO","SUBHEAD","SERVICES","CONTACT"]:
    m=re.search(rf"SET {tag}: (.+)",body)
    if m: html=set_block(tag,m.group(1),html)
with open(html_path,"w") as f: f.write(html)