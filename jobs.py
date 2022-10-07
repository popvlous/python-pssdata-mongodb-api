import datetime
import json

import requests
from flask import current_app, jsonify

from app import app, config
from model import CovidInfo
from util import sendActionRecordByOne, lineNotifyMessage
from bs4 import BeautifulSoup


def sendActionRecordJob():
    # 拋送資料
    with app.app_context():
        lineNotifyMessage(config.LINE_TOKEN, f' 溫馨提醒: 開始抓取COVID19網站資料 ')
        url = 'https://covid-19.nchc.org.tw/'  # 台積電 Yahoo 股市網址
        web = requests.get(url)  # 取得網頁內容
        soup = BeautifulSoup(web.text, "html.parser")  # 轉換內容
        total_cases = ''
        total_cases_tw = ''
        daily_cases = ''
        daily_cases_tw = ''
        total_deaths = ''
        daily_deaths_tw = ''
        tw_vaccinated = ''
        try:
            total_cases = soup.find("h1", class_="country_confirmed mb-1 text-success").text.replace(',', '')  # 找到累積確診
            total_cases_tw = soup.find_all("span", class_="country_confirmed_percent", limit=3)[0].text.split(' ')[1].replace(',', '')  # 本土累積確診
            daily_cases_tw = soup.find_all("span", class_="country_confirmed_percent", limit=3)[1].text.split(' ')[1]  # 每日確診
            daily_cases = soup.find("h1", class_="country_recovered mb-1 text-info").text.replace('+', '').replace(',', '')  # 找到每日確診
            total_deaths = soup.find("h1", class_="country_deaths mb-1 text-dark").text.replace(',', '')  # 找到累積死亡率
            daily_deaths_tw = soup.find_all("span", class_="country_deaths_change", limit=3)[0].text.replace('+', '')  # 找到本土死亡率
            tw_vaccinated = soup.find_all("span", class_="country_deaths_change", limit=3)[1].text.replace(',', '').split(' ')[1]  # 找到本土死亡率
            lineNotifyMessage(config.LINE_TOKEN, f' 溫馨提醒: https://covid-19.nchc.org.tw/，抓取資料完畢 ')
        except Exception as err:
            current_app.logger.error(f'sendActionRecord 發生錯誤: {err}')
            lineNotifyMessage(config.LINE_TOKEN,
                              f'溫馨提醒: https://covid-19.nchc.org.tw/ 發生錯誤: {err}')

        url1 = 'https://covid-19.nchc.org.tw/dt_002-csse_covid_19_daily_reports_vaccine_city2.php'  # 台積電 Yahoo 股市網址
        web1 = requests.get(url1)  # 取得網頁內容
        soup1 = BeautifulSoup(web1.text, "html.parser")  # 轉換內容
        dose_1st = ''
        dose_2st = ''
        try:
            dose_rate = soup1.find_all("span", class_="country_deaths_percent", limit=3)[0].text  # 找到累積確診
            dose_list = dose_rate.split('%')
            dose_1st = dose_list[0].split(' ')[1]
            dose_2st = dose_list[1].split(' ')[1]

            lineNotifyMessage(config.LINE_TOKEN, f' 溫馨提醒: https://covid-19.nchc.org.tw/dt_002-csse_covid_19_daily_reports_vaccine_city2.php，抓取資料完畢 ')
        except Exception as err:
            current_app.logger.error(f'sendActionRecord 發生錯誤: {err}')
            lineNotifyMessage(config.LINE_TOKEN,
                              f'溫馨提醒: https://covid-19.nchc.org.tw/dt_002-csse_covid_19_daily_reports_vaccine_city2.php 發生錯誤: {err}')


        remove_covids = CovidInfo.objects.all()
        for remove_covid in remove_covids:
            remove_covid.delete()

        covid_info = CovidInfo(total_deaths=total_deaths,
                               daily_deaths_tw=daily_deaths_tw,
                               total_cases=total_cases,
                               daily_cases=daily_cases,
                               total_cases_tw=total_cases_tw,
                               daily_cases_tw=daily_cases_tw,
                               tw_vaccinated=tw_vaccinated,
                               dose_1st=dose_1st,
                               dose_2st=dose_2st
                               )
        covid_info.save()
