import requests, os

def download_courses(course_num):
    links = 'http://textofvideo.nptel.iitm.ac.in/'+str(course_num)+'/lec'
    i = 1
    #for i in range(1,num_lec+1):
    while True:
        link = links + str(i) + ".pdf"	
        book_name = link.split('/')[-1]
        with open(book_name, 'wb') as book:
            a = requests.get(link, stream=True)
            if a.status_code != 200:
                book.close()
                os.remove(book_name)
                return
            for block in a.iter_content(512):
                if not block:
                    break
                book.write(block)      
        print('Downloaded ' + book_name)
        i += 1

download_courses('106105081') #put in the number of the course and number of lectures here
