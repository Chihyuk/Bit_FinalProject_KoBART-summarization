#EHHelper.py
class EHHelper:
    #HTML Tag를 제거하는 정적메서드
    # src:소스 문자열
    @staticmethod
    def RemoveTag(src):
        #무한 루프
        while True:
           try:
                #여는 위치 조사
                s = src.index('<')
                #닫는 위치 조사
                e = src.index('>')
                #태그 부분 추출하기
                if s<e:
                    src = src[:s]+src[e+1:]
                else:
                    src = src[:e]+src[e+1:]
           #태그가 없을 때 예외 발생(index 함수에 의해)
           except:
                return src
    #특수 문자를 제거(공백, 숫자, 알파벳만 남음)
    # src:입력 문자열
    # 반환: 제거한 문자열
    @staticmethod
    def RemoveSymbol(src):
        dst =""
        for elem in src:
            #알파벳, 숫자, 공백일 때
            if elem.isalnum() or elem.isspace():
                dst+=elem
        return dst

    #HMTL 특수 문자 제거 (정적)메서드
    # src: 입력 문자열
    # 반환: 제거한 문자열
    @staticmethod
    def RemoveHtmlSymbol(src):
        while True:
           try:
               s = src.index('&')
               e = src.index(';')
               if s<e:
                   src = src[:s]+src[e+1:]
               else:
                   src = src[:e]+src[e+1:]
           #모든 처리가 끝났을 때(index 메서드에서 예외 발생)
           except:
               return src

    #HTML 태그, HTML 특수 문자, 기호를 제거하는 (정적)메서드
    # src:입력 문자열
    # 반환: 제거한문자열
    @staticmethod
    def RemoveTagAndSpecialCh(src):
        src = EHHelper.RemoveTag(src)
        src = EHHelper.RemoveHtmlSymbol(src)
        src = EHHelper.RemoveSymbol(src)
        return src
