SudokuGame   Generator & Solver (GUI)
===
본 프로젝트는 GUI 기반 프로그램으로 로컬 환경에서 실행해야 합니다.<br>
GitHub Codespaces 등 원격 환경에서는 GUI 디스플레이가 지원되지 않아 실행되지 않습니다.
---
Python 기반으로 제작된 스도쿠 게임 생성 & 플레이 프로그램입니다.
오리지널 스도쿠와 크로스 스도쿠를 지원하며, Tkinter 기반의 GUI로 쉽고 직관적인 조작이 가능합니다.
난이도는 3단계로 조절 할 수 있습니다.


목차
---
1. 프로젝트 소개
2. 주요 기능
3. 실행 방법
4. 사용 기술
5. 파일별, 함수별 기능
6. 참고 자료
7. 스크린샷
8. 라이선스
9. TODO 


# 프로젝트 소개

이 프로젝트는 다음 기능들을 제공합니다

모드 / 난이도 선택 후 스도쿠 퍼즐 생성
- 모드 : 오리지널 / 크로스 스도쿠 지원
- 난이도 : 쉬움, 보통, 어려움

퍼즐 생성 시 로딩 화면 표시
- 소요 시간 10초 ~ 2분

게임 중 "정답 확인, 점검, 오답 삭제, 초기화, 숫자 표시" 기능 사용 가능

게임 완료 후 여러번 플레이 가능

GUI 기반 플레이
스레드 기반 비동기 처리로 GUI 멈춤 방지

# 주요 기능

1. 스도쿠 퍼즐 생성

* 모드 : 오리지널 / 크로스
  * 오리지널 : 일반적인 스도쿠
  * 크로스 : 대각선 제약이 포함된 스도쿠

* 난이도 : 쉬움 / 보통 / 어려움
  * 쉬움 : 초기 숫자의 개수가 43개 
  * 보통 : 초기 숫자의 개수가 38개 
  * 어려움 : 초기 숫자의 개수가 33개 

* 스도쿠 중복 해 점검
  * count_solutions를 이용해 해가 1개인 스도쿠 문제만 생성

2. GUI 인터페이스

* 메인 화면
  * 종료 : 스도쿠 게임 종료
  * 모드 선택 : 오리지널 / 크로스 선택 후 난이도 선택 가능
  * 난이도 선택 : 쉬움 / 보통 / 어려움 선택 후 스도쿠 생성
  * 로딩창 : 스도쿠 생성중 팝업

* 숫자 입력 버튼
  * 초기 숫자의 경우 버튼 비활성화
  * 버튼 클릭시 숫자 입력 창 생성

* 하단 숫자 찾기 버튼
  * 클릭시 스도쿠에 존재하는 해당 숫자를 노란 배경으로 변경
  * 다른 찾기 버튼을 누르거나 해당 버튼을 다시 누를시 비활성화
  * 모든 숫자를 찾으면 회색 배경으로 전환 (초기 배경 : 흰색)
  * 회색 배경일때 해당 숫자 삭제시 흰색 배경으로 돌아감

* 게임 중 이용 가능한 기능
  * 리셋 : 처음 상태로 전환
  * 점검 : 오답에 해당되는 숫자를 빨간색으로 전환
  * 삭제 : 오답에 해당되는 숫자 삭제 후 버튼의 배경을 빨간색으로 1초 전환
  * 정답 : 모든 숫자를 정답으로 바꾸고 오답에 해당되는 숫자를 빨간색으로 전환

* 게임 종료(스도쿠 직접 완성) 후 
  * 돌아가기 : 풀고있던 스도쿠로 복귀 
  * 종료 : 메인 화면으로 복귀 (게임 다시 플레이 가능)

3. 비동기 처리
퍼즐 생성 연산은 시간이 오래 걸릴 수 있어 별도 스레드에서 생성 후 GUI에 전달
로딩 중 프로그램이 멈추지 않음

# 실행 방법

1. 저장소 클론
git clone https://github.com/jun604/SudokuGame.git
cd sudokugame

2. Python 요구사항

 * Python 3.x

 * Tkinter 

3. 실행
python main.py

# 사용 기술

Python 3

Tkinter

Threading

백트래킹 기반 스도쿠 생성 알고리즘

# 파일별, 함수별 기능

* 스도쿠.py : 메인 파일
  * sudoku(mode, level, loading_win)
    * 스도쿠 게임 생성
    * 로딩창 닫기
    * 게임 시작
  * start_sudoku_in_thread(mode, level, loading_win) : 스레드로 sudoku 실행
  * button_mode(num) : 모드 버튼
    * 모드 선택 버튼 관리
    * 메인창 숨기기
    * 난이도 선택창 생성
  * button_lev(inter, num) : 난이도 버튼
    * 난이도 선택 버튼 관리
    * 난이도 선택창(inter) 닫기 
    * 로딩창 생성
    * start_sudoku_in_thread실행
  * button_ex : 종료 버튼
    * 메인창 닫기
  * "__main__"
    * 메인창 생성
    * 모드 버튼 및 설명 생성 (메인창)
