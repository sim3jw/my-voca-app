import streamlit as st
import streamlit.components.v1 as components
import random
import pandas as pd

# 모바일 화면에 맞게 화면 넓게 쓰기
st.set_page_config(page_title="나만의 단어장", layout="centered")

# ==========================================
# 1. 기본 단어 데이터 (1과 ~ 30과)
# ==========================================
voca_1 = {
    "detour": "우회하다", "pull over": "길가에 대다", "meander": "구불구불하다", "careen": "위태롭게 달리다",
    "diverge": "갈라지다", "hail": "불러 세우다", "jump the gun": "성급하게 출발하다", "charter": "전세 내다",
    "designate": "지정하다", "bypass": "우회하다", "moor": "정박시키다", "pandemonium": "대혼란",
    "convoluted": "복잡한", "veer": "방향을 바꾸다", "cramped": "비좁은", "make way": "길을 열어주다",
    "disregard": "무시하다", "bound": "~행의", "descent": "하강", "in turn": "차례로", "mileage": "연비"
}

voca_2 = {
    "frugal": "절약하는", "cut down on": "줄이다", "mortgage": "담보 대출", "loan": "대출",
    "in the red": "적자인", "recession": "불경기", "stimulate": "자극하다", "galvanize": "자극하다",
    "plummet": "폭락하다", "remuneration": "보수", "reimburse": "배상하다", "deficit": "적자",
    "currency": "화폐", "subsidy": "보조금", "redeem": "교환하다", "tally up": "합계하다",
    "disparity": "불균형", "endow": "기부하다", "abundant": "풍부한", "moratorium": "지불 유예",
    "parity": "동격", "pitch in": "협력하다", "rig": "조작하다", "appraise": "감정하다",
    "recoup": "만회하다", "plunge": "급락하다", "unfettered": "자유로운", "deposit": "예금하다",
    "sustain": "유지하다", "bankrupt": "파산한", "burden": "부담", "capitalism": "자본주의",
    "circumstance": "상황", "commodity": "상품", "debtor": "채무자", "interest rate": "금리",
    "levy": "징수하다", "liability": "부채", "monopolize": "독점하다", "monopoly": "독점",
    "poverty": "빈곤", "profitable": "이익이 되는"
}

voca_3 = {
    "hit the spot": "만족시키다", "savor": "음미하다", "edible": "먹을 수 있는", "delectable": "맛있는",
    "devour": "게걸스럽게 먹다", "voracious": "게걸스럽게 먹는", "appetite": "식욕", "bland": "담백한",
    "authentic": "진정한", "rigorous": "엄격한", "quibble": "옥신각신하다", "picky": "까다로운",
    "concoct": "조리하다", "imbibe": "마시다", "culinary": "요리의", "pungent": "톡 쏘는",
    "satiate": "충분히 만족시키다", "connoisseur": "감정가", "gorge": "게걸스럽게 먹다", "make do with": "견디다",
    "rancid": "썩은 냄새가 나는", "prod": "찌르다", "purveyor": "조달 업자", "funnel": "깔때기",
    "parched": "몹시 목마른", "provision": "식량", "help oneself to": "~을 마음껏 먹다", "pulverize": "분쇄하다",
    "prick": "찌르다", "dairy": "유제품의", "eat out": "외식하다", "regardless of": "~에도 불구하고"
}

voca_4 = {
    "prolific": "다작의", "narrative": "이야기", "obscure": "애매한", "engrossing": "마음을 사로잡는",
    "fathom": "이해하다", "banality": "진부함", "tangential": "거의 관계가 없는", "epitomize": "전형적으로 나타내다",
    "bewilder": "당황하게 하다", "connotation": "함축", "prescient": "선견지명이 있는", "altercation": "언쟁",
    "formulaic": "정형화된", "manipulate": "조작하다", "pass for": "~으로 통하다", "backdrop": "배경",
    "recrimination": "맞비난", "seminal": "중대한", "cull": "추려내다", "exaggerate": "과장하다",
    "legible": "필적이 읽기 쉬운", "sink in": "충분히 이해되다", "extemporize": "즉흥적으로 하다",
    "recondite": "난해한", "euphemism": "완곡어법", "account for": "~을 설명하다", "perception": "인식",
    "envision": "마음속에 그리다", "coin": "창조하다", "induce": "야기하다", "implication": "암시",
    "florid": "화려한", "enunciate": "명확히 말하다", "interpret": "해석하다", "literacy": "읽고 쓰는 능력",
    "stand for": "~을 상징하다", "wordy": "장황한"
}

voca_5 = {
    "drizzle": "이슬비", "moderate": "적당한", "soak": "적시다", "let up": "그치다",
    "peculiar": "이상한", "imminent": "임박한", "admittedly": "인정하건대", "fluctuate": "오르내리다",
    "inundate": "침수시키다", "sap": "약화시키다", "arid": "건조한", "bundle up": "껴입다",
    "foliage": "나뭇잎", "scorch": "시들게 하다", "lull": "잠잠함", "hunch": "예감",
    "down in the dumps": "우울한", "germane": "밀접한 관련이 있는", "bane": "골칫거리",
    "disperse": "퍼뜨리다", "accustomed": "익숙한", "drench": "흠뻑 젖게 하다",
    "cataclysm": "대재앙", "whirling": "소용돌이치는", "subside": "진정되다",
    "precede": "~보다 앞서 발생하다", "concerning": "~에 관하여", "alarming": "놀라운"
}

voca_6 = {
    "pledge": "약속하다", "advocate": "지지하다", "corruption": "부패", "administration": "정권",
    "rampant": "만연하는", "allay": "진정시키다", "impose": "부과하다", "enact": "제정하다, 연기하다",
    "mitigate": "완화하다", "defy": "~에게 반항하다", "garner": "정보/지지를 얻다", "delegate": "대표",
    "autonomy": "자치권", "reinstate": "복직시키다", "resignation": "사직, 포기", "proclaim": "선언하다",
    "muster": "모으다", "suppress": "억누르다", "incumbent": "재임자", "intercede": "중재하다",
    "embargo": "통상금지", "conciliatory": "회유적인", "diplomatic": "외교적 수완이 있는", "chicanery": "속임수",
    "forswear": "그만두다", "regressive": "퇴보하는", "retroactive": "소급하는", "impasse": "교착상태",
    "stonewall": "방해하다", "engaged": "종사하는", "mandate": "요구하다", "indefatigable": "끈질긴",
    "sanction": "처벌", "rebuke": "비난하다", "subjugate": "복종시키다", "face the music": "비난을 받아들이다",
    "unilateral": "일방적인", "turmoil": "혼란", "consensus": "합의", "denounce": "비난하다",
    "armed": "무장한", "authority": "권한", "communism": "공산주의", "civilian": "민간의",
    "democracy": "민주주의", "diplomat": "외교관", "dispute": "논쟁하다", "embassy": "대사관",
    "facilitate": "촉진하다", "parliament": "의회", "protest": "항의하다", "ulterior motive": "속셈",
    "warfare": "전쟁"
}

voca_7 = {
    "vacancy": "빈방", "aisle seat": "통로 쪽 좌석", "carry-on": "기내 반입용의",
    "overhead compartment": "머리 위 짐칸", "lavatory": "화장실", "layover": "경유",
    "impeccable": "결점 없는", "barge": "난입하다, 뗏목", "tease": "괴롭히다", "circumspect": "신중한",
    "obtrusive": "눈에 거슬리는", "cruise": "순항하다", "aerial": "대기의", "unruffled": "침착한",
    "content": "내용물, 만족한", "concourse": "중앙 홀", "raucous": "시끄러운", "receptionist": "접수원",
    "see off": "~를 배웅하다", "stow": "싣다"
}

