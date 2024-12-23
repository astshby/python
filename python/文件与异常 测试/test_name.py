def fetformatname(first,last):
    """生成格式规范的姓名"""
    fullname=f"{first} {last}"
    return fullname
def test_flname():
    """能否正确识别名字"""
    fullname=fetformatname('h','by')
    assert fullname=='h by'

# i=5
# while i:
#     first=input('first name\n')
#     last=input('last name\n')
#     full=fetformatname(first=first,last=last)
#     print(full)
#     i=i-1