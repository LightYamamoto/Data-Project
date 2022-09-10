import scrapy
import re
from scrapy_splash import SplashRequest
from no_accent_vietnamese import no_accent_vietnamese
class CovidSpider(scrapy.Spider):

    name = 'covid'
    allowed_domains = ['web.archive.org']
    start_urls = ['https://web.archive.org/web/20210914011208/https://covid19.gov.vn/big-story/cap-nhat-dien-bien-dich-covid-19-moi-nhat-hom-nay-171210901111435028.htm']



    def parse(self, response):
        
        
       
       
        
        # # Loop qua lần lượt từng bảng số liệu, dùng xpath tách phần tử cần truy vấn, sử lí bằng hàm RegEx

        

        for data in response.xpath('//li[contains(@class,"kbwscwl clearfix cc timeline-item")]'):
            # Truy vấn data trong từng bảng bằng xpath và sử lí bằng regEx để ra kết quả
            raw_time = data.xpath('.//div[1]/div[1]/text()').get()
            time = re.findall("\d{2}:\d{2} \d{2}\/\d{2}\/\d{4}",raw_time)

            raw_new_case = data.xpath(".//div[1]/div[2]/h3/text()").get()
            new_case = re.findall("\d{1,5}.\d{1,7}",raw_new_case)

            # Xử lí số ca từng tỉnh bằng module no_accent_vietnamese
            raw_case_per_city = data.xpath(".//div[2]/p[1]/text()").get()
            case_per_city = no_accent_vietnamese(raw_case_per_city)
            city =re.findall("(?<=[tai\,,\s]).{3,16}(?=\()",case_per_city)
            case = re.findall("(?<=\()\w?.?\w+(?=\))",case_per_city)
            
            city_case=[]
            for i in range(len(case)):
                city_case.append({'city':city[i],'case':case[i]})
            yield {
                'time': time[0],
                'new_case': new_case[0],
                'city_case':city_case
                }
        # Lấy url để truyền vào Splash để thực hiện thao tác Next    
        url = response.xpath('.//meta[@property="og:url"]/@content').get()
        yield SplashRequest(url=str(url),callback= self.parse,endpoint = "execute",args = {'lua_source': self.script})

    script = '''
    function main(splash, args)
        splash.private_mode_enabled = false
        url = args.url
        assert(splash:go(url))
        assert(splash:wait(10))
        next_day = assert(splash:select("#wm-toolbar > div.n > table > tbody > tr.d > td.f > a > img"))
        next_day:mouse_click()
        assert(splash:wait(10))
        splash:set_viewport_full()
        return splash:html()   
    end
    '''
    
    