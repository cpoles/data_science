'''Linkedin Scraper'''

from selenium import webdriver
import time

# constants
URL_LINKEDIN_DS = 'https://www.linkedin.com/jobs/data-scientist-jobs?position=1&pageNum=0'

# main function
if __name__ == '__main__':
    driver = webdriver.Chrome() 
    driver.implicitly_wait(10) # max wait time for a page to load
    # get the linkedin search results page
    driver.get(URL_LINKEDIN_DS) 
   
    # get the job card list
    job_card_list = driver.find_elements_by_class_name('result-card')
    print(f'Number of jobs: {len(job_card_list)}')
    
    
    description_list = []

    while True:
        # sentinel condition
        if len(description_list) == len(job_card_list):
            break
 
        # go through the job results, click and fetch the job description
        for job_card in job_card_list[len(description_list):]:  
            print(job_card.text)
            job_card.click() # click on the job
            time.sleep(3)
            try:
                # get job description
                description = driver.find_element_by_class_name('description').text
                description_list.append(description)
                print(description)
            except:
                print('Erro.')
                pass

        # load the next set of results 
        job_card_list = driver.find_elements_by_class_name('result-card') 
        
        print(f'Number of jobs: {len(job_card_list)}')
        print(f'Number of decriptions: {len(description_list)}')


    # concatenate the descriptions with \n
    descriptions = '\n'.join(description_list)
    # save the descriptions to a text file
    with open('jobs_descriptions.txt', 'w') as f:
        f.write(descriptions)


    driver.quit()




