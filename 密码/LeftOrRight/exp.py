# f09e54c1bad2x38mvyg7wzlsuhkijnop
# 905e4c1fax328mdyvg7wbsuhklijznop

def fromFMtoL( mid ):
  global las #全局后序遍历
  global fir #先序遍历
  root = fir[0]  #取出当前树根
  fir = fir[1:]  #取出树根后 先序遍历把根拿出来 下面一个元素做树根
  root_po = mid.find( root ) #在中序遍历当中树根的位置
  left = mid[0:root_po]  #左子树
  right = mid[root_po+1:len(mid)] #右子树
  '''
  后序遍历： 左 右 根 
  先左子树 再右子树 最后跟
  '''
  #有左子树的时候
  if len(left) > 0:
    fromFMtoL( left )
  #有右子树的时候
  if len(right) > 0:
    fromFMtoL( right )
  #树根写进结果
  las += root
if __name__ == "__main__" :
  # fir = input("请输入先序遍历：")   #前序遍历的结果
  # mid = input("请输入中序遍历：")   #中序遍历的结果
  fir = "f09e54c1bad2x38mvyg7wzlsuhkijnop"
  mid = "905e4c1fax328mdyvg7wbsuhklijznop"
  # fir = "ABC"
  # mid = "BAC"
  las = ""
  fromFMtoL( mid )
  print(las)