voca_8 = {
    "sturdy": "튼튼한", "regimen": "요법", "supplement": "보충하다, 보충", "come down with": "(병에) 걸리다",
    "congested": "혼잡한, 코가 막힌", "lethargic": "무기력한", "diagnose": "진단하다", "contract": "(병에) 걸리다, 계약서",
    "infection": "감염", "inject": "주사하다", "prescription": "처방", "pass out": "기절하다",
    "remedy": "바로잡다, 구제책", "aggravate": "악화시키다", "detrimental": "해로운", "prognosis": "예후",
    "vigorous": "격렬한, 강건한", "hygiene": "위생", "shake off": "(병을) 떨쳐내다", "posture": "자세",
    "acute": "심한", "dehydration": "탈수", "indisposed": "몸이 안좋은", "a bout of flu": "독감 치레",
    "cot": "간이침대", "spry": "기운찬", "doze off": "깜빡 졸다", "outbreak": "발발",
    "constrict": "수축하다", "chronic": "만성적인", "obesity": "비만", "addicted": "중독된",
    "torpid": "무기력한", "efficacy": "효능", "resist": "저항하다", "complications": "합병증",
    "episode": "발현", "transitory": "일시적인", "allergic": "알레르기가 있는", "bleed": "출혈하다",
    "cripple": "불구로 만들다", "irritate": "~에 염증을 일으키다", "physician": "의사", "unconscious": "의식을 잃은"
}

voca_9 = {
    "ecstatic": "열광하는", "arduous": "몹시 힘든", "assiduous": "근면한", "kudos": "찬사",
    "pay off": "성과를 거두다, 빚을 모두 갚다", "preoccupied": "몰두한", "agenda": "안건", "feckless": "무책임한",
    "onerous": "부담스러운", "discharge": "해고하다, 방출하다", "ingratiate": "비위를 맞추다", "leave out": "~을 제외하다",
    "upbraid": "꾸짖다", "commensurate": "상응하는", "relegate": "좌천시키다", "grievance": "불만",
    "get around to": "~까지도 하다", "manage to": "간신히 해내다", "loose cannon": "돌발행동을 하는 사람",
    "under the wire": "간신히", "antagonize": "반감을 사다", "goad": "자극하다", "impugn": "이의를 제기하다",
    "impute": "전가하다", "dismiss": "해고하다", "appoint": "임명하다", "adjourn": "잠시 중단하다",
    "occupation": "직업, 업무, 점령", "go at": "~을 열심히 하다", "insist": "요구하다", "be tied up": "바쁘다",
    "be willing to": "기꺼이 ~하다", "bossy": "으스대는", "overwork": "과로하다"
}

voca_10 = {
    "stymie": "좌절시키다", "rehabilitate": "회복시키다", "gaze": "응시하다", "avert": "방지하다, 외면하다",
    "stave off": "안 좋은 일을 면하다", "alleviate": "완화하다", "vulnerable": "취약한", "tide ~ over": "~가 곤경을 헤쳐나가도록 하다",
    "conflagration": "대화재", "precipitate": "촉진하다", "mar": "망치다", "claim": "빼앗다, 주장하다",
    "aghast": "깜짝 놀란", "hobble": "절뚝거리며 걷다", "leery of": "~을 경계하는", "pounce": "갑자기 달려들다",
    "scald": "데게 하다", "cower": "웅크리다", "confine": "가두다, 제한하다", "omit": "빠뜨리다",
    "wade through": "간신히 빠져나가다", "emerge": "나타나다", "revive": "소생시키다", "fatal": "치명적인",
    "pull through": "극복하게 하다", "evacuate": "대피시키다", "plague": "전염병, 괴롭히다", "devastating": "파괴적인",
    "excessive": "과도한", "investigate": "조사하다", "commotion": "소동", "desperate": "필사적인",
    "regrettably": "유감스럽게도", "severe": "심한"
}

voca_11 = {
    "acquaintance": "지인", "courteous": "정중한", "grudge": "유감, 원한", "feud": "불화",
    "amicable": "사이좋은", "compatible": "뜻이 맞는", "ostentatious": "과시하는", "peer": "또래",
    "hospitable": "친절한", "affectation": "허세", "hit it off": "~와 죽이 맞다", "flaunt": "과시하다",
    "condolence": "애도", "congenial": "마음이 맞는", "disparage": "비하하다", "sit on the fence": "중립적 태도를 취하다",
    "hassle": "골치 아픈 일", "amenable": "순종하는", "coerce a into ing": "강요하다", "procrastinate": "꾸물거리다",
    "prone to": "~하는 경향이 있는", "introverted": "내성적인", "take after": "~를 닮다", "slip one’s mind": "잊어버리다",
    "magnanimous": "관대한", "let the cat out of the bag": "무심코 비밀을 누설하다", "work up": "북돋우다", "garrulous": "수다스러운",
    "tell off": "야단치다", "debonair": "멋지고 당당한", "deprecate": "비난하다", "harass": "괴롭히다",
    "let on": "털어놓다", "nuptial": "결혼의", "repulsive": "불쾌한", "get back at": "~에게 복수하다",
    "stick to": "~을 고수하다", "recall": "상기하다", "ring a bell": "들어본 적이 있는 것 같다", "sharp dresser": "멋쟁이",
    "pull one’s leg": "~을 놀리다", "intimate": "친밀한", "preteen": "사춘기 직전의", "avuncular": "아저씨 같은",
    "come over": "들르다", "begrudge": "시기하다", "bolt": "뛰어나가다", "alumnus": "동창",
    "fraternal": "형제간의", "duplicitous": "일구이언의", "insult": "모욕하다", "it’s been ages.": "진짜 오랜만이다",
    "socialize": "어울리다"
}

voca_12 = {
    "medieval": "중세의", "reign": "지배", "consecutive": "연속적인", "defeat": "패배시키다",
    "restore": "회복하다", "flourish": "번창하다, 잘 자라다", "succeed": "계승하다", "successive": "연속적인",
    "trace back to": "~까지 거슬러 올라가다", "abolish": "폐지하다", "occupy": "점령하다", "be occupied with": "~에 전념하다",
    "reclaim": "간척하다", "colossal": "거대한", "rebel": "반역자", "credence": "신빙성",
    "belligerent": "호전적인", "pedigree": "혈통", "vanquish": "패배시키다", "speculate": "추측하다, 투기하다",
    "lapse": "상태에 빠지다", "invade": "침략하다", "excavation": "발굴", "bestow": "수여하다",
    "emancipate": "해방하다", "up in arms": "분개하여", "primeval": "원시 시대의", "posterity": "후대",
    "reprisal": "보복 행위", "triumphant": "승리를 거둔", "grovel": "굽실거리다", "integral": "필수적인, 완전한",
    "remain": "잔해, 여전히 ~이다", "archaeologist": "고고학자", "legacy": "유산", "counterpart": "대응물",
    "wipe out": "없애버리다", "occasion": "때, 야기하다", "afterward": "나중에", "betray": "배반하다",
    "bury": "묻다", "conquer": "정복하다", "conquest": "정복", "liberate": "해방하다",
    "prehistoric": "선사 시대의", "primitive": "원시의", "prosper": "번영하다", "slavery": "노예 제도",
    "territory": "지역"
}

