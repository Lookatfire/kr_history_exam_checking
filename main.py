from pandas import concat as con
from pandas import DataFrame as df
from pandas import read_excel as rxlsx

class kr_history_exam():
  def __init__(self):
    self.all_info=rxlsx('한능검 채점기 전용 정보.xlsx')
    self.all_answer=rxlsx('한능검 채점기 전용 답.xlsx')
    self.all_score=rxlsx('한능검 채점기 전용 배점.xlsx')
    self.accept_answer=["1","2","3","4","5","x"]
    self.accept_score=["1","2","3"]

  def upload(self):
    question_num=1
    answer=[]
    score=[]
    for i in range(2):
      if i == 0:
        while question_num<51:
          k=input(f'{question_num}번의 정답을 입력하시오.')
          if k in self.accept_answer:
            answer.append(k)
            question_num+=1
          else:
            print("정답에 해당되지 않는 답입니다. 다시 시도해주세요.")
      else:
        while question_num<51:
          k=input(f'{question_num}번의 배점을 입력하시오.')
          if k in self.accept_score:
            score.append(int(k))
            question_num+=1
          else:
            print("배점에 해당되지 않습니다. 다시 시도해주세요.")
        question_num=1
    answer_max=max(self.all_answer.columns)+1
    score_max=max(self.all_score.columns)+1
    an=df({answer_max:answer})
    sc=df({score_max:score})
    alan=con([self.all_answer,an],axis=1)
    alsc=con([self.all_score,sc],axis=1)
    alan.to_excel('한능검 채점기 전용 답.xlsx', index=False)
    alsc.to_excel('한능검 채점기 전용 배점.xlsx', index=False)
    print(f'{answer_max}회의 답과 배점을 저장하였습니다.')

  def marking(self):
    u=0
    print("=====================================================")
    print("채점 시스템을 가동합니다.")
    print(f'회차는 {min(self.all_answer.columns)}회부터 {max(self.all_answer.columns)}회까지 가능합니다.')
    while u==0:
      try:
        checking_test_num=int(input("채점하기 원하는 회차를 자연수로만 입력하세요. : "))
      except ValueError:
        print("잘못된 회차를 입력하였습니다. 다시 시도하시오.")
      else:
        if checking_test_num>=min(self.all_answer.columns) and checking_test_num<=max(self.all_answer.columns):
          answer_data=self.all_answer[checking_test_num]
          score_data=self.all_score[checking_test_num]
          u+=1
        else:
          print(f"{checking_test_num}회는 해당되지 않는 회차입니다. 다시 시도해주세요")
    print("이제부터는 채점을 시작합니다. 정수로만 입력하세요.")
    t,score,good,worse,ocuur_error=0,0,0,0,0
    while t<50:
      input_answer=input(f"{t+1}번의 답을 입력해주세요 : ")
      if input_answer in self.accept_answer:
        if answer_data[t]=="x":
          print(f'{t+1}번 문제는 답이 없어서 모두 정답처리됩니다.')
          score=score+score_data[t]
          good+=1
          ocuur_error+=1
        elif int(input_answer)==answer_data[t]:
          print(f'{t+1}번 정답')
          score=score+score_data[t]
          good+=1
        else:
          print(f'{t+1}번 오답')
          worse+=1
        t+=1
      else:
        print('잘못된 답을 입력하였습니다. 다시 시도해주세요')
    print("=====================================================")
    if checking_test_num<47:
      print(f'고급 {checking_test_num}회 채점 결과')
      if score>=70:
        print("1급 합격")
      elif score>=60:
        print("2급 합격")
      else:
        print("불합격")
    else:
      print(f'심화 {checking_test_num}회 채점 결과')
      if score>=80:
        print("1급 합격")
      elif score>=70:
        print("2급 합격")
      elif score>=60:
        print("3급 합격")
      else:
        print("불합격")
    print("")
    print("채점 세부 사항")
    print(f"점수 : {score}점")
    print(f"맞은 개수 : {good}개")
    print(f"틀린 개수 : {worse}개")
    print(f"오류있는 문항 개수 : {ocuur_error}개")
    print('* 오류있는 문항은 맞은 것으로 처리됩니다. 유의하세요.')
    print("=====================================================")
    print('본 시험의 시험일과 합격률은 아래와 같습니다.')
    print(f"시험일 : {self.all_info['시험일'][checking_test_num-15]}")
    print(f"합격률 : {self.all_info['합격률'][checking_test_num-15]}%")
    print("시험 보느라 수고 많으셨습니다.")

  def main(self):
    print("=====================================================")
    print("한능검 채점기 시스템 가동")
    print("(전) 고급, (현) 심화 난이도 문제만 채점 가능합니다.")
    print(f'채점 가능한 회차는 {min(self.all_answer.columns)}회~{max(self.all_answer.columns)}회입니다.')
    print('답과 배점을 추가할 때 같은 회차를 저장시키길 바랍니다.')
    print('=====================================================')
    print('1. 답이랑 배점을 추가시키기')
    print('2. 채점하기')
    print('3. 종료시키기')
    while True:
      try:
        manu_input_data=int(input("메뉴를 정수로 입력하시오. : "))
      except ValueError:
        print("오류를 불러오는 값을 입력하였습니다. 다시 시도하세요.")
      else:
        if manu_input_data==1:
          kr_history_exam.upload(self)
        elif manu_input_data==2:
          kr_history_exam.marking(self)
        elif manu_input_data==3:
          print('한능검 채점기 시스템을 종료합니다.')
          break
        else:
          print("메뉴에는 없는 값을 넣으셨습니다. 다시 시도하세요.")

        if manu_input_data<3:
          print('=====================================================')
          print('1. 답이랑 배점을 추가시키기')
          print('2. 채점하기')
          print('3. 종료시키기')