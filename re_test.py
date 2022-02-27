import requests
import re
import os
import time
if __name__ == '__main__':
    start_directory = r'E:\Python\requests模块\Pictures'
    os.startfile(start_directory)
    url = 'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&tn=monline_4_dg&wd=%E7%99%BE%E5%BA%A6&oq=https%2526lt%253B%2526lt%253BA%252F%252Fwww.baidu.com%252Fs%2526lt%253B%2526lt%253BFcl%2526lt%253B%2526lt%253BD%2526lt%253B%2526lt%253B26tn%2526lt%253B%2526lt%253BDbaidutop10%2526lt%253B26fr%2526lt%253B%2526lt%253BDtop1000%2526lt%253B26wd%2526lt%253B%2526lt%253BD%2526lt%253B&rsv_pq=92ff880800019e36&rsv_t=9ec5vuWY8HwxgDDLMGrvumBvzWgp1n6wdmO79kYPhZeMugY%2BvYaisFtOXodSlODcCB%2Bb&rqlang=cn&rsv_enter=1&rsv_dl=tb&rsv_sug3=9&rsv_sug1=6&rsv_sug7=101&rsv_sug2=0&rsv_btype=t&inputT=1234&rsv_sug4=110491&rsv_sug=2'
    header ={ 
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0'
    }
    urls = []
    urls.append(url)
    i=1
   
    #print(requests_get.text)
    #result_urls = re.findall(r'(?<=href=")http:\/\/.*?(?=")', requests_get.text)
    #img_urls = re.findall(r'(?<=src=")https:\/\/.*?[^\.][^j][^s](?="[^+])', requests_get.text)
    for new_url in urls:
        time.sleep(1)
        #try:
        requests_get = requests.get(url=new_url,headers = header)
        add_urls = re.findall(r'(?<=href=")http:\/\/.*?(?=")', requests_get.text)
        img_urls = re.findall(r'(?<=src=")https:\/\/.*?[^\.][^j][^s](?="[^+])', requests_get.text)
        for url in add_urls:
            urls.append(url)
        for url in img_urls:
            time.sleep(1)
            response = requests.get(url,headers = header)
            content = response.content
                
            print(url)
            if url[-3:] == 'jpg':
                w=open(r'E:\Python\requests模块\Pictures\{}.jpg'.format(i),'wb')
                i+=1
                print('获取到{}张图片'.format(i))
                w.write(content)
            elif url[-4:] == 'jpeg':
                w=open(r'E:\Python\requests模块\Pictures\{}.jpeg'.format(i),'wb')
                i+=1
                print('获取到{}张图片'.format(i))
                w.write(content)
            elif url[-3:] == 'png':
                w=open(r'E:\Python\requests模块\Pictures\{}.png'.format(i),'wb')
                i+=1
                print('获取到{}张图片'.format(i))
                w.write(content)
    
        del new_url
        