voca_13 = {
    "grumble": "불평하다", "churn out": "대량 생산하다", "necessity": "필수품", "alter": "수선하다, 변경하다",
    "charge": "청구하다, 외상으로 사다", "credit": "외상으로 팔다, 학점", "be charged with": "책임을 지다", 
    "be credited with": "공로를 인정받다", "exempt": "면제되는", "versatile": "다용도의", "shed": "벗다",
    "peddle": "팔러 다니다", "depreciate": "가치가 떨어지다", "wrinkle": "주름이 지다", "spurious": "가짜의",
    "over the moon": "너무나도 행복한", "break in": "~을 길들이다", "ransack": "샅샅이 뒤지다", 
    "take ~ back": "~을 반품하다", "that being said": "그렇긴 해도", "bargain": "흥정하다, 특가품",
    "throng": "모여들다", "tattered": "너덜너덜한", "clad": "옷을 입은", "dainty": "앙증맞은",
    "strew with": "~으로 뒤덮다", "stingy": "구두쇠의", "negligible": "무시해도 될 정도의", 
    "remodel": "개조하다", "faint": "희미한", "priceless": "매우 귀중한"
}

voca_14 = {
    "legitimate": "합법적인", "fraudulent": "사기의", "file a complaint": "고소하다", "suspect": "용의자",
    "apprehend": "체포되다, 파악하다", "plead": "변론하다", "convict a of b": "B에 대해 A에게 유죄를 선고하다",
    "take ~ for a ride": "~를 속이다", "fabricate": "위조하다", "sentence": "선고하다", "penalize": "벌주다",
    "take in": "속이다, 흡수하다", "final ruling": "최종 판결", "exonerate": "혐의를 풀어주다",
    "breach": "위반하다", "extenuate": "정상 참작하다", "allegation": "혐의", "condone": "용서하다",
    "infringement": "침해", "reiterate": "반복하다", "retain": "보유하다", "smuggle": "밀수하다",
    "impartial": "공정한", "repeal": "폐지하다", "exercise": "행사하다", "sequester": "격리하다",
    "bribery": "뇌물 수수", "incarcerate": "감금하다", "reprieve": "형 집행을 유예하다", "illicit": "불법의",
    "jurisdiction": "권한", "deliberate on": "~를 숙고하다", "proliferation": "확산", "sneak in": "몰래 들어가다",
    "finagle": "속임수를 쓰다", "infraction": "위반", "accomplice": "공범", "withhold": "보류하다",
    "reprimand": "징계하다", "commit": "저지르다, 전념하다", "violate": "위반하다", "rescind": "폐지하다",
    "be saddled with": "짐을 지다", "clemency": "관용", "deter from": "~하는 것을 저지하다", "evade": "피하다",
    "forge": "위조하다, 구축하다", "legal": "합법적인", "probe": "조사하다"
}

voca_15 = {
    "dabble in": "~을 취미 삼아 해보다", "get in shape": "좋은 몸 상태를 유지하다", "assess": "평가하다",
    "stretch": "뻗다, 펼쳐지다", "gasping": "헐떡거리는", "work out": "운동하다, 잘 풀리다", "dart": "쏜살같이 달리다",
    "avid": "열렬한", "dull": "지루한, 흐리게하다", "meticulous": "세심한", "contentious": "다투기 좋아하는",
    "dodge": "재빨리 피하다", "feeble": "미미한", "alacrity": "민첩", "keep up with": "유행을 따르다",
    "demoralize": "사기를 꺾다", "double over": "몸을 웅크리다", "outpace": "앞지르다", "nimble": "재빠른",
    "fluke": "뜻밖의 행운", "cup of tea": "좋아하는 것", "valid": "유효한, 타당한", "get along with": "사이좋게 지내다",
    "apparent": "명백한, 외관상의", "brisk pace": "활발한 걸음", "coveted": "탐내는", "outdo": "~보다 뛰어나다",
    "bar": "금지하다", "enthusiasm": "열광", "ascent": "오름", "deft": "능숙한", "beat": "이기다",
    "compel": "억지로 시키다", "distinguish": "구분하다", "give it a try": "시도하다", "parachute": "낙하산",
    "rivalry": "경쟁", "spent": "지쳐버린"
}

voca_16 = {
    "revere": "숭배하다", "significant": "중대한, 상당한", "pilgrimage": "성지 순례", "congregate": "모이다",
    "convention": "관습, 집회", "subsequently": "그 후에", "secular": "비종교적인", "rigid": "엄격한, 완고한",
    "resolve": "해결하다, 다짐하다", "conform": "따르다", "dwell on": "숙고하다", "ground": "근거",
    "basis": "근거", "repel": "물리치다", "be devoted to": "~에 헌신하다", "leeway": "자유",
    "ascetic": "금욕적인", "in the same vein": "같은 맥락에서", "sophisticated": "복잡한, 약삭빠른",
    "veracity": "진실", "transient": "덧없는", "monotheism": "유일신교", "ignorant": "무지한",
    "supplant": "대체하다", "commemoration": "기념", "superficial": "피상적인", "constitute": "~이 되다, 구성하다",
    "uphold": "지지하다", "abstruse": "난해한", "undermine": "서서히 약화시키다", "infallible": "절대 오류가 없는",
    "instill": "사상을 주입하다", "adhere": "고수하다", "martyr": "순교자", "Buddhism": "불교",
    "cathedral": "대성당", "Christianity": "기독교", "Confucianism": "유교", "conscientious": "양심적인",
    "faithful": "충실한", "fundamental": "근본적인", "immoral": "부도덕한", "Jewish": "유대인의",
    "Judaism": "유대교", "Muslim": "무슬림", "Protestantism": "개신교", "rational": "이성적인",
    "solemn": "엄숙한", "vice": "악덕 행위", "virtue": "미덕", "worship": "숭배하다"
}

voca_17 = {
    "unbearable": "참을 수 없는", "compelling": "주목할만한", "crack up": "웃음을 터뜨리다", "remorse": "후회",
    "red herring": "중요한 사안에서 벗어나는 것", "candor": "정직", "initiative": "솔선, 발안, 독창성",
    "clout": "영향력", "clam up": "침묵하다", "tepid": "열의 없는", "vilify": "비난하다", "dearth": "부족",
    "trait": "특징", "bark up the wrong tree": "잘못 짚다", "conflate": "혼합하다", "slate": "예정하다",
    "facile": "술술 하는", "replete with": "~로 가득찬", "relevant to": "~과 관련된", "drag on": "질질 끌다",
    "hoodwink": "속이다", "scorn": "비웃다", "inform a of b": "알리다", "pirate": "저작권 침해하다",
    "indiscreet": "경솔한", "inane": "무의미한", "limelight": "각광", "turn out": "~임이 밝혀지다",
    "pique": "흥미를 불러일으키다, 화나게 하다", "ornery": "심술궂은", "pervasive": "퍼지는", "aspire": "열망하다",
    "recreate": "재현하다", "frank": "솔직한", "generalization": "일반화", "mislead": "잘못 인도하다",
    "misleading": "허위의", "obvious": "명백한", "touching": "감동적인", "without a doubt": "의심할 여지없이"
}

