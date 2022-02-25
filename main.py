from operator import mod
from TotalSql import TotalSql

import torch
# import streamlit as st
from kobart import get_kobart_tokenizer
from transformers.models.bart import BartForConditionalGeneration
import threading
from TotalSql import TotalSql

# @st.cache
def load_model():
    model = BartForConditionalGeneration.from_pretrained('./kobart_summary')
    # tokenizer = get_kobart_tokenizer()
    return model

# 문장이 길 경우 나눠서 요약하기 위해 문장을 끊어주는 메소드
def splitcont(cont):                    
  t_list = []                         # 빈 리스트 생성

  while(True):
      pos = cont.find('.')            # 마침표를 기준으로
      if pos == -1:                   # 마침표가 없을 때 까지
          break
      t_list.append(cont[:pos+1])     # 나눠서 t_list에 넣기
      cont = cont[pos+1:]             # 다음 마침표 찾기위해 t_list에 들어간 문자열 제거
    
  return t_list                       # 나눈 리스트 리턴

# 1문장을 10문장으로 합치기
def sumten(t_list):
  try:
    cont_ahrt = len(t_list)//10       # 몫
    cont_skajwl = len(t_list)%10      # 나머지
    len_10 = []    # 리턴할 리스트

    # 10개 쌓기
    for i in range(cont_ahrt):
        temp = t_list[i*10]+t_list[i*10+1]+t_list[i*10+2]+t_list[i*10+3]+t_list[i*10+4]+t_list[i*10+5]+t_list[i*10+6]+t_list[i*10+7]+t_list[i*10+8]+t_list[i*10+9]
        len_10.append(temp)

    # 나머지가 있는 경우
    if cont_skajwl != 0:
      tt = len_10[-1]                               # 10개씩 묶어 저장된 문자열에 나머지 문장들도 넣어서 요약시키기 위해 마지막에 저장한 내용 가져오기
      for j in range(cont_skajwl):                  # 나머지 처리하기 위해 for 문 돌리기
          tt = tt + t_list[(cont_ahrt)*10 + j]      # 나머지를 마지막 문장에 합쳐주기
      del len_10[-1]                                # 중복된 마지막 문장 제거
      len_10.append(tt)                             # 나머지가 합쳐진 마지막 문장 append
  except:
    return len_10                                   # 에러가 발생되면 쌓인 문장만 return
  else:
    return len_10                                   # 나눈 문장 return

# KoBART 모델 사용해 요약하기
def useModel(content):
    model = load_model()
    tokenizer = get_kobart_tokenizer()
    input_ids = tokenizer.encode(content)
    input_ids = torch.tensor(input_ids)
    input_ids = input_ids.unsqueeze(0)
    output = model.generate(input_ids, eos_token_id=1, max_length=512, num_beams=5)
    output = tokenizer.decode(output[0], skip_special_tokens=True)
    return output


def main(a=2):                                               # 인자값을 안주면 내림차순으로 넣기

  # n_id 낮은 숫자부터 오름차순으로 요약 시키기
  if a == 1:
    conts = TotalSql.findContent()                            # DB에 있는 전체 n_id(기사 아이디)와 n_content(기사 내용) 가져오기
    for cont in conts:                                        # 기사 하나씩 처리하기
      try:
        total_output = ""                                     # 문서 요약한 애들 모으기위한 변수
        if cont:                                              # 기사가 있다면
          cont_split = splitcont(cont[1])                     # 마침표를 기준으로 문장들을 나누기
          cont_sum_ten = sumten(cont_split)                   # 한 줄씩 나눈 문장들을 10문장으로 합치기
          for csf in cont_sum_ten:                            # 10줄씩 끊은 문장 처리
            csf = csf.replace('\n', '')                       # 요약 모델 처리를 위해 개행 없애기
            output = useModel(csf)                            # 요약처리
            total_output = total_output + output + "\n"       # 요약된 문장을 개행을 붙여 넣어주기
        TotalSql.insertSum(cont[0], total_output)             # 기사 아이디와 요약 내용과 함께 인자값으로 넣어 값 넣기 

        output_one = useModel(cont[1])                        # 전체 내용을 넣어 모델 돌리기 => 한줄로 생성
        TotalSql.insertSum_One(cont[0], output_one)           # 한 줄 들어가는 db에 넣기
      except:
        continue
    threading.Timer(180, main).start()                        # 3분 뒤 재시작

  # n_id 큰 숫자부터 내림차순으로 요약 시키기
  elif a == 2:  
    conts = TotalSql.findContent("desc")                        # desc 인자를 주어 DB에 있는 전체 n_id(기사 아이디)와 n_content(기사 내용) 가져오기
    exist = 0                                                   # db에 값이 존재하는지 판단하기 위해 변수 생성
    for cont in conts:
      try:
        total_output = ""                                       # 문서 요약한 애들 모으기
        if cont:
          cont_split = splitcont(cont[1])
          cont_sum_ten = sumten(cont_split)
          for csf in cont_sum_ten:
            csf = csf.replace('\n', '')
            output = useModel(csf)
            total_output = total_output + output + "\n"
        exist = TotalSql.insertSum(cont[0], total_output, exist)  # exist 변수를 같이 넣어 존재 여부 판단하기
        if exist >= 5:                                            # 만약 DB에 연속적으로 같은 값이 5번 들어갔다고 판단하면 다 요약했다고 판단하여 멈추기
          break
        output_one = useModel(cont[1])                            # 한 줄 요약
        TotalSql.insertSum_One(cont[0], output_one)
      except:
        continue
    threading.Timer(180, main).start()                            # 3분 뒤 재시작


if __name__ == "__main__":
    main(1)

    