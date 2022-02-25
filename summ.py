# -*- coding: utf-8 -*-

import torch
# import streamlit as st
from kobart import get_kobart_tokenizer
from transformers.models.bart import BartForConditionalGeneration

# @st.cache
def load_model():
    model = BartForConditionalGeneration.from_pretrained('./kobart_summary')
    # tokenizer = get_kobart_tokenizer()
    return model

model = load_model()
tokenizer = get_kobart_tokenizer()

#st.title("KoBART 요약 Test")
#text = st.text_area("뉴스 입력:")

text = """
다만 어제까지는 선별진료소에서 PCR 검사나 신속항원검사 중 선택해서 받을 수 있었지만, 오늘부터는 고위험군만 PCR 검사를 받고, 그 외는 신속항원검사를 해야 합니다.

신속항원검사는 관리자의 감독 아래 검사자가 자가검사키트로 직접 시행합니다.

PCR 검사를 받는 고위험군은 60세 이상 고령층, 확진자와 밀접접촉 등 역학적 관련이 있는 사람, PCR 검사를 받아야 한다는 의사 소견이 있는 사람, 신속항원검사에서 양성이 나온 사람, 요양병원 등 취약시설 종사자 등입니다.

정부는 지난달 28일까지 전국 선별진료소와 임시선별검사소에 총 220만 명분의 자가검사키트를 배송했고, 내일까지 추가로 466만 명분의 키트를 배송할 계획입니다.

방역패스로 사용할 수 있는 음성확인서는 선별진료소에서 관리자 감독하에 신속항원검사를 해서 음성이 나온 경우와 호흡기전담클리닉 등 지정 병원에서 전문가용 신속항원검사로 음성이 나온 경우 발급받을 수 있고 유효기간은 24시간입니다.

"""

# st.markdown("## 뉴스 원문")
# st.write(text)

if text:
    text = text.replace('\n', '')
    # st.markdown("## KoBART 요약 결과")
    #with st.spinner('processing..'):
    input_ids = tokenizer.encode(text)
    input_ids = torch.tensor(input_ids)
    input_ids = input_ids.unsqueeze(0)
    output = model.generate(input_ids, eos_token_id=1, max_length=512, num_beams=5)
    output = tokenizer.decode(output[0], skip_special_tokens=True)
    #st.write(output)

print(output)