voca_18 = {
    "accomplished": "뛰어난", "sculpt": "조각하다", "usher": "안내하다", "represent": "나타내다, 대표하다",
    "depict": "묘사하다", "put in one’s two cents": "자기 의견을 말하다", "perspective": "원근법, 관점",
    "vandalism": "고의적 파괴", "adroit": "능숙한", "embrace": "채택하다", "inscrutable": "수수께끼 같음",
    "purport": "주장하다", "predilection": "편애", "patron": "후원자, 단골손님", "applaud": "박수갈채를 보내다",
    "esoteric": "난해한", "impromptu": "즉흥적인", "dupe": "속이다", "steal the show": "관심을 독차지하다",
    "doodle": "낙서를 끄적거리다", "phony": "가짜", "play down": "강조하지 않다", "improvise": "즉흥적으로 하다",
    "adorn": "장식하다", "lavish": "사치스러운", "be composed of": "~로 구성되다", "belittle": "경시하다",
    "in the mood": "~할 기분인", "contrast": "대조", "portrayal": "묘사", "aesthetic": "심미적인",
    "carve": "새기다", "dye": "염색하다", "elaborate": "정교한", "house": "수용하다, 소장하다",
    "imitate": "흉내내다", "pottery": "도자기", "tasteful": "멋을 아는", "vivid": "선명한"
}

voca_19 = {
    "admire": "감탄하다", "itinerary": "여행 일정", "scenic": "아름다운", "resort": "수단, 의지하다",
    "end up": "결국 ~하게되다", "regarding": "~에 관해서", "rock the boat": "소란을 일으키다",
    "compromise": "타협하다, 위태롭게 하다", "count on": "~을 기대하다", "round off": "완료하다",
    "sojourn": "체류", "maroon": "고립시키다", "sympathize": "공감하다", "look back on": "되돌아보다",
    "run up against": "~에 맞닥드리다", "in a pinch": "위기를 맞은", "play it by ear": "그때그때 봐서 처리하다",
    "rejuvenate": "원기를 회복시키다", "punctual": "시간을 잘 지키는", "anticipate": "기대하다",
    "stick with": "~와 함께 있다", "allure": "매력, 끌어들이다", "mingle with": "~와 어울리다",
    "intrigue": "~의 흥미를 돋우다, 음모", "comprehensive": "종합적인", "overtake": "따라잡다",
    "hail from": "~출신이다", "quaint": "색다른", "misgiving": "불안", "candid": "솔직한",
    "fascinated": "매료된", "fatigue": "피로", "fork": "갈라지다", "idle": "게으른",
    "room": "여유", "sightseeing": "관광", "take a for granted": "A를 당연시하다"
}

voca_20 = {
    "remote": "리모컨, 외딴", "feasible": "실현 가능한", "hoist": "들어 올리다", "potent": "강력한",
    "act up": "제대로 작동하지 않다", "displace": "대체하다", "enable": "가능하게 하다",
    "emblazon": "장식하다", "gear": "요구에 맞게 조정하다", "obviate": "제거하다",
    "breakthrough": "획기적인 발견", "work the system": "자기에게 맞게 작동시키다", "immaculate": "완벽한",
    "viable": "실행 가능한", "dud": "실패작", "ubiquitous": "흔한", "on one’s last legs": "거의 망가진",
    "controversial": "논란의 여지가 있는", "boon": "혜택", "strive": "노력하다", "plug away at": "꾸준히 하다",
    "secure": "안전한, 확보하다", "durable": "내구성이 있는", "play a role in": "~하는 역할을 하다",
    "generate": "발생시키다", "erect": "건설하다", "reliability": "신뢰성", "utility": "공공시설",
    "infrastructure": "기반 시설", "handy": "유용한", "intuitive": "직관적인", "built-in": "내장된",
    "lightweight": "경량의", "out of order": "고장난", "outdated": "구식의", "up-to-date": "최신식의"
}

voca_21 = {
    "furnished": "가구가 비치된", "revamp": "개조하다", "wrap": "포장하다, 끝내다", "rummage": "샅샅이 뒤지다",
    "stuffy": "숨 막히는", "vacate": "비우다", "austere": "소박한", "evict": "쫓아내다", "embed": "박아 넣다",
    "tenant": "세입자", "landlord": "집주인", "stark": "삭막한, 냉혹한, 극명한", "tinker": "어설프게 고치다",
    "undo": "매듭을 풀다", "hit the hay": "잠자리에 들다", "incineration": "소각", "groom": "손질하다",
    "adequate": "충분한", "settle into": "정착하다", "settle on": "결정하다", "adjust to": "적응하다",
    "inhabitant": "주민", "enhance": "향상시키다", "move": "제안하다", "foreclosure": "압류",
    "sublet": "재임대하다", "real estate": "부동산", "tidy": "정돈된", "urban": "도시의", "wardrobe": "옷장"
}

voca_22 = {
    "distraught": "완전히 제정신이 아닌", "console": "위로하다, 제어 장치", "assuage": "감정을 누그러뜨리다, 식욕을 채우다",
    "eulogize": "칭송하다", "uneasy": "불안한", "smoothing": "달래는", "capricious": "변덕스러운",
    "be hostile to": "~에게 적대적이다", "long for": "바라다", "have confidence in": "~를 신뢰하다",
    "be confidence about": "~를 확신하다", "indulge in": "빠지다", "stubborn": "고집이 센", "blow up": "화내다",
    "penchant": "기호", "simmer down": "진정하다", "contemplate": "숙고하다", "unabashed": "뻔뻔한",
    "indifferent in": "무관심한", "yearn": "갈망하다", "qualm": "양심의 가책", "engender": "불러일으키다",
    "set off": "화나게 하다", "dejected": "낙담한", "aloof": "냉담한", "wayward": "말을 안듣는",
    "prudence": "신중", "bristle": "발끈하다", "droopy": "의기소침한", "glower at": "노려보다",
    "incensed": "몹시 화난", "a load off one’s mind": "마음의 짐을 더는", "vacillate": "망설이다",
    "perturb": "혼란시키다", "temper": "성질, 누그러뜨리다", "conceal": "감추다", "irksome": "짜증 나는",
    "refractory": "고집 센", "cantankerous": "심술궂은", "grin": "활짝 웃다", "impertinent": "무례한",
    "sneer": "비웃다", "relieved": "안도한", "pessimistic": "비관적인", "budge": "의견을 바꾸다",
    "secluded": "은둔한", "thunderstruck": "깜짝 놀란", "scowl": "얼굴을 찌푸리다", "despair": "절망하다",
    "hesitate": "망설이다", "homesick": "향수에 잠긴", "painful": "정신적으로 괴로운", "pretend": "~인 척이다",
    "pretentious": "자만하는", "suspicion": "의심", "tendency": "경향", "terrified": "겁먹은"
}

voca_23 = {
    "audit": "회계 감사하다, 청강하다", "knowledgeable": "정통한", "approve": "승인하다", "discipline": "학과, 징계",
    "stir up": "고무하다", "admit": "인정하다", "salient": "중요한", "tardy": "지각한", "accolade": "칭찬",
    "grant": "보조금, 수여하다", "suspend": "중지하다, 정학시키다", "inculcate": "사상을 심어 주다", "jot down": "적다",
    "precocious": "발달이 빠른", "tick": "체크표시를 하다", "paragon": "모범", "spell out": "~을 분명히 설명하다",
    "turn ~ away": "돌려보내다", "wet behind the ears": "미숙한", "rudimentary": "기초적인", "in hindsight": "지나고 보니",
    "chastise": "벌하다", "institute": "제정하다, 연구소", "cumulative": "누적되는", "due": "~하기로 되어 있는, 지불 기일이 된",
    "turn in": "잠자리에 들다, 제출하다", "catch on": "이해하다", "run over": "빠르게 훑어보다", "faculty": "교수진, 기능",
    "show ~ the ropes": "~에게 요령을 알려주다", "prestigious": "일류의", "statistics": "통계, 통계학", "prospective": "예비의",
    "acquire": "습득하다", "acquired": "후천적인", "bring up": "양육하다, 화제를 꺼내다", "restrain": "억제하다", "term paper": "학기말 리포트"
}

