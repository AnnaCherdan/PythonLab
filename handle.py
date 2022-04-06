# Открывается файл для чтения только в той папке, которая прописана к консоли или  Шарме.
# handle = open("pup.txt")
# handle = open(r"D:\Общие документы\AnnCherdan\Pup.txt", "r")
# "r" показывает, что строка обрабатывается, как исходная.
# print('D:\Общие документы\AnnCherdan\Python')
handle = open("pup.txt", "r")
data = handle.read()
print(data)
handle.close()