* sudoku_inter.py : 스토쿠 게임 인터페이스 관리
  * table(self, interface, board, input_row, mode_func) : 스도쿠 보드_인터페이스 생성 및 관리
    * 3x3 보드 배경색(흰색/회색)으로 구분
    * 대각선은 초록색으로 구분
    * 공백 부분 버튼에 커맨드 button_input설정
    * 초기 숫자 보드_인터페이스에 입력 (파란색)
  * button_search_num(num) : 하단 숫자 찾기 버튼
    * 이전에 누른 버튼 비활성화
    * 현재 누른 버튼과 동일하면 종료
    * 누른 버튼의 숫자들의 배경 노란색으로 변경
    * 해당하는 숫자를 모두 찾으면 배경색 회색으로 변경(다른 함수에서)(이후 '찾기 버튼 판단'으로 서술)
  * search_del(rdx, cdx) : button_search_num의 '찾기 리스트'에서 제외
    * 해당 인덱스에 있는 숫자를 변경할때 사용
  * button_input(rdx, cdx, mode_func) : 숫자 입력창
    * 이전에 열린 입력창 닫기
    * 숫자 입력창 및 버튼 생성
    * 커맨드 button_change사용
  * button_change(tk, rdx, cdx, i, mode_func) : 숫자 입력
    * search_del후 입력 숫자 '찾기 리스트'에 추가
    * 찾기 버튼 판단
    * 스도쿠 완성 판단 후 완료창 팝업
    * 스도쿠 규칙에 어긋난 숫자를 입력하면 에러창 3초간 팝업
  * button_rego(instant) : 풀고있던 스도쿠로 복귀
  * button_ex(instant) : 메인 화면으로 복귀 (게임 다시 플레이 가능)
  * button_reset : 처음 상태로 전환
  * button_judge(mode_func) : 오답에 해당되는 숫자를 빨간색으로 전환
  * button_del(mode_func) : 오답에 해당되는 숫자 삭제 후 버튼의 배경을 빨간색으로 1초 전환
  * button_answer(mode_func) : 모든 숫자를 정답으로 바꾸고 오답에 해당되는 숫자를 빨간색으로 전환
  * run_sudoku(board, mode, level, on_close=None) : 스도쿠 게임 실행
* sudoku_board.py : 스도쿠 보드 생성
  * make_empty : 빈 보드 생성
  * random_box : 3x3 랜덤 박스 생성
  * random_board(board, a) : 보드의 a위치에 random_box적용
  * random_del(board, mode_func, level) : 완성된 보드에서 랜덤 숫자 삭제
    * 난이도에 따라 38, 43, 48개 삭제
    * 삭제후 풀지 못하면 다시 삭제
  * valid_random_board(board, a, mode_func) : random_board를 이용해 보드에 규칙에 맞는 random_box적용
  * make_random(mode, level) : 랜덤 보드 생성
    * sudoku_solver.count_solutions를 이용해 유일성 강화
* sudoku_solver.py : 스도쿠 풀이
  * is_current_board_valid(board) : 기본 스도쿠 규칙에 맞는 보드인지 판단
  * is_current_cross_board_valid(board) : is_current_board_valid의 크로스 버전
  * is_valid_set_of_chunk(chunk) : 기본 스도쿠 규칙 검사
  * get_boxes(board) : 3x3 박스 추출
  * get_cross(board) : 대각선 추출
  * get_empty_cells(board) : 보드에서 빈곳 추출
  * solve_sudoku(board, valid_board_func) : solver리턴
    * 시작 시간 저장
  * solver(board, valid_board_func, start, timeout=3) : 스도쿠 풀기
    * 제한 시간을 넘으면, 보드가 규칙에 어긋나면, 풀지 못하면 False 리턴
    * 빈 부분이 없으면 True 리턴
    * 빈 부분에 1~9중 랜덤한 순서대로 입력후 solver실행 (백트래킹)
  * count_solutions(board, valid_board_func, limit=2) : 스도쿠 중복해 유무를 검사

# 참고 자료

* GUI 인터페이스
  * "https://velog.io/@parkjw0/python-%EC%9D%98-Tkinter-%EB%AA%A8%EB%93%88%EC%9D%84-%EC%82%AC%EC%9A%A9%ED%95%B4%EC%84%9C-To-Do-List%EB%A5%BC-%EB%A7%8C%EB%93%A4%EC%96%B4%EB%B3%B4%EC%9E%90-1"
  * 기본적인 인터페이스는 위 자료 참고
  * 달력을 스도쿠판으로 변형
* 백트래킹 기반 스도쿠 생성 알고리즘
  * "https://github.com/kodingk/sudoku-solver/blob/main/sudoku_solver.py"
  * 기본적으로 동일하고 몇몇 기능 추가 및 변경
    * is_current_board_valid와 get_boxes의 크로스 버전인 is_current_cross_board_valid와 get_cross를 추가
    * solver에 start와 timeout=3변수 추가해 연산 시간이 길어지면 종료
    * solver에서 탐색 순서를 1~9에서 랜덤으로 변경해 랜덤성 강화
    * count_solutions추가 스도쿠 중복해 유무를 검사해 유일성 강화

# 스크린샷

* 메인 화면(모드 선택)
<img src="스크린샷/SudokuGame_main.png" width="400">

* 난이도 선택(오리지널/크로스)
<img src="스크린샷/SudokuGame_original.png" width="350">
<img src="스크린샷/SudokuGame_cross.png" width="350">

* 로딩창
<img src="스크린샷/SudokuGame_loading.png" width="200">

* 생성되는 보드(오리지널_normal/크로스_hard)
<img src="스크린샷/SudokuGame_original_play.png" width="400">
<img src="스크린샷/SudokuGame_cross_play.png" width="400">

* 숫자 찾기
<img src="스크린샷/SudokuGame_search.png" width="400">

* 숫자 찾기(모두 완료)
<img src="스크린샷/SudokuGame_search_done.png" width="400">

* 스도쿠 완성
<img src="스크린샷/SudokuGame_end.png" width="200">

# 라이선스

MIT License

# TODO

타이머

힌트 기능

자동 채우기

퍼즐 저장/불러오기/중간종료

입력 취소(여러번)

스도쿠 생성 시간 단축
