import json
import re
import os
import sys

home_dir = os.path.expanduser("~")

def load_json(filename):
    with open(filename, 'r') as file:
        return json.load(file)

def save_json(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

def find_result_files():
    pattern = re.compile(r'text_[^.]*\.json')
    return [file for file in os.listdir(f'{home_dir}/surchin/') if pattern.match(file)]

def process_url(url, rules):
    for rule in rules:
        if not rule["disabled"]:
            pattern = re.sub(r'\*', '(.*)', rule["includePattern"])
            match = re.match(pattern, url)
            if match:
                new_url = re.sub(r'\$1', match.group(1), rule["redirectUrl"])
                return new_url
    return url

def generate_html(input_data):
    html_content = '<html><head><title>Entries</title></head><body><ol>'
    for idx, entry in enumerate(input_data, start=1):
        html_content += f'<li><a href="{entry["href"]}">{entry["title"]}</a><p>{entry["body"]}</p>'
        html_content += f'<div class ="linky"><p>{entry["href"]}</p></div></li>'
    html_content += '</ol></body></html>'

    with open('output.html', 'w') as file:
        file.write(html_content)

def main():
    redirector_rules = load_json(os.path.join(home_dir, 'surchin', 'Redirector.json'))
    json_files = find_result_files()

    for filename in json_files:
        input_data = load_json(filename)
        for item in input_data: 
            item["href"] = process_url(item["href"], redirector_rules)
        save_json(filename, input_data)
        generate_html(input_data)

if __name__ == "__main__":
    main()
