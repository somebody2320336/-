
import base64
import time
import streamlit as st
from PIL import Image, ImageEnhance
import pandas as pd
import streamlit.components.v1 as components  

page = st.sidebar.radio('我的首页', ['兴趣推荐', '历史人物志' , '图片处理', '智慧词典', '留言区'])

def bar_bg(img):
    last = 'jpg'
    st.markdown(
        f"""
        <style>
        [data-testid='stSidebar'] > div:first-child {{
            background: url(data:img/{last};base64,{base64.b64encode(open(img, 'rb').read()).decode()});
        }}
        </style>
        """,
        unsafe_allow_html = True,
    )

def page_bg(img):
    last = 'jpg'
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: url(data:img/{last};base64,{base64.b64encode(open(img, 'rb').read()).decode()});
            background-size: cover
        }}
        </style>
        """,
        unsafe_allow_html = True,
    )

bar_bg('背景.jpg')
page_bg('背景.jpg')

def page_1():
    st.title(':red[我的兴趣推荐]:clap:')
    st.write(' ')
    st.subheader(':blue[音乐推荐]')
    st.write(':blue[林俊杰-愿与愁]:point_down:')
    with open('愿与愁.mp3', 'rb') as f:
        mus = f.read()
    st.audio(mus, format='audio/mp3', start_time = 0)
    st.write(':blue[林俊杰-裂缝中的阳光]:point_down:')
    with open('裂缝中的阳光.mp3', 'rb') as h:
        mus_ = h.read()
    st.audio(mus_, format='audio/mp3', start_time = 0)
    st.write(':blue[邓紫棋-桃花诺]:point_down:')
    with open('桃花诺.mp3', 'rb') as u:
        mus_1 = u.read()
    st.audio(mus_1, format='audio/mp3', start_time = 0)
    st.write('-------------------------------------------')

    st.subheader(':green[电影推荐]')
    st.write(':green[《首尔之春》]:point_down:')
    st.write('这部影片以1979年12月12日发生的“双十二政变”作为背景，讲述了一个充满政治色彩的故事。故事从1979年10月26日朴正熙总统遇刺身亡这一重大历史时刻开始展开，生动再现了韩国在那段特殊时期经历的社会动荡和权力斗争。随着朴正熙去世后，掌握军权的郑昇和以及代理总统崔圭夏试图结束军人统治并推动国家向文官政府过渡。然而，朴正熙生前培养起来的一批忠实追随者如全斗焕等人对这种转变感到不满，并对处理朴正熙被刺杀案件的方式持有异议，因此密谋反对现有领导者。他们通过精心策划的秘密行动，挑战了当时的权力结构。')
    st.write('本片通过紧凑的情节安排和强烈的紧张氛围，深刻探讨了人性的复杂性和历史发展的必然趋势。同时，它还聚焦于政变之后韩国社会所经历的巨大变化、旧有体系崩溃以及普通士兵面对历史洪流时所作出的选择与牺牲。')
    vi = open('视.mp4', 'rb')
    vi_ = vi.read()
    st.video(vi_)
    col3, col4 = st.columns([2, 1])
    with col3:
        st.image('照.jpg')
    with col4:
        st.image('首尔.png')
    st.write('-------------------------------------------')

    st.subheader(':orange[书籍推荐]')
    col1, col2 = st.columns([1, 1])
    with col1:
        st.write(':orange[当年明月《明朝那些事儿》]:point_down:')
        st.write('《明朝那些事儿》是一部讲述中国明朝历史的故事作品，涵盖了从朱元璋出生到崇祯皇帝自缢明朝灭亡的整个时期。该作品以史料为基础，以年代和具体人物为主线，并加入了小说的笔法，语言生动诙谐，对明朝十七帝和其他王公权贵和小人物的命运进行全景展示，尤其对官场政治、战争、帝王心术着墨最多，并加入对当时政治经济制度、人伦道德的演义。')
    with col2:
        st.write(':orange[丁立梅《有美一朵向晚生香》]:point_down:')
        st.write('丁立梅十年经典散文自选集，分为"黄裙子，绿帕子""有一种爱叫相依为命""一天就是一辈子""小扇轻摇的时光""有美一朵，向晚生香""风过林梢""当华美的叶片落尽""花都开好了"等八辑，收录丁立梅经典散文和新作90篇。丁立梅文笔细腻，清新温婉;作品清新，意境隽永。在看似平淡寻常的小场景小事件中，传递着爱与感动。带你细品用音乐煮出的文字，用文字感怀温暖的人生。书中文章连续十年被选作中考试题。')
    col13, col14 = st.columns([1, 1])
    with col13:
        st.image('明朝.jpg')
    with col14:
        st.image('有美.jpeg')

def page_2():
    st.title(':red[历史人物志]:clap:')
    t1, t2, t3, t4, t5, t6 = st.tabs(['于谦', '毛泽东', '全斗焕', '丘吉尔', '古德里安', '人物集及问卷'])
    with t1:
        st.subheader(':orange[人物介绍]:point_down:')
        st.write('于谦（1398年5月13日－1457年2月16日），字廷益，号节庵，汉族，浙江杭州府钱塘县（今杭州市上城区）人。明朝名臣、民族英雄。')
        st.write('永乐十九年（1421年），于谦登进士第。宣德元年（1426年），以御史职随明宣宗平定汉王朱高煦之乱，因严词斥责朱高煦而受宣宗赏识，升为巡按江西，颂声满道。宣德五年（1430年），以兵部右侍郎巡抚河南、山西等地。明英宗时因入京觐见时不向权臣王振送礼，遭诬陷下狱，因两省百姓、官吏乃至藩王力请而复任。土木之变后，英宗兵败被俘，他力排南迁之议，坚请固守，升任兵部尚书。明代宗即位，整饬兵备，部署要害，亲自督战，率师二十二万，列阵北京九门外，抵御瓦剌大军。瓦剌太师也先挟英宗逼和，他以“社稷为重，君为轻”，不许。也先无隙可乘，被迫释放英宗。和议后，于谦仍积极备战，挑选京军精锐分十团营操练，又遣兵出关屯守，边境得以安宁。当时朝务繁杂，于谦独运征调，合乎机宜。其号令明审，令行政达。他忧国忘身，口不言功，平素俭约，居所仅能遮蔽风雨。但因个性刚直，招致众人忌恨。')
        col7, col8 = st.columns([1, 1])
        with col7:
            st.image('于谦.jpg')
        with col8:
            st.write('天顺元年（1457年），英宗复辟，大将石亨等诬陷于谦谋立襄王之子，致使其含冤遇害。明宪宗时，于谦被复官赐祭，弘治二年（1489年），追谥“肃愍”。明神宗时，改谥“忠肃”。有《于忠肃集》传世。《明史》称赞其“忠心义烈，与日月争光”。他与岳飞、张煌言并称“西湖三杰”。')
        st.subheader(':orange[有关资料]:point_down:')
        st.write('【清】夏燮,中华书局《明通鉴》， 【清】计六奇,中华书局《明季北略》， 【清】计六奇,中华书局《明季南略》， 【清】张廷玉,中华书局《明史》， 【清】谷应泰,中华书局《明史纪事本末》， 【清】龙文彬,中华书局《明会要》')     
        st.subheader(':orange[有关视频]:point_down:')
        st.link_button('【为王朝续命200年，一身傲骨，只有清风。千古于少保-于谦】', 'https://www.bilibili.com/video/BV1n14y1n726?vd_source=86548fb714a4e99157ad07fa910cc744')
    
    with t2:
        st.subheader(':orange[人物介绍]:point_down:')
        st.write('毛泽东，1893年12月26日生于一个农民家庭。辛亥革命爆发后在起义的新军中当了半年兵。1914～1918年，在湖南第一师范学校求学。毕业前夕和蔡和森等组织革命团体新民学会。五四运动前后接触和接受马克思主义，1920年，在湖南创建共产主义组织。 1921年7月，出席中国共产党建党的第一次全国代表大会，后任中共湘区委员会书记，领导长沙、安源等地工人运动。1923年，出席中共第三次全国代表大会，被选为中央执行委员，参加中央领导工作。')
        st.write('1924年国共合作后，在国民党第一、第二次全国代表大会上都当选为候补中央执行委员，曾在广州任国民党中央宣传部代理部长，主编《政治周报》，主办第六届农民运动讲习所。1926年11月，任中共中央农民运动委员会书记。1925年冬至1927年春，先后发表《中国社会各阶级的分析》、《湖南农民运动考察报告》等著作，指出农民问题在中国革命中的重要地位和无产阶级领导农民斗争的极端重要性，批评了陈独秀的右倾思想。')
        st.write('国共合作全面破裂后，在1927年8月中共中央紧急会议上，他提出“政权是由枪杆子中取得的”，即以革命武装夺取政权的思想，并被选为中央政治局候补委员。会后，到湖南、江西边界领导秋收起义。接着率起义部队上井冈山，发动土地革命，创立第一个农村革命根据地。1928年，同朱德领导的起义部队会师，成立工农革命军（不久改称红军）第四军，他任党代表、前敌委员会书记，朱德任军长。以他为主要代表的中国共产党人，从中国的实际出发，在国民党政权统治比较薄弱的农村发展武装斗争，开创了以农村包围城市、最后夺取城市和全国政权的道路。他在《中国的红色政权为什么能够存在？》、《星星之火，可以燎原》等著作中对这个问题从理论上作了阐述。') 
        st.write('1930年5月，写《反对本本主义》，提出“没有调查，没有发言权”的著名论断。同年8月，红军第一方面军成立，任总政治委员。1931年，中华苏维埃共和国临时政府在江西瑞金成立，被选为主席。1933年，被补选为中共中央政治局委员。从1930年底起，同朱德领导红一方面军战胜了国民党军队的多次“围剿”。以王明为代表的“左”倾路线领导集团进入中央革命根据地以后，将毛泽东排斥于党和红军的领导之外，他们执行不同的战略和政策，导致第五次反“围剿”战争失败。1934年10月，参加红一方面军长征。长征途中，1935年1月中共中央政治局在贵州召开扩大会议（即遵义会议），确立了以毛泽东为代表的新的中央领导。')
        st.write('10月，中共中央和红一方面军到达陕北，结束长征。12月，作《论反对日本帝国主义的策略》的报告，阐明了抗日民族统一战线政策。1936年10月，红四方面军和红二方面军经过长征到达甘肃境内，先后同红一方面军会师。同年12月，同周恩来等促使西安事变和平解决，这成为由内战到第二次国共合作、共同抗日的时局转换的枢纽。1936年12月，写《中国革命战争的战略问题》。1937年夏，写《实践论》和《矛盾论》。')
        st.write('抗日战争开始后，以他为首的中共中央坚持统一战线中的独立自主原则，努力发动群众，开展敌后游击战争，建立了许多大块的抗日根据地。这些抗日根据地大部分是在华北山区，但也有的是在河北平原和苏北平原。1938年10月，在中共扩大的六届六中全会上提出“马克思主义中国化”的指导原则。在抗日战争时 期，他发表《论持久战》、《〈共产党人〉发刊词》、《新民主主义论》等重要著作。')
        st.write('1942年，领导全党开展整风运动，纠正主观主义和宗派主义，使全党进一步掌握了马克思列宁主义的普遍真理和中国革命的具体实践相结合的基本方向，为夺取抗日战争和全国革命的胜利奠定了思想基础。1943年，领导根据地军民开 展生产运动，渡过了严重的经济困难。同年3月，被选为中共中央政治局主席。1945年，主持召开中共第七次全国代表大会，作《论联合政府》的报告。大会制定了“放手发动群众，壮大人民力量，在我党的领导下，打败日本侵略者，解放全国人民，建立一个新民主主义的中国”的战略。毛泽东思想在这次大会上被确定为中共的指导思想。他从七届一中全会起至1976年逝世为止，一直担任中共中央主席。抗日战争胜利后，针对蒋介石企图消灭共产党及其武装力量的现实，他提出“针锋相对”的斗争方针。1945年8月赴重庆同蒋介石谈判，表明中国共产党争取国内和平的愿望。')
        col9, col10 = st.columns([1, 1])
        with col9:
            st.image('毛泽东.jpg')
        with col10:
            st.write('1946年夏蒋介石发动全面内战后，毛泽东同朱德、周恩来领导中国人民解放军进行积极防御，集中优势兵力，各个歼灭敌人。1947年3月至1948年3月，同周恩来、任弼时转战陕北，指挥西北战场和全国的解放战争。1947年夏，中国人民解放军从战略防御转入战略进攻，在以他为首的党中央领导下，经过辽沈、淮海、平津三大战役和1949年4月渡长江以后的作战，推翻了国民党政府。')
            st.write('1949年3月，主持召开中共七届二中全会，并作重要报告，决定把党的工作重心从农村转到城市，规定了党在全国胜利以后的各项基本政策，号召全党务必保持谦虚、谨慎、不骄、不躁的作风，务必继续保持艰苦奋斗的作风。7月1日，发表《论人民民主专政》，规定了人民共和国的政权的性质及其对内对外的基本政策。1949年10月1日，中华人民共和国建立，他当选为中央人民政府主席。')
            st.write('1950年6月，主持召开中共七届三中全会，提出为争取国家财政经济状况的基本好转而斗争的总任务。同年10月，迫于美国军队攻入朝鲜民主主义人民共和国、威胁中国东北部的形势，以他为首的中共中央决定进行抗美援朝战争。')
        st.write('1950～1952年，在他的领导下，进行了土地改革、镇压反革命和其他民主改革，开展了反对贪污、反对浪费、反对官僚主义的“三反”运动和反对行贿、反对偷税漏税、反对盗骗国家财产、反对偷工减料、反对盗窃经济情报的“五反”运动。1953年，按照他的建议，中共中央宣布了党在过渡时期的总路线，开始有系统地进行社会主义工业化和对生产资料私有制的社会主义改造。')
        st.write('1954年，第一届全国人民代表大会第一次会议通过了由他主持起草的《中华人民共和国宪法》，他在这次会议上当选为中华人民共和国第一任主席，任职到1959年。1956年4月，作《论十大关系》的讲话，这个讲话对适合中国国情的建设社会主义的道路进行了一些初步的探索。接着，在中共中央政治局扩大会议上提出“百花齐放，百家争鸣”的方针。1956年，生产资料私有制的社会主义改造基本完成。')
        st.write('同年9月，中共召开第八次全国代表大会，指出全国人民的主要任务已经转变为集中力量发展社会生产力。但是这个方针后来没有得到认真的执行，因而导致了以后的一系列指导工作上的错误和挫折。1957年2月，他作《关于正确处理人民内部矛盾的问题》的讲话，提出正确区分和处理社会主义社会中敌我之间和人民内部两类不同性质矛盾的学说。')
        st.write('1957年7月，提出要“造成一个又有集中又有民主，又有纪律又有自由，又有统一意志、又有个人心情舒畅、生动活泼，那样一种政治局面”的要求。1958年，发动“大跃进”和农村人民公社化运动。1959年，主持召开庐山会议。他本想纠正已经觉察到的错误，但在会议后期错误地发动了对彭德怀的批判，会后在全党 错误地开展了“反右倾”斗争。')
        st.write('从1960年冬到1965年，在以他为首的中共中央领导下，对国民经济实行“调整、巩固、充实、提高”的方针，初步纠正“大跃进”和人民公社化运动中的错误，使国民经济得到比较迅速的恢复和发展。在这期间，他提出了一系列措施，初步纠正了农村工作中和其他方面的“左”的错误。但在1962年9月召开的中共八届十中全会上，他把社会主义社会中一定范围内存在的阶级斗争扩大化和绝对化，发展了他在1957年反右派斗争以后提出的无产阶级同资产阶级的矛盾仍然是中国社会的主要矛盾的观点。')
        st.write('1963～1965年，发动农村和城市社会主义教育运动，提出运动的重点是整所谓“党内走资本主义道路的当权派”。从50年代开始，他领导中共同苏共领导人奉行的大国主义和干涉、控制中国的企图进行了坚决的斗争。1966年，由于对国内阶级斗争形势作出了极端的估计，他发动了“文化大革命”运动，这个运动因受林彪、江青两个反革命集团操纵而变得特别狂暴，大大超出了他的预计和他的控制，以至延续十年之久，使中国许多方面受到严重的破坏和损失。')
        st.write('在“文化大革命”中，毛泽东也制止和纠正过一些具体错误。他领导了粉碎林彪反革命集团的斗争，不让江青、张春桥等夺取最高领导权的野心得逞。在对外政策方面，他提出“三个世界”划分的战略和中国永远不称霸的重要思想，并且开始打开对外工作的新局面，为中国进行现代化建设创造了有利的国际条件。1976年9月9日，在北京逝世，享年83岁。')
        st.subheader(':orange[有关资料]:point_down:')
        st.write('《中国社会各阶级的分析》， 《中国红色政权为什么能够存在》， 《古田会议决议》， 《星星之火可以燎原》， 《中国革命战争的战略问题》， 《论持久战》， 《新民主主义论》， 《论人民民主专政》， 《一九五七年夏季的形势》')
        st.subheader(':orange[有关视频]:point_down:')
        st.link_button('【#纪念毛泽东同志逝世46周年##军史回眸#95年前的今天，秋收起义爆发。】', 'https://www.bilibili.com/video/BV1X14y1s71f?vd_source=86548fb714a4e99157ad07fa910cc744')

    with t3:
        st.subheader(':orange[人物介绍]:point_down:')
        st.write('全斗焕（韩语：전두환，1931年3月6日—2021年11月23日），男、朝鲜族。出生于庆尚南道陕川郡，毕业于韩国陆军官校 ，韩国第11届和12届总统 。1955年，毕业后以少尉身份入伍。1961年，因组织支持5·16军事政变的陆军士官学校学生游行而得到朴正熙的青睐。之后晋升为少将。1979年12月12日，发动双十二政变，攫取军权。1980年，通过5·17紧急戒严事件控制政权，并镇压了光州事件；同年8月，以陆军大将退役，并当选韩国第11届总统 。此后修改宪法，并依新宪法于1981年2月当选为韩国第12届总统，开创第五共和国。1988年2月，卸任，实现了大韩民国首次和平的政权交接 。1996年，因涉嫌“军事叛乱罪”被起诉，一审被判处死刑，随后又改为无期徒刑，并追缴罚款2205亿韩元。1997年12月，被时任韩国总统金泳三特赦，并于1998年初获释 。2013年7月，被抄家偿还赃款。2017年，出版个人回忆录，但因涉嫌在书中损害死者名誉，于2020年11月被判刑8个月，缓刑2年执行 。2021年8月9日，再次出庭参加诽谤案庭审 ；同年11月23日，在家中去世，终年90岁 。')
        col11, col12 = st.columns([1, 1])
        with col11:
            st.image('全斗焕.jpg')
        with col12:
            st.write('全斗焕卸任后，曾三次访问中国。2001年12月，应中国人民外交学会邀请，全斗焕访华，田纪云、戴秉国分别会见，其后又南下上海。2007年10月，全斗焕再应中国人民外交学会邀请访华，全国政协主席贾庆林于31日在人民大会堂会见全斗焕夫妇一行，对全斗焕在任总统期间为中韩关系改善做出的努力表示赞赏。期间全斗焕夫妇曾参观雍和宫。11月前往江苏扬州，会见江苏省委书记、省长梁保华、扬州市委书记季建业等，并参观崔致远纪念馆。2011年9月，全斗焕第三次应中国人民外交学会邀请访华，访问了黑龙江、山东等地。')
        st.subheader(':orange[有关资料]:point_down:')
        st.write('《韩国近代史》， 《朝鲜韩国近现代史事典:一八六〇～二〇一二(第3版)》， 《当代韩国史——1945-2000》， 《近代韩国外交文书》， 《韩国史大观》， 《韩国史新论》')
        st.subheader(':orange[有关视频]:point_down:')
        st.link_button('【不能再犹豫了！——赌神总统 全斗焕】', 'https://www.bilibili.com/video/BV1cK421v7B7?vd_source=86548fb714a4e99157ad07fa910cc744')

    with t4:
        st.subheader(':orange[人物介绍]:point_down:')
        st.write('温斯顿·伦纳德·斯宾塞·丘吉尔爵士（Sir Winston Leonard Spencer Churchill，1874年11月30日—1965年1月24日），政治家、演说家及作家以及记者，1953年诺贝尔文学奖得主，曾于1940－1945年及1951－1955年期间两度任英国首相，被认为是20世纪最重要的政治领袖之一，带领英国获得第二次世界大战的胜利。被公认为世界上掌握单词词汇量最多的人(5万多)。丘吉尔1874年11月30日出生在英格兰牛津郡的一个贵族世家，1965年1月24日卒于伦敦。1894年毕业于桑德赫斯特皇家军事学院。')
        st.write('1939年以前的主要政治活动 1895年从军，曾参加英国在印度、苏丹和南非的殖民战争。1906年进入下院。主张自由贸易，反对保护主义的关税政策。后历任殖民部次官、商务大臣、内政大臣、海军大臣和军需大臣、陆军大臣兼空军大臣、殖民大臣等要职。在任海军大臣期间，大力加强海军实力，以回击德国对英国海上霸权的挑战。第一次世界大战爆发后，1915年，英军在黑海海峡的盖利博卢战役中失利，同年11月丘吉尔引咎辞职。1919年1月丘吉尔出任陆军大臣兼空军大臣，积极参与策划武装干涉苏俄。')
        st.write('1922年，因不满自由党的政策而脱离该党。1924年任S.鲍德温内阁的财政大臣。1925年在英国恢复金本位制，企图恢复伦敦作为世界金融中心的地位。1931年1月，因对保守党领袖的政策不满退出鲍德温的影子内阁。此后他被排斥在政府公职之外 ，专心从事写作。在此期间，他同保守党右翼一起，反对向印度独立的要求作任何让步。丘吉尔对来自德国的威胁不断发出警告，主张重整军备，反对A.N.张伯伦姑息德国侵略的绥靖政策，主张联合法国和苏联，依靠国际联盟来阻止德国的侵略。')
        st.write('第二次世界大战中的活动 1939年9月德国入侵波兰后，丘吉尔任张伯伦政府的海军大臣，积极组织援助挪威的战役。1940年5月10日继张伯伦任首相，并兼国防大臣，立即把全国经济纳入战时轨道。丘吉尔政府拒绝德国的诱和，坚持对德作战，同时争取美、苏作为同盟者参战。为了保卫不列颠群岛，亲自视察海防、空防设施。')
        col11, col12 = st.columns([1, 1])
        with col11:
            st.image('丘吉尔.jpeg')
        with col12:
            st.write('他支持沦陷国家开展抵抗运动，支持沦陷国家的流亡政府。苏德战争爆发当天，丘吉尔庄严声明：“俄国人的危难就是我们的危难，也就是美国的危难。”1941年7月12日签订《英 、苏在对德战争中联合行动的协定》。8月9日，丘吉尔和F.D.罗斯福签署《大西洋宪章》。太平洋战争爆发后，丘吉尔与美国缔结一系列条约，其中包括联合使用两国的军事和经济资源、成立联合参谋部等内容。1942年以时机尚未成熟为借口，推迟开辟第二战场。丘吉尔先后参加德黑兰会议、雅尔塔会议等国际会议。在处置战败的德国、波兰的疆界变动和政府组成等问题上，极力维护英帝国的利益。战后的政治生涯 1945 年7月大选中，保守党在选举中失败，丘吉尔辞去首相职务。1946年3月5日，在美国密苏里州富尔顿发表题为《和平砥柱》的演说，这次演说揭开战后冷战时期的序幕。')
        st.write('1948年10月9日 ，丘吉尔在英国保守党年会上正式提出一个把英美联盟、联合的欧洲、英联邦和英帝国连接在一起的三环外交的总方针。但由于战后英国的衰落未能实现。1951～1955年，丘吉尔再度出任首相。在执政期间签订1954年《巴黎军事协定》，并缔结《东南亚防务条约》，继续对苏采取强硬态度。1953年，丘吉尔被封为爵士，获嘉德勋章，同年获诺贝尔文学奖。1955年4月5日正式退休，但直到1964年7月一直任下院议员。')  
        st.subheader(':orange[有关资料]:point_down:')
        st.write('《第二次世界大战回忆录》， 《世界1937：丘吉尔眼中的时代人物》， 《丘吉尔传——与命运同行》， 《不需要的战争》， 《英国中坚——丘吉尔》， 《丘吉尔——千面政客》， 《丘吉尔全传》')
        st.subheader(':orange[有关视频]:point_down:')
        st.link_button('【日不落帝国的落日余晖：温斯顿·丘吉尔【历史调研室10】】', 'https://www.bilibili.com/video/BV1P5411a7M4?vd_source=86548fb714a4e99157ad07fa910cc744')

    with t5:
        st.subheader(':orange[人物介绍]:point_down:')
        st.write('海因兹·威廉·古德里安(Heinz Wilhelm Guderian，1888年6月17日-1955年5月14日)，是第二次世界大战期间德国一名陆军军官，1940年7月被晋升为上将。军事家，军事理论家，统帅，德国装甲兵创建者，并被认为是闪电战的创始人之一，虽然不是纳粹政权时期的最高级将领却被认为是第二次世界大战最出色的指挥官之一;被各国战史学家公认赞誉是"世界坦克(作战)之父"。 古德里安在奥地利和苏台德地区吞并行动中担任第十六装甲军军长。')
        st.write('第二次世界大战期间古德里安参与的重要战役有:波兰侵略战担任第十九装甲军军长，隶属伦德施泰特南方集团军群;法国侵略战担任后期任装甲集团军群司令;苏德战争开始后于10月担任第二装甲军团司令;后先后担任装甲兵总监与德国投降前"德国保卫战"代理陆军参谋总长。1945年5月10日向美军投降，随后被关押3年，因为在战争期间并未虐待战俘和屠杀平民没有被列为战犯，于1948年释放。1955年5月14日古德里安因病去世。')
        col19, col20 = st.columns([1, 1])
        with col19:
            st.image('古德里安.jpg')
        with col20:
            st.write('古德里安曾获得战功十字勋章二级，带剑奥地利战争纪念勋章，带剑匈牙利战争纪念勋章，一级三军战斗荣誉勋章，战斗纪念勋章(1938年3月13日)占领奥地利后，布拉格城堡勋章(1938年10月1日)波兰侵略战后，荣誉骑士十字勋章，坦克突击勋章银质，铁十字勋章一级1914版，铁十字勋章一级1939版(加授带)，橡叶骑士铁十字勋章，骑士铁十字勋章(1939年10月27日)，骑士铁十字勋章加橡叶(1941年7月17日)')
        st.subheader(':orange[有关资料]:point_down:')
        st.write('《一个军人的回忆》, 《闪击战》, 《历史与记忆中的第三帝国》, 《第三帝国的到来》, 《当权的第三帝国》, 《战时的第三帝国》')
        st.subheader(':orange[有关视频]:point_down:')
        st.link_button('【【古德里安】闪击波兰狂飙法国，闪电战之父比你想象中更夸张！】', 'https://www.bilibili.com/video/BV1hU411U7Wi?vd_source=86548fb714a4e99157ad07fa910cc744')

    with t6:
        html = r'码.txt' 
        with open(html, 'r', encoding='utf-8') as file:  
            html_content = file.read()  
        
        def image_to_base64(image_path):  
            with open(image_path, 'rb') as img_file:  
                return base64.b64encode(img_file.read()).decode()  

        image1_base64 = image_to_base64('1.jpeg')  
        image2_base64 = image_to_base64('2.jpg')  
        image3_base64 = image_to_base64('3.jpg')  
        image4_base64 = image_to_base64('4.jpeg')  
        image5_base64 = image_to_base64('5.png')  
        html_code = f'''  
        <!DOCTYPE html>  
        <html>  
        <head>  
            <title>已录入人物</title>  
            <style>  
                h1 {{  
                    color:purple;  
                    font-size:30px;  
                    text-align:center;  
                }}  
                .gallery {{  
                    display: flex;  
                    justify-content: center;  
                    gap: 20px;  
                }}  
                .gallery img {{  
                    width: 140px;  
                    transition: transform 1s;  
                }}  
                .gallery img:hover {{  
                    transform: scale(1.4) rotate(10deg);  
                }}  
            </style>  
        </head>  
        <body>  
            <h1>已录入人物</h1>  
            <div class="gallery">  
                <img src="data:image/png;base64,{image1_base64}" />  
                <img src="data:image/png;base64,{image2_base64}" />  
            </div>  
            <div class="gallery">  
                <img src="data:image/png;base64,{image3_base64}" />  
                <img src="data:image/png;base64,{image4_base64}" />  
                <img src="data:image/png;base64,{image5_base64}" />
        </div>  
        </body>  
        </html>  
        '''  
        components.html(html_code, height=600)  
    
        st.write('-------------------------------------------')
        with open('history.txt', 'r', encoding="utf-8") as f:
            history_list = f.read().split('\n')
        for i in range(len(history_list)):
            history_list[i] = history_list[i].split('#')
        history_dict = {}
        for i in history_list:
            history_dict[int(i[0])] = [i[1], int(i[2])]

        st.write('你喜欢什么类型的历史呢？')
        cb1 = st.checkbox('中国古代史')
        cb2 = st.checkbox('中国近代史')
        cb3 = st.checkbox('中国现代史')
        cb4 = st.checkbox('世界史')
        l = [cb1, cb2, cb3, cb4]
        if st.button('确认回答'):
            if True in l:
                for i in range(len(l)):
                    if l[i] == True:
                        history_dict[i+1][1] += 1
                
                with open('history.txt', 'w', encoding="utf-8") as p:
                    message = ''
                    for k, v in history_dict.items():
                        message += str(k) + '#' + v[0] + '#' + str(v[1]) + '\n'
                    message = message[:-1]
                    p.write(message)
                st.write(':blue[看看别人的想法吧]')
    
                num = 0
                with open('history.txt', 'r', encoding="utf-8") as f:
                    history_list = f.read().split('\n')
                for i in range(len(history_list)):
                    history_list[i] = history_list[i].split('#')
                    num += int(history_list[i][2])
                st.write('中国古代史:'+str(int(int(history_list[0][2])/num*100))+'%', '中国近代史:'+str(int(int(history_list[1][2])/num*100))+'%', '中国现代史:'+str(int(int(history_list[2][2])/num*100))+'%', '世界史:'+str(int(int(history_list[3][2])/num*100))+'%')
                chart_data = pd.DataFrame(
                    [[int(history_list[0][2]), int(history_list[1][2]), int(history_list[2][2]), int(history_list[3][2])]],
                    columns=['中国古代史', '中国近代史', '中国现代史', '世界史'])
                st.bar_chart(chart_data)    
            else:
                st.write(':red[#你没有勾选内容]')
    
    st.write('-------------------------------------------')
    st.write('详细内容可前往其它网站了解哦:sparkling_heart:')
    go = st.selectbox('为你推荐几个网站', ['百度', 'bilibili'])
    if go == '百度':
        st.link_button('前往百度', 'https://www.baidu.com/')
    elif go == 'bilibili':
        st.link_button('前往B站', 'https://www.bilibili.com/')

def img_change(img, cr, cg, cb):
    width, height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            r = img_array[x, y][cr]
            g = img_array[x, y][cg]
            b = img_array[x, y][cb]
            img_array[x, y] = (g, b, r)
    return img

def bright(img):
    e = ImageEnhance.Brightness(img)
    img = e.enhance(1.3)
    return img

def contrast(img):
    e = ImageEnhance.Contrast(img)
    img = e.enhance(1.3)
    return img

def rotate_(img):
    img = img.rotate(180)
    return img

def transpose_(img):
    img = img.transpose(Image.FLIP_LEFT_RIGHT)
    return img
    
def page_3():
    st.title(':red[我的图片处理]:clap:')
    st.write(':blue[可对图片进行改色，提高亮度，提高对比度，旋转和镜像]')
    uploaded_file = st.file_uploader('上传图片', type=['jpg', 'png', 'gif', 'jpeg'])
    if uploaded_file:
        img = Image.open(uploaded_file)
        col15, col16 = st.columns([1, 1])
        with col15:
            st.image(img)
        with col16:
            g1 = st.toggle('改色1')
            g2 = st.toggle('改色2')
            g3 = st.toggle('提高亮度')
            g4 = st.toggle('提高对比度')
            g5 = st.toggle('旋转')
            g6 = st.toggle('镜像')
        if st.button('开始处理图片'):
            roading = st.progress(0, '开始加载')
            for i in range(1, 101, 1):
                time.sleep(0.02)
                roading.progress(i, '正在加载'+str(i)+'%')
            roading.progress(100, '加载完毕！')

            if g1:
                img = img_change(img, 1, 2, 0)
            if g2:
                img = img_change(img, 0, 2, 1)
            if g3:
                img = bright(img)
            if g4:
                img = contrast(img)
            if g5:
                img = rotate_(img)
            if g6:
                img = transpose_(img)
            st.image(img)
            st.write('#[右键另存为]保存图片')

    st.write('-------------------------') 
        
def page_4():
    st.title(':red[我的智慧词典]:clap:')
    st.write(':blue[英语不懂问我哦]')
    with open('words_space.txt', 'r', encoding="utf-8") as f:
        words_list = f.read().split('\n')
    for i in range(len(words_list)):
        words_list[i] = words_list[i].split('#')
    EC_words_dict = {}
    CE_words_dict = {}
    for i in words_list:
        EC_words_dict[i[1]] = [int(i[0]), i[2]]
    for i in words_list:
        CE_words_dict[i[2]] = [int(i[0]), i[1]]

    with open('EC_check_out_times.txt', 'r', encoding="utf-8") as a:
        times_list = a.read().split('\n')
    for i in range(len(times_list)):
        times_list[i] = times_list[i].split('#')
    EC_times_dict = {}
    for i in times_list:
        EC_times_dict[int(i[0])] = int(i[1])

    with open('CE_check_out_times.txt', 'r', encoding="utf-8") as a:
        times_list = a.read().split('\n')
    for i in range(len(times_list)):
        times_list[i] = times_list[i].split('#')
    CE_times_dict = {}
    for i in times_list:
        CE_times_dict[int(i[0])] = int(i[1])
    
    mo = st.selectbox('选择翻译模式:', ['英译中', '中译英'])
    if mo == '英译中':
        word = st.text_input('请输入可查询的英语单词')
        if word in EC_words_dict:
            st.write(EC_words_dict[word][1])
            n = EC_words_dict[word][0]
            if n in EC_times_dict:
                EC_times_dict[n] += 1
            else:
                EC_times_dict[n] = 1
    
            with open('EC_check_out_times.txt', 'w', encoding="utf-8") as b:
                message = ''
                for k, v in EC_times_dict.items():
                    message += str(k) + '#' + str(v) + '\n'
                message = message[:-1]
                b.write(message)
            st.write('查询次数', EC_times_dict[n])
    
            if word == 'balloon':
                st.balloons()
            elif word == 'snowy':
                st.snow()
            elif word == 'python':
                st.code('''
                        print('Hello, world.')
                        ''')

    elif mo == '中译英':
        word = st.text_input('请输入可查询单词的中文意思及词性')
        if word in CE_words_dict:
            st.write(CE_words_dict[word][1])
            n = CE_words_dict[word][0]
            if n in CE_times_dict:
                CE_times_dict[n] += 1
            else:
                CE_times_dict[n] = 1
    
            with open('CE_check_out_times.txt', 'w', encoding="utf-8") as s:
                message = ''
                for k, v in CE_times_dict.items():
                    message += str(k) + '#' + str(v) + '\n'
                message = message[:-1]
                s.write(message)
            st.write('查询次数', CE_times_dict[n])

            if word == 'n.气球':
                st.balloons()
            elif word == 'adj.有雪的，下雪的':
                st.snow()
            elif word == 'n.编程':
                st.code('''
                        print('Hello, world.')
                        ''')
    st.write('-------------------------') 

def page_5():
    st.title(':red[留言区]:clap:')
    st.subheader(':blue[说说你的建议吧！]:sparkling_heart:')

    with open('leave_messages.txt', 'r', encoding="utf-8") as f:
        messages_list = f.read().split('\n')
    for i in range(len(messages_list)):
        messages_list[i] = messages_list[i].split('#')

    col5, col6 = st.columns([1, 1])
    with col5:
        name = st.text_input('你的名字:')
    with col6:
        job = st.selectbox('你是:', ['学生', '老师', '工人', '农民', '白领', '医生'])
    new_message = st.text_input('留言内容')
    if st.button('点我留言'):
        if len(new_message) != 0:
            messages_list.append([str(int(messages_list[-1][0])+1), name, job, new_message])
            with open('leave_messages.txt', 'w', encoding="utf-8") as p:
                message = ''
                for i in messages_list:
                    message += i[0] + '#' + i[1] + '#' + i[2] + '#' + i[3] + '\n'
                message = message[:-1]
                p.write(message)
            st.write('谢谢' + name + '的留言，我们会尽快处理。')
        else:
            st.write(':red[#你没有输入内容]')

    st.write('')
    st.subheader(':point_down:留言记录:point_down:')
    for i in messages_list:
        if i[2] == '制作者':
            with st.chat_message('👦'):
                st.write(i[1]+'('+i[2]+')', ':', i[3])
        elif i[2] == '学生':
            with st.chat_message('👨‍🎓'):
                st.write(i[1]+'('+i[2]+')', ':', i[3])
        elif i[2] == '老师':
            with st.chat_message('👨‍🏫'):
                st.write(i[1]+'('+i[2]+')', ':', i[3])
        elif i[2] == '工人':
            with st.chat_message('👨‍🏭'):
                st.write(i[1]+'('+i[2]+')', ':', i[3])
        elif i[2] == '农民':
            with st.chat_message('👨‍🌾'):
                st.write(i[1]+'('+i[2]+')', ':', i[3])
        elif i[2] == '白领':
            with st.chat_message('👨‍💼'):
                st.write(i[1]+'('+i[2]+')', ':', i[3])
        elif i[2] == '医生':
            with st.chat_message('👨‍⚕️'):
                st.write(i[1]+'('+i[2]+')', ':', i[3])
    

if page == '兴趣推荐':
    page_1()
elif page == '历史人物志':
    page_2()
elif page == '图片处理':
    page_3()
elif page == '智慧词典':
    page_4()
elif page == '留言区':
    page_5()
