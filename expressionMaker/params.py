import sys
if len(sys.argv) < 3:
  print('请输入最大值和生成题目数')
  exit()
MAX = int(sys.argv[1])
expression_num = int(sys.argv[2])
# MAX = 5
# expression_num = 100