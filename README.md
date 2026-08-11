<p align="center">
  <img src="./assets/lab-hero.svg" width="100%" alt="KENITOA portfolio flow hero">
</p>

<div align="center">

# KENITOA

### 포트폴리오처럼 읽히고, 플로우차트처럼 따라갈 수 있는 작업 기록

<a href="https://github.com/kenitoa?tab=repositories"><strong>전체 공개 레포 보기</strong></a>

</div>

```text
[idea] -> [working interface] -> [local proof] -> [public record]
```

저는 막연한 아이디어를 실제로 눌러보고 실행할 수 있는 시스템으로 바꿉니다.
지금 공개된 작업들은 `로컬 AI`, `업무 자동화`, `공간/기록 아카이브`라는 세 흐름으로 이어집니다.

## 01. Portfolio Flow

<p align="center">
  <img src="./assets/research-floorplan.svg" width="100%" alt="KENITOA repository routing map">
</p>

| Flow | Direction | Repositories |
| --- | --- | --- |
| `LOCAL INTELLIGENCE` | PC 안에서 실행되는 AI와 언어 처리 | [`local-ai`](https://github.com/kenitoa/local-ai) -> [`text-to-make-question`](https://github.com/kenitoa/text-to-make-question) |
| `HUMAN WORKFLOW` | 반복 작업을 도구화하고 안전하게 실행 | [`CozyNote`](https://github.com/kenitoa/CozyNote) -> [`auto-folder`](https://github.com/kenitoa/auto-folder) -> [`PC-search-all-file`](https://github.com/kenitoa/PC-search-all-file) -> [`automade-web-site`](https://github.com/kenitoa/automade-web-site) |
| `SPATIAL ARCHIVE` | 게임, 3D 공간, 역사 기록을 탐색 화면으로 구성 | [`MuWorld`](https://github.com/kenitoa/MuWorld) -> [`-3D-`](https://github.com/kenitoa/-3D-) -> [`War-Achive`](https://github.com/kenitoa/War-Achive) -> [`warsachive`](https://github.com/kenitoa/warsachive) |
| `BASELINE` | 작은 로직 실험과 프로필 인덱스 | [`mini-project`](https://github.com/kenitoa/mini-project) -> [`kenitoa`](https://github.com/kenitoa/kenitoa) |

## 02. Project Nodes

<table>
  <tr>
    <td width="33%">
      <h3>LOCAL AI</h3>
      <p><a href="https://github.com/kenitoa/local-ai"><strong>local-ai</strong></a></p>
      <p>Windows PC에서 로컬 AI 채팅, 모델 선택, Ollama 실행, expert 조합, 로그 확인을 한 화면으로 묶는 데스크톱형 AI 런타임.</p>
      <sub>C# / ASP.NET / WPF / Ollama</sub>
    </td>
    <td width="33%">
      <h3>QUESTION ENGINE</h3>
      <p><a href="https://github.com/kenitoa/text-to-make-question"><strong>text-to-make-question</strong></a></p>
      <p>평소 발화에서 핵심어를 찾고 그 단어를 중심으로 다음 질문을 만드는 한국어 질문 생성 도구.</p>
      <sub>Python / SQLite rules / STT bridge</sub>
    </td>
    <td width="33%">
      <h3>LOGIC SKETCHBOOK</h3>
      <p><a href="https://github.com/kenitoa/mini-project"><strong>mini-project</strong></a></p>
      <p>작은 알고리즘, 로직 구현, 학습용 프로그램을 독립 예제로 모아 둔 실험장.</p>
      <sub>Python / logic practice</sub>
    </td>
  </tr>
  <tr>
    <td width="33%">
      <h3>NOTE SPACE</h3>
      <p><a href="https://github.com/kenitoa/CozyNote"><strong>CozyNote</strong></a></p>
      <p>블록형 메모, 자동 저장, 검색, 체크리스트 보상, 음악 위젯을 결합한 로컬 메모 작업공간.</p>
      <sub>Java / JavaFX / SQLite</sub>
    </td>
    <td width="33%">
      <h3>FOLDER BUILDER</h3>
      <p><a href="https://github.com/kenitoa/auto-folder"><strong>auto-folder</strong></a></p>
      <p>Markdown, TXT, DOCX, HWPX 문서의 제목과 트리 구조를 읽어 바탕화면 폴더 구조로 변환하는 자동화 도구.</p>
      <sub>PowerShell / dry-run / path validation</sub>
    </td>
    <td width="33%">
      <h3>FILE INDEX</h3>
      <p><a href="https://github.com/kenitoa/PC-search-all-file"><strong>PC-search-all-file</strong></a></p>
      <p>드라이브 확인, 파일 개수 계산, 색인 생성, 빠른 검색을 분리한 로컬 파일 검색 도구.</p>
      <sub>Python / indexing / filesystem safety</sub>
    </td>
  </tr>
  <tr>
    <td width="33%">
      <h3>VISUAL BUILDER</h3>
      <p><a href="https://github.com/kenitoa/automade-web-site"><strong>automade-web-site</strong></a></p>
      <p>폼, 표, 차트, 탭, 네비게이션을 캔버스에 배치하고 실행 가능한 웹사이트 폴더로 저장하는 비주얼 빌더.</p>
      <sub>JavaScript / canvas / export</sub>
    </td>
    <td width="33%">
      <h3>RHYTHM WORLD</h3>
      <p><a href="https://github.com/kenitoa/MuWorld"><strong>MuWorld</strong></a></p>
      <p>내 PC의 음악과 생성된 패턴으로 플레이하는 Windows 로컬 리듬게임.</p>
      <sub>C# / rhythm game / local play</sub>
    </td>
    <td width="33%">
      <h3>3D CAMPUS</h3>
      <p><a href="https://github.com/kenitoa/-3D-"><strong>-3D-</strong></a></p>
      <p>한신대학교 경기캠퍼스를 3D 지형, 건물, 동선, 내부 평면 패널로 탐색하는 Babylon.js 정적 웹사이트.</p>
      <sub>JavaScript / Babylon.js / static web</sub>
    </td>
  </tr>
  <tr>
    <td width="33%">
      <h3>ARCHIVE SOURCE</h3>
      <p><a href="https://github.com/kenitoa/War-Achive"><strong>War-Achive</strong></a></p>
      <p>전쟁사 기록을 JSON 양식과 기여 흐름으로 정리하려는 원본 아카이브 프로젝트.</p>
      <sub>archive concept / historical records</sub>
    </td>
    <td width="33%">
      <h3>ARCHIVE FRONT</h3>
      <p><a href="https://github.com/kenitoa/warsachive"><strong>warsachive</strong></a></p>
      <p>GitHub Pages에 배포되는 전쟁사 정적 아카이브 프런트엔드. 콘텐츠 인덱스, 상세 페이지, sitemap을 자동 생성합니다.</p>
      <sub>Next.js / GitHub Pages / static content</sub>
    </td>
    <td width="33%">
      <h3>INDEX PAGE</h3>
      <p><a href="https://github.com/kenitoa/kenitoa"><strong>kenitoa</strong></a></p>
      <p>현재 보고 있는 프로필 README. 공개 작업물을 빠르게 훑는 포트폴리오 플로우보드입니다.</p>
      <sub>GitHub profile README</sub>
    </td>
  </tr>
</table>

## 03. Working Rules

```text
local-first   개인 데이터와 실행 흐름은 가능한 한 사용자 PC 가까이에 둡니다.
visible-flow  라우팅, 파일, 로그, 실패 경로를 숨기지 않습니다.
small-proof   큰 말보다 먼저 작게 작동하는 흐름을 만듭니다.
public-map    프로젝트마다 의도와 구조를 읽을 수 있게 남깁니다.
```

## 04. Now Building

자동화, 발행, 아카이브 인터페이스를 연결해서 정보를 수집하고 검증한 뒤
사용자가 이해할 수 있는 화면으로 보여주는 시스템을 만들고 있습니다.

<p align="center">
  <a href="https://github.com/kenitoa?tab=repositories">
    <img src="./assets/lab-exit.svg" width="100%" alt="Open Kenitoa public repository map">
  </a>
</p>
