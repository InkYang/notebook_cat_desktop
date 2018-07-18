import json
import sys

if len(sys.argv) < 2:
    raise Exception('参数数量必须大于1！')


# accept argument lst
notebook_path_lst = sys.argv[1:]

target_notebook = {}
cells_lst = []
# read notebook path list
for path in notebook_path_lst:
    with open(path) as notebook:
        notebook_str = notebook.read()
        notebook_json = json.loads(notebook_str)
        cells = notebook_json['cells']
        cells_lst += cells

target_notebook['cells'] = cells_lst

# 转化成字符串
target_notebook_str = json.dumps(target_notebook)

# 存入文件
with open('target_notebook.ipynb','w') as target:
    target.write(target_notebook_str)
