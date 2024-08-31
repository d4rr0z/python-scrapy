import scrapy
from coursescraper.items import CoursescraperItem

class CoursespiderSpider(scrapy.Spider):
    name = "coursespider"
    allowed_domains = ["uslugirozwojowe.parp.gov.pl"]
    start_urls = [
        "https://uslugirozwojowe.parp.gov.pl/wyszukiwarka/uslugi/szukaj?nazwaUslugi=&podkategoria%5B%5D=560&podkategoria%5B%5D=561&podkategoria%5B%5D=562&podkategoria%5B%5D=563&podkategoria%5B%5D=564&podkategoria%5B%5D=565&podkategoria%5B%5D=566&podkategoria%5B%5D=567&mozliwoscDofinansowania=true&cenaOd=&cenaDo=&cenaRodzaj=brutto_usluga&godzinyOd=&godzinyDo=&dataRozpoczeciaZakres=&dataZakonczeniaZakres=&miejsceSzkolenia=&miejscowoscId=&wojewodztwoId=&promienZasiegu=&nabycieKwalifikacji=false&wykluczUslugiDedykowane=true&order=_score-desc&wynikiNaStronie=10&numerStrony=0",
        "https://uslugirozwojowe.parp.gov.pl/wyszukiwarka/uslugi/szukaj?nazwaUslugi=&podkategoria%5B%5D=490&podkategoria%5B%5D=492&podkategoria%5B%5D=540&mozliwoscDofinansowania=true&cenaOd=&cenaDo=&cenaRodzaj=brutto_usluga&godzinyOd=&godzinyDo=&dataRozpoczeciaZakres=&dataZakonczeniaZakres=&miejsceSzkolenia=&miejscowoscId=&wojewodztwoId=&promienZasiegu=&nabycieKwalifikacji=false&wykluczUslugiDedykowane=true&order=_score-desc&wynikiNaStronie=10&numerStrony=0",
        "https://uslugirozwojowe.parp.gov.pl/wyszukiwarka/uslugi/szukaj?nazwaUslugi=&podkategoria%5B%5D=470&podkategoria%5B%5D=471&podkategoria%5B%5D=472&podkategoria%5B%5D=475&podkategoria%5B%5D=476&podkategoria%5B%5D=477&podkategoria%5B%5D=478&podkategoria%5B%5D=541&mozliwoscDofinansowania=true&cenaOd=&cenaDo=&cenaRodzaj=brutto_usluga&godzinyOd=&godzinyDo=&dataRozpoczeciaZakres=&dataZakonczeniaZakres=&miejsceSzkolenia=&miejscowoscId=&wojewodztwoId=&promienZasiegu=&nabycieKwalifikacji=false&wykluczUslugiDedykowane=true&order=_score-desc&wynikiNaStronie=10&numerStrony=0",
        "https://uslugirozwojowe.parp.gov.pl/wyszukiwarka/uslugi/szukaj?nazwaUslugi=&podkategoria%5B%5D=481&podkategoria%5B%5D=482&podkategoria%5B%5D=483&podkategoria%5B%5D=484&podkategoria%5B%5D=485&podkategoria%5B%5D=488&podkategoria%5B%5D=542&podkategoria%5B%5D=543&podkategoria%5B%5D=544&mozliwoscDofinansowania=true&cenaOd=&cenaDo=&cenaRodzaj=brutto_usluga&godzinyOd=&godzinyDo=&dataRozpoczeciaZakres=&dataZakonczeniaZakres=&miejsceSzkolenia=&miejscowoscId=&wojewodztwoId=&promienZasiegu=&nabycieKwalifikacji=false&wykluczUslugiDedykowane=true&order=_score-desc&wynikiNaStronie=10&numerStrony=0",
        "https://uslugirozwojowe.parp.gov.pl/wyszukiwarka/uslugi/szukaj?nazwaUslugi=&podkategoria%5B%5D=575&podkategoria%5B%5D=576&podkategoria%5B%5D=577&podkategoria%5B%5D=578&mozliwoscDofinansowania=true&cenaOd=&cenaDo=&cenaRodzaj=brutto_usluga&godzinyOd=&godzinyDo=&dataRozpoczeciaZakres=&dataZakonczeniaZakres=&miejsceSzkolenia=&miejscowoscId=&wojewodztwoId=&promienZasiegu=&nabycieKwalifikacji=false&wykluczUslugiDedykowane=true&order=_score-desc&wynikiNaStronie=10&numerStrony=0",
        "https://uslugirozwojowe.parp.gov.pl/wyszukiwarka/uslugi/szukaj?nazwaUslugi=&podkategoria%5B%5D=445&podkategoria%5B%5D=446&podkategoria%5B%5D=447&podkategoria%5B%5D=448&podkategoria%5B%5D=449&podkategoria%5B%5D=450&podkategoria%5B%5D=452&podkategoria%5B%5D=453&mozliwoscDofinansowania=true&cenaOd=&cenaDo=&cenaRodzaj=brutto_usluga&godzinyOd=&godzinyDo=&dataRozpoczeciaZakres=&dataZakonczeniaZakres=&miejsceSzkolenia=&miejscowoscId=&wojewodztwoId=&promienZasiegu=&nabycieKwalifikacji=false&wykluczUslugiDedykowane=true&order=_score-desc&wynikiNaStronie=10&numerStrony=0",
        "https://uslugirozwojowe.parp.gov.pl/wyszukiwarka/uslugi/szukaj?nazwaUslugi=&podkategoria%5B%5D=413&podkategoria%5B%5D=414&podkategoria%5B%5D=415&podkategoria%5B%5D=416&podkategoria%5B%5D=417&podkategoria%5B%5D=418&podkategoria%5B%5D=419&podkategoria%5B%5D=420&podkategoria%5B%5D=421&podkategoria%5B%5D=422&podkategoria%5B%5D=424&podkategoria%5B%5D=425&mozliwoscDofinansowania=true&cenaOd=&cenaDo=&cenaRodzaj=brutto_usluga&godzinyOd=&godzinyDo=&dataRozpoczeciaZakres=&dataZakonczeniaZakres=&miejsceSzkolenia=&miejscowoscId=&wojewodztwoId=&promienZasiegu=&nabycieKwalifikacji=false&wykluczUslugiDedykowane=true&order=_score-desc&wynikiNaStronie=10&numerStrony=0",
        "https://uslugirozwojowe.parp.gov.pl/wyszukiwarka/uslugi/szukaj?nazwaUslugi=&podkategoria%5B%5D=510&podkategoria%5B%5D=511&podkategoria%5B%5D=512&podkategoria%5B%5D=513&podkategoria%5B%5D=514&podkategoria%5B%5D=515&podkategoria%5B%5D=516&podkategoria%5B%5D=517&podkategoria%5B%5D=518&podkategoria%5B%5D=519&podkategoria%5B%5D=520&podkategoria%5B%5D=526&podkategoria%5B%5D=539&podkategoria%5B%5D=545&mozliwoscDofinansowania=true&cenaOd=&cenaDo=&cenaRodzaj=brutto_usluga&godzinyOd=&godzinyDo=&dataRozpoczeciaZakres=&dataZakonczeniaZakres=&miejsceSzkolenia=&miejscowoscId=&wojewodztwoId=&promienZasiegu=&nabycieKwalifikacji=false&wykluczUslugiDedykowane=true&order=_score-desc&wynikiNaStronie=10&numerStrony=0",
        "https://uslugirozwojowe.parp.gov.pl/wyszukiwarka/uslugi/szukaj?nazwaUslugi=&podkategoria%5B%5D=556&podkategoria%5B%5D=557&podkategoria%5B%5D=558&mozliwoscDofinansowania=true&cenaOd=&cenaDo=&cenaRodzaj=brutto_usluga&godzinyOd=&godzinyDo=&dataRozpoczeciaZakres=&dataZakonczeniaZakres=&miejsceSzkolenia=&miejscowoscId=&wojewodztwoId=&promienZasiegu=&nabycieKwalifikacji=false&wykluczUslugiDedykowane=true&order=_score-desc&wynikiNaStronie=10&numerStrony=0",
        "https://uslugirozwojowe.parp.gov.pl/wyszukiwarka/uslugi/szukaj?nazwaUslugi=&podkategoria%5B%5D=455&podkategoria%5B%5D=460&podkategoria%5B%5D=461&podkategoria%5B%5D=462&podkategoria%5B%5D=464&podkategoria%5B%5D=465&podkategoria%5B%5D=466&podkategoria%5B%5D=467&podkategoria%5B%5D=571&podkategoria%5B%5D=572&podkategoria%5B%5D=573&podkategoria%5B%5D=574&mozliwoscDofinansowania=true&cenaOd=&cenaDo=&cenaRodzaj=brutto_usluga&godzinyOd=&godzinyDo=&dataRozpoczeciaZakres=&dataZakonczeniaZakres=&miejsceSzkolenia=&miejscowoscId=&wojewodztwoId=&promienZasiegu=&nabycieKwalifikacji=false&wykluczUslugiDedykowane=true&order=_score-desc&wynikiNaStronie=10&numerStrony=0",
        "https://uslugirozwojowe.parp.gov.pl/wyszukiwarka/uslugi/szukaj?nazwaUslugi=&podkategoria%5B%5D=569&podkategoria%5B%5D=570&mozliwoscDofinansowania=true&cenaOd=&cenaDo=&cenaRodzaj=brutto_usluga&godzinyOd=&godzinyDo=&dataRozpoczeciaZakres=&dataZakonczeniaZakres=&miejsceSzkolenia=&miejscowoscId=&wojewodztwoId=&promienZasiegu=&nabycieKwalifikacji=false&wykluczUslugiDedykowane=true&order=_score-desc&wynikiNaStronie=10&numerStrony=0",
        "https://uslugirozwojowe.parp.gov.pl/wyszukiwarka/uslugi/szukaj?nazwaUslugi=&podkategoria%5B%5D=547&podkategoria%5B%5D=548&podkategoria%5B%5D=549&podkategoria%5B%5D=550&podkategoria%5B%5D=551&podkategoria%5B%5D=552&podkategoria%5B%5D=553&podkategoria%5B%5D=554&mozliwoscDofinansowania=true&cenaOd=&cenaDo=&cenaRodzaj=brutto_usluga&godzinyOd=&godzinyDo=&dataRozpoczeciaZakres=&dataZakonczeniaZakres=&miejsceSzkolenia=&miejscowoscId=&wojewodztwoId=&promienZasiegu=&nabycieKwalifikacji=false&wykluczUslugiDedykowane=true&order=_score-desc&wynikiNaStronie=10&numerStrony=0"
    ]

    def parse(self, response):
        courses = response.css('div.card-body')

        for course in courses:
            try:
                course_url = 'https://uslugirozwojowe.parp.gov.pl' + course.css('h3 a::attr(href)').get()
            except:
                continue
            yield response.follow(course_url, callback=self.parse_course_page)

        next_page = response.css('li.next.page-item a::attr(href)').get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)

    def parse_course_page(self, response):
        course_name = response.css('h3 a::text').get()
        course_category = response.xpath("//div[contains(text(), 'Kategoria')]/following-sibling::div/text()").get()
        goals_list = response.xpath("//h2[contains(text(), 'Cel')]/following-sibling::text()").getall()
        results_list = response.xpath("//div[contains(text(), 'Efekty uczenia się')]/following-sibling::text()").getall()
        program_list = response.xpath("//h2[contains(text(), 'Program')]/following-sibling::div//*/text()").getall()

        course_item = CoursescraperItem()
        course_item['name'] = course_name.strip()
        course_item['category'] = course_category.split("/")[0].strip()
        course_item['goals'] = ' '.join([item.strip() for item in goals_list if item.strip()])
        course_item['results'] = ' '.join([item.strip() for item in results_list if item.strip()])
        course_item['program'] = ' '.join([item.strip() for item in program_list if item.strip()])
        yield course_item