voca_24 = {
    "spot": "찾아내다", "on the spot": "즉석에서", "stem from": "유래하다", "abnormal": "비정상적인",
    "inherit": "물려받다", "hand down to": "물려주다", "stunt": "저해하다", "indigenous": "원산의",
    "alert": "기민한, 경고하다", "eradicate": "박멸하다", "regulate": "조절하다", "docile": "온순한",
    "innate": "타고난", "perish": "소멸하다", "tether": "밧줄로 매어 놓다", "extraneous": "외부에서 발생한",
    "shrivel": "시들다", "forage": "식량을 찾아다니다", "decoy": "미끼", "flap": "퍼덕거리다", "gill": "아가미",
    "ingest": "섭취하다", "attribute a to b": "B의 탓으로 돌리다", "factor": "고려하다", "lure": "유혹하다",
    "sprout": "싹이 나다", "evolve": "진화하다", "confront": "직면하다", "susceptible": "취약한", "instinct": "본능",
    "predator": "포식자", "correlation": "상관관계", "mature": "성숙한", "dominant": "지배적인", "magnify": "확대하다",
    "bough": "나무 가지", "give birth to": "~의 원인이 되다, 낳다", "hatch": "부화하다", "hide": "가죽",
    "life span": "수명", "majority": "대부분", "mammal": "포유동물", "meadow": "초원", "stalk": "줄기, 스토킹하다"
}

voca_25 = {
    "inferior": "열등한", "enterprise": "기업, 모험", "underpin": "근거를 대다", "preempt": "선매권에 의해 획득하다, 예방하다",
    "initiate": "시작하다", "on strike": "파업중인", "influx": "유입", "endorse": "지지하다",
    "estimate": "견적하다, 평가하다, 견적", "pragmatic": "실용적인", "renege": "어기다", "stammer": "말을 더듬다",
    "pull off": "성사시키다", "financial transaction": "금융 거래", "indication": "징조", "portion": "부분",
    "daunt": "기세를 꺾다", "daunting work": "벅찬 업무", "shrewd": "통찰력 있는", "berate": "질책하다",
    "knock the socks off": "큰 영향을 미치다", "let down": "실망시키다", "presentable": "외모가 단정한", "foray": "진출",
    "attain": "달성하다", "asset": "재산, 강점", "grasp": "이해하다, 기회를 잡다", "boost": "증대시키다, 후원하다",
    "commence": "시작하다", "post": "직책", "win over": "설득하다", "divvy up": "분배하다",
    "page": "안내 방송을 하다", "subservient": "복종하는", "occur to": "~에게 생각이 떠오르다", "commerce": "상업",
    "executive": "임원, 행정적인", "export": "수출하다", "import": "수입하다", "favorable": "호의적인",
    "firm": "단단한, 회사", "patent": "~의 특허를 취득하다", "possess": "소유하다", "questionnaire": "설문지",
    "smoothly": "순조롭게", "take advantage of": "이용하다", "venture": "사업, 위험을 무릅쓰고 하다"
}

voca_26 = {
    "dissolve": "용해하다", "compound": "혼합물, 혼합하다", "volatile market": "변동성이 큰 시장", "precaution": "예방책",
    "phase out": "단계적으로 폐지하다", "dilute": "희석하다", "go haywire": "이상해지다", "concede": "인정하다",
    "hasten": "촉진하다", "convince": "설득하다", "assume": "떠맡다, 가정하다", "affirm": "단언하다",
    "extensive": "광범위한", "undergo": "치료를 받다, 겪다", "hypothesis": "가설", "indisputable": "반론의 여지가 없는",
    "neutralize": "상쇄하다", "unadulterated": "순수한", "formidable": "어마어마한", "penetrate": "통과하다",
    "sterilize": "살균하다, 중성화하다", "exude": "풍기다", "motion": "제안", "agitate": "흔들다, 동요시키다",
    "conductive": "전도성의", "objective": "목표, 객관적인", "subjective": "주관적인", "function as": "~의 역할을 하다",
    "equivalent to": "~에 상응하는", "as a whole": "전체로서", "dense": "조밀한", "examine": "조사하다",
    "figure out": "이해하다", "gradual": "점진적인", "proportion": "비율", "quantity": "양", "solidify": "응고시키다"
}

voca_27 = {
    "cordially": "정중히", "audible": "들을 수 있는", "connection": "전화 연결", "eventually": "마침내",
    "immediately": "즉시", "transmit": "보내다", "hectic": "몹시 바쁜", "impetus": "자극",
    "burgeon": "급증하다", "coincidence": "우연의 일치", "arrangement": "합의", "relay": "중계하다",
    "shoot the breeze": "수다를 떨다", "show off": "자랑하다", "vex": "짜증나게 하다", "get through": "연락이 되다",
    "i’ll put you through.": "전화를 연결해드리겠습니다.", "give ~ a shot": "~을 시도하다", "exceed": "초과하다", "emulate": "모방하다",
    "solicit": "요청하다", "broach": "발의하다", "urgent": "긴급한", "terminate": "종료하다",
    "extension": "내선번호, 확장", "trivial": "사소한", "prematurely": "너무 이르게", "hang up on": "갑자기 전화를 끊다",
    "corrupt": "오류를 일으키다", "recipient": "수령인", "intermittent": "간헐적으로 끊기는", "novelty": "신기한 물건",
    "advent": "출현", "be on the phone": "통화 중이다.", "get in touch with": "~와 연락하다", "noted": "저명한",
    "on a daily basis": "매일", "on another line": "다른 전화를 받고 있는", "payphone": "공중전화", "so far": "지금까지",
    "vast": "막대한"
}

voca_28 = {
    "terrain": "지형", "desolate": "황량한", "intense": "강렬한", "detect": "발견",
    "detective": "형사", "observe": "말하다, 준수하다", "illuminate": "밝히다", "erupt": "폭발하다, 이가 나다",
    "have impact on": "~에영향을 주다", "record": "기록적인", "rift": "균열", "impact": "충돌, 영향",
    "shape": "형성하다", "shrink": "수축하다", "unravel": "(의문을) 풀다", "despondent": "낙담한",
    "mystify": "당황하게 하다", "incontrovertible": "논란의 여지가 없는", "innovative": "혁신적인", "in effect": "실제로는",
    "assert": "주장하다", "definite": "명확한", "exploit": "활용하다, 착취하다", "spawn": "낳다",
    "tangible": "명확한", "substitute": "대신하다, 대용품", "conceive": "생각하다, 임신하다", "erode": "부식시키다",
    "repository": "지식의 보고", "altitude": "고도", "akin to": "유사한", "massive": "대규모의",
    "quest": "탐구", "comet": "혜성", "lengthy": "너무 긴", "satellite": "인공위성",
    "suggest": "암시하다", "surface": "떠오르다"
}

