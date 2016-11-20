import requests

links = 'http://textofvideo.nptel.iitm.ac.in/106108055/lec'
for i in range(1,42):
    link = links + str(i) + ".pdf"	
    book_name = link.split('/')[-1]
    with open(book_name, 'wb') as book:
        #print('Downloading ' + book_name)
        a = requests.get(link, stream=True)
        #content_size = len(a.content)
        #downloaded = 0
        for block in a.iter_content(512):
            if not block:
                break
            book.write(block)
            #downloaded += len(block)
            #print('Downloading ' + book_name + ' ' + str(100*(downloaded/content_size)) + '%')
            
    print('Downloaded ' + book_name)
