from pathlib import Path
contexts='I love python\n'
contexts+='fuck you\n'
contexts+='Engineering drawing\n'

path=Path('test_work/write.txt')
a=path.write_text(contexts)
print(a)
