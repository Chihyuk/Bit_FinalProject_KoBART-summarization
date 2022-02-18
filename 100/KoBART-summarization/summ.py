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
삼성 SDS, LG CNS, 카카오엔터프라이즈 등이 네이버에 이어 5세대 이동통신(5G) 특화망용 주파수 할당을 검토 중이다.

과학기술정보통신부는 20일 용인세브란스병원에서 이음5G 확산을 위해 관련 수요·공급기업 간담회를 개최했다. 앞서 지난해 정부는 공모전을 통해 5G 특화망의 새 이름으로 ‘이음(e-Um) 5G’를 선정한 바 있다.

이날 행사에는 5G 특화망 국내 1호 기업인 네이버클라우드를 비롯, 삼성SDS, LG CNS, 카카오엔터프라이즈, 용인세브란스병원, 부산시 등이 참석했다. 삼성전자, 퀄컴코리아 등 장비 업체도 참여했다.

과기정통부 관계자는 “5G 특화망 수요 기업과 공급 기업 간 교류를 위해 자리를 마련했다”라며 “이번 행사에 참가한 수요 기업들 대부분이 특화망 도입 의사가 있는 것으로 알고 있다”라고 말했다.

실제 카카오엔터프라이즈는 중대재해 예방을 위한 안전관리 체계 구축을 고려 중으로, 여기에 특화망 적용을 검토 중이다. 용인세브란스병원도 고용량 의료영상 전송, 무선 의료장비의 안정적 접속 등의 필요성으로 도입을 검토하고 있다.

조경식 과기정통부 차관은 “오늘 건의된 현장 애로사항은 조속히 개선방안을 찾는 한편, 파급력 있는 혁신 사례를 선도적으로 확보하고 초기 시장을 창출하기 위한 다양한 방안을 강구하겠다”라며 “세계적으로 아직 이음5G는 강자가 없는 상황이므로, 그간 모은 5G+ 관련 기술력과 디지털뉴딜 성과를 잘 조화한다면 우리가 이음5G의 선두주자로 디지털 대전환 시기에 좋은 기회가 될 수 있을 것으로 기대한다”라고 말했다.

김양혁 기자 present@chosunbiz.com
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