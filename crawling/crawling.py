import bs4 as bs
import urllib.request

page1 = urllib.request.urlopen("https://www.indeed.com/resumes?q=java&l=")
data1 = bs.BeautifulSoup(page1, 'lxml')
page2 = urllib.request.urlopen("https://www.indeed.com/resumes?q=java&co=IN&start=50")
data2 = bs.BeautifulSoup(page2, 'lxml')

first_50 = data1.find_all(class_='app_name')
next_50 = data2.find_all(class_='app_name')

def main():
    resume = data1.find_all('a', class_='app_link', limit=10)

    
    for urls in resume:
        x = urls['href']

        resume_url = urllib.request.urlopen("https://www.indeed.com"+x)
        resume_soup = bs.BeautifulSoup(resume_url, 'lxml')

        work_title = resume_soup.find_all(class_='work_title')
        work_dates = resume_soup.find_all(class_='work_dates')

        for w in work_title:
            print(w.text)
        for d in work_dates:
            print(d.text)

        print("##################################################################")
main()