voca_29 = {
    "ethnic": "민족의", "snob": "속물", "besiege": "포위하다", "shirk": "회피하다",
    "laud": "칭송하다", "compulsory": "강제적인", "compulsive": "강박적인, 상습적인", "assimilate": "동화되다",
    "disclose": "폭로하다", "tolerant": "관대한", "falter": "주춤하다", "ostracize": "배척하다",
    "scarcity": "부족", "deficiency": "결핍", "negligent": "태만한", "reclusive": "은둔한",
    "indigence": "빈곤", "discrimination": "차별", "racial": "인종의", "clandestinely": "비밀리에",
    "coarse": "천한", "eclectic": "폭넓은", "stupor": "아연실색, 인사불성", "neatly": "단정하게",
    "obnoxious": "아주 불쾌한", "redundant": "불필요한, 중복된", "wedlock": "혼인", "disown": "의절하다",
    "oblivious": "알지 못하는", "skirt": "피하다", "pose": "야기하다", "inveigle": "속이다",
    "status": "지위", "clamor": "강력히 요구하다", "tarry": "늦어지다", "privilege": "특권",
    "acknowledge": "인정하다", "acknowledge receipt of": "도착을 알리다", "disseminate": "유포하다", "emit": "방출하다",
    "citizenship": "시민권", "exclude": "제외하다", "funeral": "장례식", "get used to": "~에 익숙해지다",
    "identical": "동일한", "infancy": "유아기", "infant": "유아", "not to mention": "말할 것도 없이",
    "orphan": "고아, 고아로 만들다", "orphanage": "고아원", "persuasive": "설득력 있는", "racket": "소음"
}

voca_30 = {
    "poacher": "밀렵꾼", "conserve": "절약하다, 보존하다", "endangered": "멸종 위기에 처한", "noxious": "유해한",
    "fume": "연기", "landfill": "매립지", "extinction": "멸종", "continuity": "지속성, 연관성",
    "appreciate": "가치를 인정하다", "disposable": "일회용의", "dispose": "처리하다", "distinctive": "독특한",
    "adverse": "부정적인", "averse": "싫어하는", "adolescence": "청소년기", "deplete": "고갈시키다",
    "deficiency": "부족", "petroleum": "석유", "make up for": "보충하다", "subject": "국민, 시달리게 하다",
    "be subject to": "~하기 쉽다", "be subjected to": "당하다", "consequence": "결과", "tributary": "지류",
    "harsh": "가혹한", "filthy": "더러운", "ameliorate": "개선하다", "inimical": "해로운",
    "litter": "어지르다", "derelict": "유기된", "vestige": "흔적", "productive": "비옥한, 생산적인",
    "peter out": "점차 작아지다", "acquiescence": "묵인", "outrage": "폭발", "run out of": "고갈되다",
    "fertile": "비옥한", "futile": "헛된", "vortex": "소용돌이", "grime": "먼지",
    "straddle": "가로지르다", "reverse": "되돌리다", "deteriorate": "악화되다", "awareness": "자각",
    "bring about": "야기하다", "causal": "원인이 되는", "conduct": "수행하다", "decline": "쇠퇴하다, 거절하다",
    "harmless": "무해한", "harmonization": "조화", "purify": "정화하다", "wastewater": "폐수",
    "uniqueness": "독특성"
}

# ==========================================
# 2. 상급 단어 데이터 (상급 1과 ~ 상급 8과)
# ==========================================
adv_voca_1 = {
    "ascertain": "확인하다", "deviate": "벗어나다, 빗나가다", "elapse": "경과하다",
    "alternate": "대신의, 교대의, 교대하다", "alter": "바꾸다", "awkward": "어색한",
    "inept": "솜씨 없는", "behind the wheel": "운전하여", "sober": "술 취하지 않은, 엄숙한",
    "drive under the influence": "술 취한 채 운전하다", "break down": "고장나다, 분해하다",
    "dent": "움푹 들어가게 하다, 움푹 들어간 곳", "detach": "분리시키다", "pick up the tab": "돈을 지불하다",
    "impassable": "지나갈 수 없는", "intact": "멀쩡한", "pass through": "~를 통과하다",
    "pedestrian": "보행자", "yield": "양보하다, 이익을 내다", "milestone": "중요한 사건",
    "shortcut": "지름길", "steer": "조종하다", "toll": "통행료, 사상자 수",
    "take a toll": "피해를 입다", "tow": "견인하다", "wear down": "마모되다",
    "attrition": "마찰", "callous": "냉담한", "hamper": "방해하다",
    "thwart": "좌절시키다", "wobble": "흔들흔들하다", "enumerate": "열거하다"
}

adv_voca_2 = {
    "amass": "축적하다", "score a goal": "득점하다", "deduct": "감하다", "dispense": "나눠주다",
    "allocate": "할당하다", "beneficiary": "수혜자", "premium": "보험료",
    "booming": "급속히 발전하는", "sluggish": "부진한", "consolidate": "통합하다",
    "mogul": "거물", "tycoon": "거물", "downturn": "침체", "fall short of expectation": "기대에 미치지 못하다",
    "impoverished": "빈곤에 처한", "incur": "초래하다", "make ends meet": "손익분기점을 맞추다",
    "moonlight": "부업하다", "rosy": "낙관적인", "optimistic": "낙관적인",
    "self-sufficiency": "자급 자족", "stagnation": "침체", "surplus": "흑자",
    "shortfall": "감소", "tactics": "책략", "gimmick": "책략", "withdrawal": "인출, 철수",
    "up to": "~까지", "affluent": "풍부한", "bolster": "지지하다, 강화하다", "curtail": "줄이다",
    "insolvent": "파산한", "default": "채무 불이행", "reckless": "무분별한", "prodigal": "낭비하는",
    "pension": "연금", "scrimp": "절약하다", "sumptuous": "낭비하는", "squander": "흥청망청 쓰다"
}

adv_voca_3 = {
    "brew": "(차를) 끓이다", "complement": "보충하다", "detract": "(질을) 떨어뜨리다", "detractor": "가치를 폄하하는 사람",
    "craving": "갈망", "condemn": "비난하다", "decay": "부패하다, 부패", "enrich": "풍부하게 하다",
    "dissuade": "만류하다", "fast": "단식하다, 단식", "famine": "기근", "intake": "섭취",
    "mince": "잘게 다지다", "mouth-watering": "군침이 도는", "run-of-the-mill": "너무 평범한", "spine-tingling": "등골이 오싹한",
    "ripe": "(과일이) 익은", "sip": "한 모금 마시다, 한 모금", "swallow": "삼키다, 억누르다", "inhale": "숨을 들이마시다",
    "corpulent": "비만의", "plump": "통통한", "fermentation": "발효", "grab a bite": "간단히 먹다",
    "pasteurize": "저온 살균하다", "split the bill": "더치페이하다", "hit the hay": "잠자리에 들다", "abstemious": "자제하는",
    "supple": "유연한", "repugnant": "비위 상하는", "poultry": "가금류", "thaw": "해동시키다", "stale": "상한, 진부한"
}

adv_voca_4 = {
    "anonymous": "익명의", "unanimous": "만장일치의", "ambiguous": "애매한", "chronicle": "시간순으로 기록하다",
    "cohesive": "응집력 있는", "copious": "풍부한", "cut to the chase": "본론으로 들어가다", "Don’t beat around the bush.": "둘러 얘기하지 마.",
    "get away with it": "교묘하게 모면하다", "run up a bill": "청구서가 쌓이다", "lay down the law": "강압적으로 말하다", "eloquent": "말 잘하는",
    "loquacious": "말 많은", "orator": "웅변가", "encompass": "포함하다", "encyclopedia": "백과사전",
    "gist": "요점", "guts": "요점", "ironic": "아이러니한", "satirical": "풍자적인",
    "satire": "풍자", "naive": "순진한", "novice": "초보", "nonverbal": "비언어적인",
    "unsurpass": "능가하다", "protagonist": "주인공", "antagonist": "적수", "readership": "독자",
    "ridership": "승객", "synonymous": "동의어의", "vague": "애매한", "jovial": "쾌활한",
    "allude": "암시하다", "decipher": "해독하다", "encrypt": "암호화하다", "make out": "알아듣다",
    "succinct": "간결한", "lucid": "명료한", "verbose": "말이 많은", "confound": "당황한",
    "simultaneous": "동시의", "denote": "나타내다", "mordant": "신랄한"
}

