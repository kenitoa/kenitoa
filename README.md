<!-- KENITOA / NEON ATLAS. Motion panels are illustrations; project evidence is linked below. -->

![KENITOA — NEON ATLAS. 시안·보라·핑크 파형이 움직이는 타이틀.](https://capsule-render.vercel.app/api?type=waving&color=0:06B6D4,50:7C3AED,100:EC4899&height=300&section=header&text=KENITOA&fontSize=110&fontColor=FFFFFF&animation=fadeIn&fontAlignY=40&desc=NEON%20ATLAS&descSize=36&descAlignY=65)

<p align="center">
  <strong>AI를 도구로 연결하고, 아이디어를 사용할 수 있는 경험으로 만듭니다.</strong><br>
  로컬 AI 에이전트, 데스크톱 도구, 웹 3D와 게임을 개발합니다.
</p>

<div align="center">

![Local AI Systems · Tools for Everyday Work · Interactive Worlds 순서로 나타나는 소개.](https://readme-typing-svg.demolab.com?font=Fira+Code&weight=500&size=27&duration=2600&pause=1400&color=C4B5FD&background=0B1020&center=true&vCenter=true&width=540&height=55&lines=Local+AI+Systems;Tools+for+Everyday+Work;Interactive+Worlds&repeat=true)

</div>

<p align="center"><strong>LOCAL AI &nbsp; / &nbsp; DESKTOP TOOLS &nbsp; / &nbsp; WEB 3D &nbsp; / &nbsp; GAMES</strong></p>

[대표작](#selected-work) · [추가 프로젝트](#more-projects) · [개발 방식](#how-i-build) · [기술](#tools-in-practice) · [전체 프로젝트](#project-archive) · [개발 기록](https://kiseno3231.tistory.com/)

---

## Selected Work

**공간을 탐색하고, 정보를 연결하고, 음악을 플레이합니다.**

### 01 / 3D Campus

[![3D CAMPUS — 건물과 공간을 연결하는 탐색 경험을 표현한 움직이는 파형. 실제 화면은 아래에서 펼쳐 볼 수 있습니다.](https://capsule-render.vercel.app/api?type=waving&color=0:0891B2,50:6D28D9,100:7C3AED&height=190&section=header&text=3D%20CAMPUS&fontSize=64&fontColor=FFFFFF&animation=fadeIn&fontAlignY=42)](https://github.com/kenitoa/-3D-)

**공간을 둘러보며 정보를 찾는 캠퍼스 인터페이스.**

Babylon.js 3D 장면에 건물·공간 검색과 상세 정보를 연결했습니다. 지도에서 살펴보는 경험과 자료를 검토하고 공개하는 흐름을 함께 설계합니다.

- **사용 흐름** — 캠퍼스 탐색 → 건물·공간 검색 → 상세 정보와 출처 확인.
- **설계 포인트** — 3D·2D·문자 탐색과 정보 패널을 연결하고, 자료의 승인·공개 상태를 구분합니다.

`TypeScript` `Babylon.js` `Node.js` `SQLite / libSQL`

[코드 보기 ↗](https://github.com/kenitoa/-3D-) · [구현·검증 기록 ↗](https://github.com/kenitoa/-3D-/blob/main/docs/validation.md)

<details>
<summary>실제 캠퍼스 화면과 확인 범위 펼치기</summary>

![공개 QA 기록의 실제 3D 캠퍼스와 탐색 패널 화면.](https://raw.githubusercontent.com/kenitoa/-3D-/main/evidence/screenshots/refinement-live-desktop.png)

[모바일 QA 화면 보기](https://raw.githubusercontent.com/kenitoa/-3D-/main/evidence/screenshots/refinement-live-mobile.png)

공개 소스와 QA 기록에 근거한 소개입니다. 정밀 측량 모델, 학교 전체 API 연동, 현장 접근성·실기기 XR 검증은 별도의 확인 범위입니다.

</details>

---

### 02 / AI Librarian Agent

<div align="center">

[![AI LIBRARIAN — 도서 검색, 이용자별 기억, 근거 기반 답변을 나타내는 애니메이션.](https://readme-typing-svg.demolab.com?font=Fira+Code&weight=500&size=26&duration=2200&pause=1500&color=67E8F9&background=0B1020&center=true&vCenter=true&multiline=true&width=480&height=132&lines=SEARCH+%3E+TOOL+EVIDENCE;USER+MEMORY+%3E+CONTEXT;GROUNDED+REPLIES&repeat=true)](https://github.com/kenitoa/AI-Librarian-Agent)

</div>

**검색 결과와 이용자별 기억을 연결하는 로컬 도서관 에이전트.**

수업 자료의 도서 목록을 검색하고, 이용자의 독서 선호를 기억하며, 도구 결과에 근거해 답합니다. 입력 가드레일과 최종 응답 검증을 대화 흐름에 연결했습니다.

- **사용 흐름** — 질문 → 도서 검색 도구 → 이용자별 문맥 → 근거 기반 안내.
- **설계 포인트** — 모델의 도구 선택과 필수 검증 호출을 구분하고, 제공되지 않은 정보는 명확히 안내합니다.

`Python` `LangChain / LangGraph` `Ollama / Qwen` `Scoped Memory`

[▶ 실제 CMD 데모](https://youtu.be/6JLd9IuQius) · [코드 보기 ↗](https://github.com/kenitoa/AI-Librarian-Agent) · [실모델 검증 기록 ↗](https://github.com/kenitoa/AI-Librarian-Agent/blob/main/evidence/live-final.json)

<details>
<summary>데이터·메모리·검증 범위 펼치기</summary>

공개 README에는 단위 검사와 실제 로컬 모델 시나리오의 실행 기록이 있습니다. 위 데모와 기록은 해당 저장소의 검증 근거이며, 프로필을 읽는 시점의 모델 서버 상태를 뜻하지 않습니다.

검색 대상은 수업 자료에 제공된 11권의 제목·저자입니다. 실제 도서관 API·대출 처리·RAG·영구 DB는 포함하지 않으며, 이용자별 기억은 프로세스 종료 시 소멸합니다.

</details>

---

### 03 / MuWorld

[![MUWORLD — 보라와 핑크 파형이 움직이는 리듬게임 타이틀. 실제 곡 선택 화면은 아래에서 펼쳐 볼 수 있습니다.](https://capsule-render.vercel.app/api?type=waving&color=0:4F46E5,50:9333EA,100:EC4899&height=200&section=header&text=MUWORLD&fontSize=76&fontColor=FFFFFF&animation=twinkling&fontAlignY=42)](https://github.com/kenitoa/MuWorld)

**음악을 분석하고, 채보를 만들고, 직접 플레이하는 리듬게임.**

C#으로 만든 Windows 리듬게임입니다. 다양한 키 구성과 노트 유형에 입력 보정·리플레이·차트 편집을 연결해, 곡을 준비하고 플레이를 돌아보는 과정을 구성했습니다.

- **사용 흐름** — 곡 선택 → 채보 준비·난이도 선택 → 플레이 → 기록·리플레이 확인.
- **설계 포인트** — 음악 분석과 패턴 생성, 타이밍 설정과 편집 기능을 함께 다룹니다.

`C#` `.NET 9` `Windows Forms` `Rhythm Game`

[코드 보기 ↗](https://github.com/kenitoa/MuWorld) · [품질 검증 기록 ↗](https://github.com/kenitoa/MuWorld/blob/main/front%20interface/docs/quality-validation.md)

<details>
<summary>실제 곡 선택 화면과 확인 범위 펼치기</summary>

![MuWorld 저장소에 공개된 실제 네온 계열 곡 선택 UI.](https://raw.githubusercontent.com/kenitoa/MuWorld/main/media/image.png)

공개 소스·화면·품질 문서를 바탕으로 소개합니다. 자동 검사와 실제 청감·사람 플레이·모든 코덱 및 기기에서의 확인은 서로 다른 검증입니다.

</details>

---

## More Projects

**일상에서 사용하는 도구부터, 직접 만드는 작업공간까지.**

### Local AI / 로컬 모델을 하나의 Windows 작업공간으로

모델 선택·대화·마켓·로그 확인을 데스크톱 인터페이스에 모았습니다. WPF의 WebView2 화면과 ASP.NET API, Ollama 실행 계층을 연결합니다.

`C#` `ASP.NET Core` `WPF / WebView2` `Ollama`

[코드·실행 방법 ↗](https://github.com/kenitoa/local-ai)

<details>
<summary>초기 UI 화면과 현재 MVP 범위</summary>

![Local AI 공개 웹 UI 소스를 연 초기 화면. 실제 모델 응답이나 WPF 통합 실행의 증거는 아닙니다.](https://raw.githubusercontent.com/kenitoa/kenitoa/main/assets/local-ai.png)

현재 공개 문서는 Ollama adapter, 공통 Expert 구조, 규칙 기반 라우팅, Single/Pipeline 기반을 MVP로 설명합니다. 병렬 실행 고도화·Judge 평가·자동 fallback은 향후 확장 영역입니다. 위 이미지는 초기 웹 UI이며 실제 모델 추론을 시연한 화면은 아닙니다.

</details>

### Automade / 화면 편집에서 실행 가능한 웹 결과물까지

캔버스와 속성 패널에서 화면을 편집하고 반응형 미리보기를 확인합니다. 프로젝트 저장·복구와 소스·빌드·독립 실행 패키지 생성을 연결한 웹 제작 도구입니다.

`React` `TypeScript` `Vite / Node.js` `SQLite`

[코드·구현 범위 ↗](https://github.com/kenitoa/automade-web-site)

### CozyNote / 기록과 음악, 작은 카페가 함께 있는 작업공간

JavaFX로 만든 카페·음악·메모 작업공간입니다. 리치 텍스트 메모의 검색·분류·자동 저장에 휴지통·이전 버전·백업 복원을 연결합니다.

`Java 21` `JavaFX` `SQLite` `Desktop App`

[코드 보기 ↗](https://github.com/kenitoa/CozyNote) · [카페 개편 기록 ↗](https://github.com/kenitoa/CozyNote/blob/main/docs/cafe-redesign.md)

### Beyond the Showcase

- **[warsachive](https://github.com/kenitoa/warsachive)** — 역사 자료를 검색·연표·주제로 탐색하는 웹·모바일 아카이브. 주장별 출처와 콘텐츠 검수 흐름을 함께 다룹니다.
- **[Project-virtual-AI](https://github.com/kenitoa/Project-virtual-AI)** — 협업 중인 가상 AI 캐릭터 제어 기반. 공개 `main`의 비동기 대기열·취소·늦은 응답 차단·제한된 대화 기록을 중심으로 소개합니다. 음성·아바타·방송 통합은 공개 문서의 후속 범위입니다.

---

## How I Build

**화면에서 이해할 수 있는 흐름을 만들고, 코드에서 확인할 수 있는 근거를 남깁니다.**

**01 / 실행 상태를 드러냅니다.**
Local AI의 실행 로그와 Project-virtual-AI의 요청·취소 흐름처럼, 사용자가 진행과 실패를 이해할 수 있는 경계를 만듭니다.

**02 / 작업을 보존합니다.**
CozyNote와 Automade에서 저장·복원·실패 상태를 작업 흐름에 포함합니다. 작성한 내용과 다시 돌아오는 경험을 함께 다룹니다.

**03 / 근거와 확인 범위를 남깁니다.**
AI Librarian의 도구 결과, 3D Campus의 공간 자료, warsachive의 출처를 구분합니다. 구현·검증 기록·추가 확인이 필요한 영역을 각각 설명합니다.

---

## Tools in Practice

**기술은 실제 프로젝트에서 맡은 역할로 소개합니다.**

| 분야 | 기술과 사용한 곳 |
| :--- | :--- |
| **AI & Language** | **Python · LangChain · LangGraph · Ollama** — AI Librarian의 도구 호출·문맥·검증, 한국어 질문 변환 도구의 규칙 처리 |
| **Windows & Desktop** | **C# · ASP.NET · WPF · WebView2 · JavaFX** — Local AI의 실행 계층, MuWorld의 리듬게임, CozyNote의 작업공간 |
| **Web & Creation** | **TypeScript · React · Vite · Next.js · Node.js** — Automade의 시각 편집·패키지 생성, warsachive의 자료 탐색 |
| **Space & Data** | **Babylon.js · SQLite · SQL · PowerShell** — 캠퍼스 3D, 로컬 데이터 저장, 언어 규칙과 문서 기반 폴더 생성 |

<details>
<summary>다음에 탐구할 질문 / Planned</summary>

아래 항목은 현재 구현 완료가 아닌 향후 탐구 방향입니다.

- **Local AI** — 도구 실행 범위와 실패 상태를 인터페이스에서 어떻게 전달할까?
- **MCP 도구 연결** — 파일 검색과 폴더 생성 미리보기를 재사용 가능한 도구로 연결할 수 있을까?
- **AI 평가·실행 기록** — 모델·입력·실패·취소·응답 시간을 함께 비교하는 기록을 어떻게 만들까?
- **브라우저 그래픽** — 3D Campus의 기기별 로딩·탐색 성능을 측정하고 WebGPU 채택 효과를 비교할 수 있을까?

</details>

---

## Project Archive

**공개 프로젝트를 관심 있는 분야에서 찾아보세요.**

<details>
<summary>AI & Language / 도구 호출·모델 실행·언어 규칙</summary>

- [AI-Librarian-Agent](https://github.com/kenitoa/AI-Librarian-Agent) — 로컬 도서 검색 에이전트, 이용자별 메모리와 근거 기반 회신.
- [local-ai](https://github.com/kenitoa/local-ai) — Windows 로컬 AI 데스크톱과 모델 실행 계층.
- [Project-virtual-AI](https://github.com/kenitoa/Project-virtual-AI) — **협업·진행 중.** 비동기 캐릭터 제어와 요청 취소 기반.
- [text-to-make-question](https://github.com/kenitoa/text-to-make-question) — 한국어 조사·어미·SQL 규칙으로 일반 발화를 질문으로 변환. 실제 STT 엔진이나 LLM 생성기와 구분합니다.

</details>

<details>
<summary>Tools & Workspaces / 메모·제작·검색·자동화</summary>

- [CozyNote](https://github.com/kenitoa/CozyNote) — 카페·음악·메모와 저장·복구를 다루는 JavaFX 앱.
- [automade-web-site](https://github.com/kenitoa/automade-web-site) — 웹 시각 편집과 실행 패키지 생성.
- [PC-search-all-file](https://github.com/kenitoa/PC-search-all-file) — 드라이브 확인·파일 색인·파일명과 경로 검색을 분리한 Python 도구.
- [auto-folder](https://github.com/kenitoa/auto-folder) — 문서의 명시적 트리와 제목 규칙을 폴더 구조로 변환하는 PowerShell 도구.

</details>

<details>
<summary>Interactive Worlds / 공간·음악·역사 자료 탐색</summary>

- [-3D- / 3D Campus](https://github.com/kenitoa/-3D-) — 캠퍼스 공간과 자료를 탐색하는 Babylon.js 인터페이스.
- [MuWorld](https://github.com/kenitoa/MuWorld) — 음악 분석·채보·플레이·편집을 연결한 Windows 리듬게임.
- [warsachive](https://github.com/kenitoa/warsachive) — 출처와 검수 흐름을 포함한 역사 자료 웹·모바일 아카이브.

</details>

<details>
<summary>Learning, Collaboration & Profile / 학습·포크·기타 공개 저장소</summary>

- [mini-project](https://github.com/kenitoa/mini-project) — 알고리즘 문서와 Python 학습 실험. 완성 서비스와 구분한 학습 아카이브입니다.
- [-](https://github.com/kenitoa/-) — **[hhs120121-gif/-](https://github.com/hhs120121-gif/-)의 포크.** 구체적인 본인 기여 범위를 확인하기 전에는 독자 대표작으로 소개하지 않습니다.
- [War-Achive](https://github.com/kenitoa/War-Achive) — 설명은 있으나 2026-10-16 확인 당시 공개 파일 목록이 비어 있는 저장소입니다. `warsachive`와 별개로 구분합니다.
- [kenitoa](https://github.com/kenitoa/kenitoa) — 이 프로필과 공개 프로젝트 메타데이터 유지관리.

</details>

<details>
<summary>공개 저장소 메타데이터 / 기존 자동 갱신 영역</summary>

아래 날짜는 저장소 메타데이터의 확인일·push 날짜이며 기능 출시일이나 운영 검증일이 아닙니다. 자동 갱신 대상은 아래 세 저장소입니다.

<!-- metadata:start -->
확인일: 2026-10-19 (UTC)

- [local-ai](https://github.com/kenitoa/local-ai) · 저장소 push: 2026-06-02 · 공개 릴리스 없음
- [CozyNote](https://github.com/kenitoa/CozyNote) · 저장소 push: 2026-09-29 · 공개 릴리스 없음
- [-3D-](https://github.com/kenitoa/-3D-) · 저장소 push: 2026-10-09 · 공개 릴리스 없음
<!-- metadata:end -->

</details>

<details>
<summary>프로필의 화면·모션·소개 기준</summary>

모션 패널은 프로젝트의 주제와 흐름을 표현하는 그래픽입니다. 실제 프로젝트 화면·동작 근거는 각 프로젝트의 펼치기 영역과 코드·데모·검증 문서에서 확인할 수 있습니다.

소개는 공개 저장소와 문서 기준입니다. 별도 표기가 없는 외부 API·계정·결제·장비·운영 배포의 성공을 의미하지 않습니다. 모션을 읽지 않아도 제목·설명·링크로 같은 프로젝트를 탐색할 수 있습니다.

타이틀과 파형은 [Capsule Render](https://github.com/kyechan99/capsule-render), 타이핑 모션은 [Readme Typing SVG](https://github.com/DenverCoder1/readme-typing-svg)를 사용합니다. 외부 그래픽 서비스의 응답 상태에 따라 표시가 달라질 수 있습니다.

</details>

---

## Find Me

**코드에서 시작해, 만드는 과정까지 살펴보세요.**

[GitHub / 공개 저장소 ↗](https://github.com/kenitoa?tab=repositories&type=public) · [Tistory / 개발 기록 ↗](https://kiseno3231.tistory.com/)

프로젝트 질문과 재현 가능한 문제 제보는 해당 저장소의 Issues가 열려 있는 경우 그곳에 남겨주세요.

<p align="center"><strong>KENITOA</strong><br>Software for work, thought, and play.</p>

![시안·보라·핑크 파형으로 마무리하는 NEON ATLAS 푸터.](https://capsule-render.vercel.app/api?type=waving&color=0:06B6D4,50:7C3AED,100:EC4899&height=100&section=footer)
