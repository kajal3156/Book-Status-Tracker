name = input("BOOK NAME: ")
pages = int(input("TOTAL PAGES: "))
read = int(input("TOTAL PAGES READ: "))
if read>pages:
    print("error total pages can't be less than total pages read")
else:
    c = pages - read
    progress = (read/pages)*100
    print("BOOK: ",name)
    print("TOTAL PAGES: ",pages)
    print("TOTAL PAGES READ: ",read)
    print("TOTAL PAGES LEFT: ",c)
    print(f"PROGRESS: {progress:.2f}%")
if pages>read:
    print("STILL READING")
elif pages == read:
    print("FINISHED")