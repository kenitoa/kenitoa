# Profile evidence & maintenance

확인 기준: 2026-09-27. 프로필은 공개 저장소의 문서와 자료를 바탕으로 편집했습니다.

## 자료 출처

| 자료 | 출처와 확인 범위 |
| --- | --- |
| Local AI 설명 | https://github.com/kenitoa/local-ai — README의 현재 MVP 및 확장 영역 구분 |
| Local AI 이미지 | 해당 저장소 `Cloud AI interface/apps/web/`의 공개 소스를 로컬 정적 서버로 열어 캡처. 백엔드와 모델은 실행하지 않음 |
| CozyNote 설명 | https://github.com/kenitoa/CozyNote — README의 현재 구현 범위와 데이터 모델 |
| CozyNote 이미지 | 저장소 README의 공개 첨부 이미지 https://github.com/user-attachments/assets/5d4def09-a1f9-473d-bc5e-c9c37150af46 — 직접 재실행한 캡처가 아님 |
| Campus 이미지 | https://github.com/kenitoa/-3D- — 공개 정적 소스를 로컬 브라우저에서 렌더링하고 건물 상세 패널을 확인 |
| 기타 프로젝트 | 각 공개 저장소의 설명 및 README. War-Achive는 README 조회가 404이므로 저장소 소개만 사용 |
| 개발 기록·소셜 | https://github.com/kenitoa 에 공개된 링크 |

## 표현 기준

- 현재 기능 설명은 공개 문서 기준이며 모든 앱의 기능 테스트 통과를 의미하지 않습니다.
- Local AI의 병렬 실행·Judge 고도화·fallback 확장은 완료 기능으로 표기하지 않습니다.
- MCP·도구 호출 확장·평가 문서·WebGPU 검토는 Planned입니다. 실제 작업 근거가 생길 때 상태를 올립니다.
- 최근 변화의 날짜는 문서 확인일이며 기능 출시일이 아닙니다.
- 성능 수치, 연락 이메일, 실제 공개 데모 주소를 추정해서 추가하지 않습니다.
- 사진 위에 기능을 만들어 넣지 않습니다. 표지의 장식과 프로젝트 캡처를 구분합니다.

## 유지 관리

`python scripts/refresh-profile.py`는 공개 저장소 push 날짜와 릴리스만 갱신합니다. API 조회가 하나라도 실패하면 README를 쓰지 않습니다. `.github/workflows/profile.yml`은 기본 브랜치에서 매주 월요일과 수동 실행 시 동작합니다. 워크플로는 저장소 반영 및 Actions 활성화 후 실행되며, 보호 브랜치가 직접 push를 막으면 정책을 우회하지 않고 실패합니다.

대표 프로젝트 소개와 Recent Updates는 직접 편집합니다. 업데이트 시 문서 링크·이미지 출처·실제 구현 범위를 함께 확인합니다. 자동 날짜는 기능 출시일이나 검증 완료일로 사용하지 않습니다.

`python scripts/check-profile.py`는 이미지·문서 파일, 내부 섹션 이동, 외부 링크 응답을 검사합니다. 외부 페이지 내부 앵커의 의미나 실제 앱 실행은 별도로 확인해야 합니다. 워크플로에서도 링크 검사를 실행하며 실패는 Actions에 표시됩니다.

## 프로필과 Pages의 경계

현재 결과물은 `kenitoa/kenitoa`의 루트 README용입니다. JavaScript 검색·필터·3D 임베드 등은 별도 Pages가 필요하며 README에는 이미지와 링크를 제공합니다. 이번 범위에 별도 사이트 배포는 포함하지 않습니다.

## 반영 항목

- 정체성, 한국어 소개와 영문 보조 문구, 상단 이동 링크.
- 화면 자산을 포함한 커버와 단일 열 대표작 세 개.
- 전체 공개 프로젝트의 분야별 목록 및 설계 판단 세 가지.
- 기술과 실제 사용처의 연결, 2026 기술 계획과 상태 기준.
- 의미 있는 기록 세 개, 메타데이터 자동화 및 실패 시 기존 본문 보존.
- 개발 기록과 공개 소셜, 상세 설명 접기, 이미지 대체 텍스트.
- 실제 화면 출처와 검증 한계. GIF는 정적 이미지로 충분한 현재 구성에서 추가하지 않음.

원본 `version/README(1.0).md`는 이전 버전으로 보존합니다.
