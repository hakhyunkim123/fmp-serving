fmp chatbot serving 부분 개발 中
===============

2020.11.23
-----------

## API
1. 질문 메세지 처리 (POST, /serving/req/question)
2. 답변 등록 (POST /serving/add/answer)
3. 사용내역 조회 (GET /serving/userhist)
4. 데이터셋 DB저장 (GET /serving/save/dataset)


req: 오라클 에러
res: 오류난 에러코드가 무엇가요?

req: ORA-01111
res: 어쩌구 ~~~

답변등록시, user-id 키벨류 값으로 넣어야 됩니다.

postman 데이터 넣었습니다.
