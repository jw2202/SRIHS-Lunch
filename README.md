# SRIHS-Lunch

### ENG

Sunrin Internet High School Lunch fetcher

This app uses [Sunrin Internet High School web site](https://sunrint.sen.hs.kr/). if this site is blocked, it will not works.

### KOR

선린인고 급식 불러오기

이 앱은 [선린인고 웹 사이트](https://sunrint.sen.hs.kr)를 사용합니다. 이 사이트가 막힌다면 이 앱은 작동하지 않을 것입니다.

## Install

```bash
git clone https://github.com/jw2202/SRIHS-Lunch.git
cd SRIHS-Lunch
sudo ln -s ${PWD}/app.py /usr/bin/lunch
```

## Usage
```
Usage: lunch <days_for_fetch>
```

```
$ lunch 1
2024.11.04 월: 기장밥 쇠고기무국 모듬장조림(Y) 오이부추무침 치즈닭갈비 백김치 딸기짜먹는요거트(*) (815 kcal)
```