adv_voca_5 = {
    "condensed": "응축된", "drained": "지친", "adverse effect": "부정적인 영향", "averse": "싫어하는",
    "aversion": "혐오", "quench": "적시다, 갈증을 해소하다", "gauge": "측정하다, 평가하다", "be accustomed to": "~에 익숙하다",
    "optimal": "최적의", "immense": "엄청난", "downpour": "폭우", "likelihood": "가능성",
    "be likely to": "~할 것 같다", "precipitation": "강수량", "meteorologist": "기상학자", "meteor": "유성",
    "prolong": "연장하다", "dry spell": "건기", "shimmer": "반짝이다", "shiver": "떨다",
    "dispel": "없애버리다", "expel": "쫓아내다", "fringe": "주변", "fringe benefit": "부가 혜택",
    "cold front": "한랭 전선", "gust": "돌풍", "ignite": "불을 붙이다", "in favor of": "~에 찬성하여",
    "fall out of favor": "인기가 떨어지다", "poll": "여론조사", "inclement": "날씨가 나쁜", "fortuitous": "행운의",
    "static": "정적인", "erratic": "불규칙한", "under the weather": "몸이 안좋은", "on the ball": "유능한",
    "ample": "충분한", "innumerable": "셀 수 없는", "residual": "남은", "ensue": "계속되다",
    "abruptly": "갑자기", "drastic": "급격한", "phenomenal": "경이로운", "variable": "변하기 쉬운, 변수",
    "in terms of": "~에 있어서, ~에 관하여"
}

adv_voca_6 = {
    "accord": "동의", "in accordance with": "~에 부합하여", "alliance": "동맹", "ally": "동맹국",
    "allies": "연합국", "assassinate": "암살하다", "conspiracy": "음모", "overthrow": "전복시키다",
    "exile": "추방, 추방하다", "hegemony": "힘", "incite": "자극하다", "verdict": "판결",
    "riot": "폭동", "intervention": "간섭, 중재", "mediate": "중재하다", "menace": "위협",
    "nominate": "지명하다", "pacify": "진정시키다", "preliminary": "예비의", "revoke": "폐지하다",
    "minor": "미성년자", "run for": "입후보하다", "sovereignty": "자치권", "supremacy": "힘",
    "abdicate": "퇴임하다", "throne": "왕좌", "collusion": "공모", "manipulate": "조작하다",
    "evasive": "회피적인", "bring into": "소환하다", "impeach": "탄핵하다", "acquit": "무죄를 입증하다",
    "inception": "시작", "ostensible": "표면적인", "precursor": "전조, 선구자", "serve as": "~의 역할을 하다",
    "predecessor": "전임자", "subvert": "전복시키다", "faction": "당파", "manifest": "나타나다",
    "proponent": "지지자", "allegedly": "전해진 바에 의하면", "mollify": "진정시키다"
}

adv_voca_7 = {
    "by no means": "결코 ~이 아니다", "by all means": "물론", "embark": "탑승하다, 승선하다",
    "disembark": "내리다", "dread": "두려워하다", "eminent": "저명한", "prominent": "유명한",
    "in the nick of time": "때맞춰", "on the up and up": "승승장구 하는", "at the drop of a hat": "주저하지 않고",
    "make amends": "보상하다", "nausea": "구역질", "vomit": "토하다", "throw up": "토하다",
    "handheld": "휴대용", "no strings attached": "무조건의", "indefinitely": "무기한으로",
    "once and for all": "최종적으로", "one of a kind": "독특한 것", "retrieve": "되찾다",
    "sneaky": "몰래 하는, 비열한", "straightforward": "간단한, 솔직한", "weary": "지치게 하다, 지친",
    "ambience": "분위기", "concierge": "안내 직원", "confiscate": "압수하다", "raid": "급습",
    "on the premises": "부지 내", "confide": "신뢰하다", "disparage": "비하하다", "interrogate": "심문하다",
    "defer": "연기하다", "deter": "방해하다", "fastidious": "까다로운, 꼼꼼한", "impede": "방해하다",
    "linger": "꾸물거리다", "queasy": "구역질 나는", "bent over at the waist": "허리를 구부리다",
    "vociferous": "큰 소리로 외치는", "tempting": "솔깃한", "assail": "공격하다", "quarantine": "격리하다",
    "unobtrusively": "지나치지 않게"
}

adv_voca_8 = {
    "abate": "약해지다", "wane": "약해지다", "lessen": "줄이다", "abortion": "낙태, 유산",
    "ailment": "병", "arthritis": "관절염", "anorexia": "거식증", "asthma": "천식",
    "contagious": "전염성의", "cardiovascular disease": "심혈관 질환", "epidemic": "전염병, 유행성의",
    "fetus": "태아", "expectant mother": "산모", "fracture": "골절, 골절되다", "cast": "깁스",
    "inhale": "숨을 들어마시다", "exhale": "숨을 들이내쉬다", "insomnia": "불면증", "numb": "마비된, 마비시키다",
    "over-the-counter": "처방전 없이 살 수 있는", "perspiration": "땀", "sanitation": "위생",
    "germ": "세균", "vaccinate": "예방 접종을 하다", "abrasion": "찰과상", "acupuncture": "침술",
    "anesthetic": "마취제", "administer": "투여하다, 경영하다", "euthanasia": "안락사",
    "exacerbate": "악화시키다", "inflammation": "염증", "recuperate": "회복하다",
    "exhaustive": "철저한, 소모적인", "diarrhea": "설사", "respiratory": "호흡기의",
    "autopsy": "검시", "malady": "병", "virulent": "악성의"
}

# ==========================================
# 3. 전체 단어 사전 연동 (기본 단어 + 상급 단어 모두 통합)
# ==========================================
all_basic_voca = {
    **voca_1, **voca_2, **voca_3, **voca_4, **voca_5,
    **voca_6, **voca_7, **voca_8, **voca_9, **voca_10,
    **voca_11, **voca_12, **voca_13, **voca_14, **voca_15,
    **voca_16, **voca_17, **voca_18, **voca_19, **voca_20,
    **voca_21, **voca_22, **voca_23, **voca_24, **voca_25,
    **voca_26, **voca_27, **voca_28, **voca_29, **voca_30
}

all_adv_voca = {
    **adv_voca_1, **adv_voca_2, **adv_voca_3, **adv_voca_4,
    **adv_voca_5, **adv_voca_6, **adv_voca_7, **adv_voca_8
}

all_voca = {**all_basic_voca, **all_adv_voca}

# ==========================================
# 4. 상태(세션) 관리
# ==========================================
if 'quiz_state' not in st.session_state:
    st.session_state.quiz_state = 'selection' 
    st.session_state.word_list = []
    st.session_state.current_index = 0
    st.session_state.score = 0
    st.session_state.results = []
    st.session_state.current_voca_dict = {}

# ==========================================
# 5. 핵심 함수 (로직)
# ==========================================
def start_quiz(choice_dict):
    st.session_state.current_voca_dict = choice_dict
    st.session_state.word_list = list(choice_dict.keys())
    random.shuffle(st.session_state.word_list)
    st.session_state.current_index = 0
    st.session_state.score = 0
    st.session_state.results = []
    st.session_state.quiz_state = 'input'

