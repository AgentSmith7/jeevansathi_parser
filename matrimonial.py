def get_attr(page):
    response=requests.get(page)
    print "url got"
    soup=bs4.BeautifulSoup(response.text)
    print "url received"
    li=[a for a in soup.select("ul[class^=prfdesc] > li")]
    c=1
    for move in li:
        # print move.text
        st=u''.join(move.text).encode('utf-8')
        f.write(st+"; ")
        if c==8:
            break
        c+=1

    p_uls=[a.txt for a in soup.select(".prfdplist ul li > p")]

      # count=0
      # print p_uls.text
    partner_data={}
    partner_data['Marital status']="Any"
    partner_data['Country']="Any"
    partner_data['Religion']="Any"
    partner_data['Caste']="Any"
    partner_data['Mother tongue']="Any"
    partner_data['Income']="Any"
    partner_data['Education']="Any"

    for i, li in enumerate(p_uls):
        if li.text == "Age":
            partner_data['Age']=p_uls[i+1].text
        elif li.text == "Height":
            partner_data['height']=p_uls[i+1].text
        elif li.text =="Marital Status":
            partner_data['Marital status']=p_uls[i+1].text
        elif li.text == "Country":
            partner_data['Country']=p_uls[i+1].text
        elif li.text == "Religion":
            partner_data['Religion']=p_uls[i+1].text
        elif li.text == "Caste":
            partner_data['Caste']=p_uls[i+1].text
        elif li.text == "Mother tongue":
            partner_data['Mother tongue']=p_uls[i+1].text
        elif li.text == "Education ":
            partner_data['Education']=p_uls[i+1].text
        elif li.text == "Income ":
            partner_data['Income']=p_uls[i+1].text

    print partner_data["Age"],partner_data['height'],partner_data['Marital status'],partner_data['Country'],partner_data['Religion'],partner_data['Caste'],partner_data['Mother tongue'],partner_data['Education'],partner_data['Income']
    f.write(partner_data["Age"]+"; "+partner_data['height']+"; "+partner_data['Marital status']+"; "+partner_data['Country']+"; "+partner_data['Religion']+"; "+partner_data['Caste']+"; "+partner_data['Mother tongue']+"; "+partner_data['Education']+"; "+partner_data['Income'])

if __name__ == '__main__':
    from selenium import webdriver
    import requests
    import bs4
    import os
    root='http://www.jeevansathi.com'

    f=open("nazia_bride.csv",'w')
    dr = webdriver.PhantomJS()

    types=["hindi","marathi","hindi-up","punjabi","telgu","bengali","tamil","gujrati","malyalam","kannada","hindi-MP","bihari","rajasthani","oriya","konkani","himachali","haryanvi","assamese","kashmiri"]
    for i,l in enumerate(types):
        print "Working on",
        print 'http://www.jeevansathi.com/'+l+'-brides-girls'+"\n\n-----------------------------------\n"
        response=requests.get('http://www.jeevansathi.com/'+l+'-brides-girls')
        soup = bs4.BeautifulSoup(response.text)

        links=[a.attrs.get('href') for a in soup.select('div.comp1 a[href^=/bride]')]
        # for groom
        # links=[a.attrs.get('href') for a in soup.select('div.comp1 a[href^=/groom]')]

        addr=[root+link for link in links]
        for j,link in enumerate(addr):
            try:
                print "Working on bride %d \n" % (j+1)
                print link
                get_attr(link)
                f.write("\n")
            except Exception, e:
                print e
            
        print "Working on type %d " %(i)

