<div align="center">

# kenitoa

### 기록하고, 구현하고, 개선하는 개발자 포트폴리오

역사 아카이브 웹 서비스부터 리듬 게임, Java 데스크톱 앱, 알고리즘 실험 프로젝트까지  
아이디어를 실제로 동작하는 프로그램으로 만드는 과정을 기록하고 있습니다.

</div>

---

## About Me

저는 다양한 주제의 프로젝트를 직접 설계하고 구현하며 성장하고 있는 개발자입니다.  
프론트엔드, 백엔드, 데이터 관리, 데스크톱 애플리케이션, 게임 로직 구현까지 폭넓게 경험하고 있으며,  
단순히 기능을 만드는 것보다 **구조화된 코드**, **사용자 흐름**, **확장 가능한 설계**를 함께 고민합니다.

---

## Tech Stack

### Languages
![C#](https://img.shields.io/badge/C%23-512BD4?style=flat&logo=dotnet&logoColor=white)
![Java](https://img.shields.io/badge/Java-007396?style=flat&logo=openjdk&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat&logo=javascript&logoColor=black)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-4479A1?style=flat&logo=mysql&logoColor=white)

### Frontend / Backend
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat&logo=css3&logoColor=white)
![Node.js](https://img.shields.io/badge/Node.js-339933?style=flat&logo=node.js&logoColor=white)
![Express](https://img.shields.io/badge/Express-000000?style=flat&logo=express&logoColor=white)

### Tools / Infra
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=flat&logo=mysql&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)
![Nginx](https://img.shields.io/badge/Nginx-009639?style=flat&logo=nginx&logoColor=white)
![WinForms](https://img.shields.io/badge/WinForms-512BD4?style=flat&logo=windows&logoColor=white)

---

## Featured Projects

### 1. War Archive

[Repository](https://github.com/kenitoa/War-Achive)  
[Live Site](https://war-archive.tail498403.ts.net/)

전쟁 역사 데이터를 체계적으로 정리하고 탐색할 수 있도록 만든 풀스택 웹 아카이브 프로젝트입니다.  
고대부터 현대까지의 전쟁, 인물, 전략, 사료, 전장, 무기 데이터를 JSON 기반으로 관리하고,  
프론트엔드에서는 이를 동적으로 렌더링하여 검색과 필터링이 가능한 아카이브 형태로 제공합니다.

**주요 기능**

- 전쟁 개요, 인물 열전, 전략/전술, 사료/문서, 전장 지도, 무기/장비 등 7개 카테고리 구성
- JSON 데이터 기반 클라이언트 사이드 렌더링
- 시대별, 지역별, 키워드 기반 필터링
- 목록 페이지와 상세 페이지 분리
- Node.js + Express 기반 REST API
- MySQL 기반 사용자, 인증, 세션 관리
- Docker Compose를 활용한 MySQL, Backend, Nginx 구성
- Synology NAS 환경 배포

**기술 스택**

`HTML5` `CSS3` `Vanilla JavaScript` `Node.js` `Express` `MySQL` `Docker` `Nginx`

**포트폴리오 포인트**

이 프로젝트는 단순한 정적 페이지가 아니라, 대량의 역사 데이터를 구조화하고 탐색 가능한 서비스로 만든 프로젝트입니다.  
프론트엔드 화면 구성, 데이터 스키마 설계, 백엔드 API, 인증, Docker 기반 배포까지 전체 흐름을 경험했습니다.

---

### 2. MuWorld

[Repository](https://github.com/kenitoa/MuWorld)

C# WinForms 기반의 4-key 리듬 게임 프로젝트입니다.  
WAV 파일을 분석하여 자동으로 비트를 감지하고, 채보를 생성한 뒤 BMS 형식으로 저장 및 로드할 수 있도록 구현했습니다.  
게임 화면은 WinForms의 GDI+ Custom Rendering을 활용해 직접 렌더링했습니다.

**주요 기능**

- 4-key 리듬 게임 플레이
- WAV 오디오 분석 기반 비트 감지
- 난이도별 자동 채보 생성
- BMS 포맷 저장 및 로드
- 시간 차이 기반 판정 시스템
- 점수, 콤보, 판정 통계 관리
- 업적 시스템 및 플레이 기록 저장
- Normal, Blind, Fog 시각 모드
- GDI+ 기반 직접 렌더링
- FPS 설정, VSync, Delta Time 기반 루프 관리

**기술 스택**

`C#` `.NET 9.0` `Windows Forms` `GDI+` `System.Text.Json` `P/Invoke` `BMS`

**포트폴리오 포인트**

게임 루프, 입력 처리, 오디오 재생, 판정 로직, 채보 생성, 렌더링 최적화까지 직접 구현한 프로젝트입니다.  
특히 음원 분석 결과를 게임 데이터로 변환하는 흐름과, 시간 기반 판정 시스템을 설계한 점이 핵심입니다.

---

### 3. Small Project

[Repository](https://github.com/kenitoa/small-project)

Java로 만든 소규모 데스크톱 프로젝트들을 정리한 저장소입니다.  
각 프로젝트는 독립된 폴더로 구성되어 있으며, Java Swing을 활용한 GUI 프로그램 구현 경험을 담고 있습니다.

#### Cozy Note

메모장, Lo-fi 음악 플레이어, 방 꾸미기 미니게임을 결합한 Java Swing 데스크톱 앱입니다.  
작업 중 메모 작성, 음악 감상, 짧은 휴식용 인터랙션을 하나의 프로그램 안에서 사용할 수 있도록 구성했습니다.

**핵심 포인트**

- Java Swing 기반 GUI 구성
- 메모 작성 기능
- 음악 플레이어 기능
- 방 꾸미기 형태의 미니게임 요소
- 데스크톱 앱 사용자 흐름 설계

#### Math Calculator

미분과 적분 계산 과정을 확인할 수 있는 Java Swing 기반 계산기입니다.  
다항식 계수를 입력하고 미분, 적분, 곱 미분, 몫 미분, 부분적분, 치환적분 등의 계산 흐름을 확인할 수 있도록 만들었습니다.

**핵심 포인트**

- 수학 계산 로직 구현
- Java Swing 기반 입력/출력 UI
- 계산 과정 시각화
- 함수형 문제를 코드 구조로 분해하는 연습

**기술 스택**

`Java` `Java Swing`

**포트폴리오 포인트**

GUI 프로그램을 직접 구성하면서 이벤트 처리, 입력값 검증, 화면 흐름, 계산 로직 분리 등을 연습한 저장소입니다.

---

### 4. Mini Project

[Repository](https://github.com/kenitoa/mini-project)

작은 규모의 로직 구현과 알고리즘 실험을 기록하는 저장소입니다.  
하나의 큰 결과물보다, 다양한 아이디어를 빠르게 구현해보며 문제 해결력을 키우는 데 초점을 두고 있습니다.

**주요 내용**

- 간단한 알고리즘 구현
- 로직 중심 미니 프로젝트
- Python 기반 실험 코드
- 문제 해결 과정 기록
- 작은 아이디어를 실제 동작하는 프로그램으로 구현

**기술 스택**

`Python`

**포트폴리오 포인트**

기초 로직 구현, 알고리즘 사고, 프로그램 구조화 연습을 보여주는 학습형 저장소입니다.  
작은 단위의 구현을 반복하면서 문제를 코드로 풀어내는 습관을 기록하고 있습니다.

---

## Project Summary

| Project | Type | Main Tech | Description |
|---|---|---|---|
| [War Archive](https://github.com/kenitoa/War-Achive) | Full-stack Web | HTML, CSS, JS, Node.js, Express, MySQL, Docker | 전쟁 역사 데이터를 구조화한 웹 아카이브 |
| [MuWorld](https://github.com/kenitoa/MuWorld) | Desktop Game | C#, .NET, WinForms, GDI+ | WAV 분석과 자동 채보 생성을 포함한 4-key 리듬 게임 |
| [small-project](https://github.com/kenitoa/small-project) | Desktop Apps | Java, Swing | Cozy Note와 Math Calculator 등 Java GUI 프로젝트 모음 |
| [mini-project](https://github.com/kenitoa/mini-project) | Practice Projects | Python | 알고리즘과 로직 구현 중심의 미니 프로젝트 모음 |

---

## What I Focus On

- 아이디어를 실제 동작하는 프로그램으로 구현하기
- 기능을 작은 단위로 나누고 구조화하기
- 사용자 흐름을 고려한 화면과 기능 설계
- 데이터 구조와 파일 구조를 명확하게 관리하기
- 직접 구현을 통해 원리를 이해하기
- 프로젝트마다 배운 점과 개선점을 문서화하기

---

## GitHub Stats

<div align="center">

![GitHub Stats](https://github-readme-stats.vercel.app/api?username=kenitoa&show_icons=true&theme=tokyonight)

![Top Languages](https://github-readme-stats.vercel.app/api/top-langs/?username=kenitoa&layout=compact&theme=tokyonight)

</div>

---

## Contact

- GitHub: [github.com/kenitoa](https://github.com/kenitoa)

---

<div align="center">

### Thanks for visiting my portfolio.

</div>