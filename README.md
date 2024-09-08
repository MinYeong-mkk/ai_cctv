# AI_CCTV

<br>

## AI_CCTV 서비스 개요
이 프로젝트는 CCTV 영상을 분석하여 실시간으로 사람의 성별과 나이를 예측하고, 이를 시간별로 기록하여 로그를 생성하는 시스템입니다. AI 딥러닝 모델을 활용하여 얼굴 인식 기술과 함께 성별 및 연령대 추정을 진행하며, 추출된 데이터는 데이터베이스에 저장되어 시간대별 통계를 확인할 수 있습니다.


### 프로젝트 기간
- 2019.09.02 - 2020.05.04

### 팀원 소개

| 이름   | 역할/포지션               | 설명                                                                                                                                      |
|--------|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| 노누리 | 팀장, Back-End, AI          | Keras를 활용하여 AI 모델 개발을 주도하였으며, Back-End 시스템의 설계와 구현을 총괄. 또한, 서버와 AI 모델의 통합 및 최적화를 담당.   |
| 김아현 | Back-End 보조, AI 총괄       | 시스템의 하드웨어 환경 설정 및 Back-End 보조 작업을 수행. AI 데이터셋 구축과 데이터 라벨링, AI 모델 학습 및 지름 측정 알고리즘 구현을 담당.  |
| 김민영 | Front-End, 통신             | Front-End 개발과 UI 구현을 담당하며, 앱과 AI 모델 간의 TCP 통신을 구축. 데이터 전송 및 통신 안정성을 확보하는 작업을 수행.          |



<br>

## 시스템 구성도
![시스템 구성도](images/시스템구성도.png)



## 모델 소개

<div style="display: flex; justify-content: space-between;">
  <div style="margin-right: 10px;">
    <p>● 기존 모델 데이터</p>
    <img src="images/기존모델데이터.png" alt="기존 모델 데이터" style="width: 100%;">
  </div>
  <div style="margin-left: 10px;">
    <p>● 새로 추가한 데이터</p>
    <img src="images/새로추가한데이터.png" alt="새로 추가한 데이터" style="width: 100%;">
  </div>
</div>

<br>
<br>

레이블 처리

![alt text](images/label.png)


<br>
<br>

<table>
  <tr>
    <td style="text-align: center;">
      <p>● 기존 모델 데이터</p>
      <img src="images/beforeTrain.png" alt="기존 모델 데이터" style="width: 10%;">
    </td>
    <td style="text-align: center;">
      <p>● 새로 추가한 데이터</p>
      <img src="images/afterTrain.png" alt="새로 추가한 데이터" style="width: 10%;">
    </td>
  </tr>
</table>




![alt text](images/loss_accuracy.png)
LOSS 성별 – 0.4364 나이 – 3.8608<br>
ACCURACY 성별 – 0.8186 나이 – 0.0646



## 기능 소개

![alt text](images/example.png)


### 실제 화면

<div style="text-align: center;">
  <img src="images/시연1.gif" alt="시연 1" style="width: 75%;">
  <p><em>모드 설정</em></p>
</div>

<div style="text-align: center;">
  <img src="images/시연2.gif" alt="시연 2" style="width: 75%;">
  <p><em>분석</em></p>
</div>

<div style="text-align: center;">
  <img src="images/시연3.gif" alt="시연 3" style="width: 75%;">
  <p><em>로그 확인</em></p>
</div>