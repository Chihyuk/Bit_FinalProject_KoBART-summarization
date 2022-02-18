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


def splitcont(cont):
  t_list = []

  while(True):
      pos = cont.find('.')
      if pos == -1:
          break
      t_list.append(cont[:pos+1])
      cont = cont[pos+1:]
    
  return t_list


def sumfive(t_list):
  try:
    cont_ahrt = len(t_list)//5      # 몫
    cont_skajwl = len(t_list)%5     # 나머지
    len_5 = []    # 리턴할 리스트

    for i in range(cont_ahrt):
        temp = t_list[i*5]+t_list[i*5+1]+t_list[i*5+2]+t_list[i*5+3]+t_list[i*5+4]
        len_5.append(temp)

    if cont_skajwl != 0:
      tt = len_5[-1]
      for j in range(cont_skajwl):
          tt = tt + t_list[(cont_ahrt-1)*5 + j]
      del len_5[-1]
      len_5.append(tt)
  except:
    return len_5
  else:
    return len_5


def useModel(content):
    model = load_model()
    tokenizer = get_kobart_tokenizer()
    input_ids = tokenizer.encode(content)
    input_ids = torch.tensor(input_ids)
    input_ids = input_ids.unsqueeze(0)
    output = model.generate(input_ids, eos_token_id=1, max_length=512, num_beams=5)
    output = tokenizer.decode(output[0], skip_special_tokens=True)
    return output


def main(a=2):
  if a == 1:
    conts = TotalSql.findContent()
    for cont in conts:
      try:
        total_output = ""   # 문서 요약한 애들 모으기
        if cont:
          cont_split = splitcont(cont[1])
          cont_sum_five = sumfive(cont_split)
          for csf in cont_sum_five:
            csf = csf.replace('\n', '')
            output = useModel(csf)
            total_output = total_output + output + "\n"
        TotalSql.insertSum(cont[0], total_output)

        output_one = useModel(cont[1])
        TotalSql.insertSum_One(cont[0], output_one)
      except:
        continue
    threading.Timer(180, main).start()

  elif a == 2:
    conts = TotalSql.findContent_front()
    exist = 0
    for cont in conts:
      try:
        total_output = ""   # 문서 요약한 애들 모으기
        if cont:
          cont_split = splitcont(cont[1])
          cont_sum_five = sumfive(cont_split)
          for csf in cont_sum_five:
            csf = csf.replace('\n', '')
            output = useModel(csf)
            total_output = total_output + output + "\n"
        exist = TotalSql.insertSum_front(cont[0], total_output, exist)
        if exist >= 5:
          break
        output_one = useModel(cont[1])
        TotalSql.insertSum_One(cont[0], output_one)
      except:
        continue
    threading.Timer(180, main).start()

if __name__ == "__main__":
    main(1)

    