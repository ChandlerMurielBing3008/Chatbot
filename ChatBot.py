import shelve
from fuzzywuzzy import fuzz
#
# with shelve.open("Queries", writeback=True)as query:
# with shelve.open("Terminate", writeback=True)as terminate:
# with shelve.open("Path", writeback=True)as path:
#
query = shelve.open("Queries", writeback=True)
terminate = shelve.open("Terminate", writeback=True)
path = shelve.open("Path", writeback=True)

Terminate = dict.copy(dict(terminate))
Query = dict.copy(dict(query))
Path = dict.copy(dict(path))

query.close()
terminate.close()
path.close()

print("Hello, fellow citizen of India")
print("how can I be at service")
flag = False
while True:
    found = False

    print("="*40)
    ask = str(input()).lower()
    print("="*40)

    for q in Terminate["term"]:
        if fuzz.ratio(ask, q) > 45 or q in ask:
            ask = Terminate["term"][q]
            flag = True
            break
    if flag is True:
        print(Query[ask])
        break

    for q in Path["pat"]:
        if fuzz.ratio(ask, q) > 45 or q in ask:
            ask = Path["pat"][q]
            found = True
            print(Query[ask])
            break

    if found is False:
        print("kindly visit FAQ for more details")
