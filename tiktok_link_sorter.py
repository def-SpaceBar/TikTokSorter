import time

def tikdupe_db():
    database = []
    check_list = []
    duplicates = []
    duplicates_count = 0
    with open('db.txt','r', encoding='utf-8') as links_db:
        for line in links_db.readlines():
            if line[-1:] == "\n":
                database.append(line[:-1])
            else:
                database.append(line)
    with open('links.txt','r', encoding='utf-8') as check:
        for line in check.readlines():
            start = 'https://vt.tiktok.com/'
            end = '/?k=1'
            s = line
            line = s[s.find(start) + len(start):s.rfind(end)]
            if line[-1:] == "\n":
                check_list.append(line[:-1])
            else:
                check_list.append(line)
    print('Database:', database)
    print('Check List:', check_list)
    time.sleep(1)
    db_count = len(database)
    check_list_count = len(check_list)
    print('-----------------------------\n' + 'Statistics: \n\t' + 'Database Entries:' + str(db_count) + '\n\t' + '\n\t' + 'Check List:' + str(check_list_count))
    print('-----------------------------')
    for i in check_list:
        if i in database:
            print("Duplicate: " + i)
            check_list.remove(i)
            duplicates.append(i)
    with open('duplicates.txt','r+') as dupe:
        for i in duplicates:
            dupe.write(i)
    print(duplicates)
tikdupe_db()