def start_retake():
    st.session_state.word_list = [res["word"] for res in st.session_state.results if not res["is_correct"]]
    random.shuffle(st.session_state.word_list)
    st.session_state.current_index = 0
    st.session_state.score = 0
    st.session_state.results = []
    st.session_state.quiz_state = 'input'

def submit_answer():
    st.session_state.user_answer = st.session_state.answer_input
    st.session_state.quiz_state = 'eval'

def mark_answer(is_correct):
    current_word = st.session_state.word_list[st.session_state.current_index]
    correct_meaning = st.session_state.current_voca_dict[current_word]
    
    if is_correct:
        st.session_state.score += 1
        
    st.session_state.results.append({
        "word": current_word,
        "user_input": st.session_state.user_answer,
        "correct_meaning": correct_meaning,
        "is_correct": is_correct
    })
    
    st.session_state.current_index += 1
    if st.session_state.current_index >= len(st.session_state.word_list):
        st.session_state.quiz_state = 'result'
    else:
        st.session_state.quiz_state = 'input'

def mark_incorrect():
    mark_answer(False)
    
def mark_correct():
    mark_answer(True)

def go_home():
    st.session_state.quiz_state = 'selection'

# ==========================================
# 6. 화면(UI) 그리기
# ==========================================
st.title("📖 나만의 영단어 암기장")

# --- [단원 선택 화면] ---
if st.session_state.quiz_state == 'selection':
    st.subheader("모든 단어 통합 학습")
    
    if st.button("🌟 전체 단어 통합 학습 (기본 + 상급)", type="primary", use_container_width=True):
        start_quiz(all_voca)
        
    st.write("---")
    
    st.subheader("🔥 상급 단어 (1~8과)")
    adv_chapters = [
        ("상급 1과", adv_voca_1), ("상급 2과", adv_voca_2), ("상급 3과", adv_voca_3),
        ("상급 4과", adv_voca_4), ("상급 5과", adv_voca_5), ("상급 6과", adv_voca_6),
        ("상급 7과", adv_voca_7), ("상급 8과", adv_voca_8)
    ]
    
    for i in range(0, len(adv_chapters), 3):
        cols = st.columns(3)
        for j in range(3):
            if i + j < len(adv_chapters):
                chap_name, voca_dict = adv_chapters[i + j]
                with cols[j]:
                    if st.button(chap_name, use_container_width=True):
                        start_quiz(voca_dict)
                        
    st.write("---")
    
    st.subheader("📚 기본 단어 (1~30과)")
    basic_chapters = [
        ("1과", voca_1), ("2과", voca_2), ("3과", voca_3), ("4과", voca_4), ("5과", voca_5),
        ("6과", voca_6), ("7과", voca_7), ("8과", voca_8), ("9과", voca_9), ("10과", voca_10),
        ("11과", voca_11), ("12과", voca_12), ("13과", voca_13), ("14과", voca_14), ("15과", voca_15),
        ("16과", voca_16), ("17과", voca_17), ("18과", voca_18), ("19과", voca_19), ("20과", voca_20),
        ("21과", voca_21), ("22과", voca_22), ("23과", voca_23), ("24과", voca_24), ("25과", voca_25),
        ("26과", voca_26), ("27과", voca_27), ("28과", voca_28), ("29과", voca_29), ("30과", voca_30)
    ]
    
    for i in range(0, len(basic_chapters), 3):
        cols = st.columns(3)
        for j in range(3):
            if i + j < len(basic_chapters):
                chap_name, voca_dict = basic_chapters[i + j]
                with cols[j]:
                    if st.button(chap_name, use_container_width=True):
                        start_quiz(voca_dict)

# --- [주관식 입력 화면] ---
elif st.session_state.quiz_state == 'input':
    total = len(st.session_state.word_list)
    current = st.session_state.current_index
    
    st.info(f"진행: {current + 1} / {total} | 현재 점수: {st.session_state.score}")
    
    current_word = st.session_state.word_list[current]
    st.markdown(f"<h1 style='text-align: center; font-size: 50px;'>{current_word}</h1>", unsafe_allow_html=True)
    
    with st.form(key='answer_form', clear_on_submit=True):
        st.text_input("한글 뜻을 입력하세요", key="answer_input")
        submit_btn = st.form_submit_button("확인 (Enter)")
        if submit_btn:
            submit_answer()
            st.rerun()

    st.button("메인 메뉴로", on_click=go_home)

    # 자동 포커싱을 위한 자바스크립트 주입
    components.html(
        """
        <script>
        const inputs = window.parent.document.querySelectorAll('input[type="text"]');
        if (inputs.length > 0) {
            inputs[0].focus();
        }
        </script>
        """,
        height=0
    )

# --- [채점 화면] ---
elif st.session_state.quiz_state == 'eval':
    current_word = st.session_state.word_list[st.session_state.current_index]
    correct_meaning = st.session_state.current_voca_dict[current_word]
    user_ans = st.session_state.user_answer
    
    st.markdown(f"<h1 style='text-align: center; font-size: 50px;'>{current_word}</h1>", unsafe_allow_html=True)
    st.error(f"내가 쓴 답: {user_ans}")
    st.success(f"**정답: {correct_meaning}**")
    
    st.write("---")
    st.write("채점해주세요 👇 (PC: 키보드 '0' 또는 '1'로 바로 채점)")
    
    col1, col2 = st.columns(2)
    with col1:
        st.button("❌ 오답 처리", use_container_width=True, on_click=mark_incorrect)
    with col2:
        st.button("⭕ 정답 처리", use_container_width=True, on_click=mark_correct)

    # 단축키(0, 1) 적용을 위한 자바스크립트 주입
    components.html(
        """
        <script>
        const doc = window.parent.document;
        
        // 중복 실행을 막기 위해 이전 리스너 제거
        if (doc.quizKeyListener) {
            doc.removeEventListener('keydown', doc.quizKeyListener);
        }
        
        doc.quizKeyListener = function(e) {
            if (e.key === '0') {
                const btns = doc.querySelectorAll('button');
                btns.forEach(b => { if (b.innerText.includes('오답 처리')) b.click(); });
            } else if (e.key === '1') {
                const btns = doc.querySelectorAll('button');
                btns.forEach(b => { if (b.innerText.includes('정답 처리')) b.click(); });
            }
        };
        
        doc.addEventListener('keydown', doc.quizKeyListener);
        </script>
        """,
        height=0
    )

# --- [최종 결과 표 화면] ---
elif st.session_state.quiz_state == 'result':
    st.balloons()
    total = len(st.session_state.word_list)
    st.header(f"학습 완료! (점수: {st.session_state.score} / {total})")
    
    df = pd.DataFrame(st.session_state.results)
    df.columns = ["단어", "내가 쓴 답", "정답", "정답여부"]
    
    def color_wrong(val):
        color = '#ffebee' if not val else 'white'
        return f'background-color: {color}'
    
    styled_df = df.style.map(color_wrong, subset=['정답여부'])
    st.dataframe(styled_df, use_container_width=True)
    
    wrong_count = len(df[df["정답여부"] == False])
    
    col1, col2 = st.columns(2)
    with col1:
        st.button("🏠 처음으로", use_container_width=True, on_click=go_home)
    with col2:
        if wrong_count > 0:
            st.button(f"🔥 오답 재학습 ({wrong_count}개)", type="primary", use_container_width=True, on_click=start_retake)
