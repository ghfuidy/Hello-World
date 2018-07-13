import random

captials = {
'内蒙古自治区':'呼和浩特',
'山西':'太原',
'河北':'石家庄',
'辽宁':'沈阳',
'吉林':'长春',
'黑龙江':'哈尔滨',
'江苏':'南京',
'安徽':'合肥',
'山东':'济南',
'浙江':'杭州',
'江西':'南昌',
'福建':'福州',
'湖南':'长沙',
'湖北':'武汉',
'河南':'郑州',
'广东':'广州',
'广西壮族自治区':'南宁',
'海南':'海口',
'贵州':'贵阳',
'云南':'昆明',
'四川':'成都',
'陕西':'西安',
'甘肃':'兰州',
'宁夏回族自治区':'银川',
'青海':'西宁',
'新疆维吾尔自治区':'乌鲁木齐',
'西藏自治区':'拉萨',
'首都':'北京',
'台湾省':'台北',
}

stuNum = int(input("\n您要出几份考卷？ "))

for quizNum in range(stuNum):
    quizFiled = open('capitalsquiz{}.txt'.format(quizNum + 1),'w',encoding = 'utf-8')
    answerKeyFiled = open('capitalsquiz_answer{}.txt'.format(quizNum + 1),'w',encoding = 'utf-8')
    quizFiled.write('姓名：\n\n学号：\n\n班级\n\n')
    quizFiled.write( ' '*20 +'省 配 对 测 试 卷 {}\n\n'.format(quizNum + 1)) 

    provinces = list(captials.keys())
    random.shuffle(provinces)

    for questionNum in range(len(provinces)):
        correctAnswer = captials[provinces[questionNum]]

        wrongAnswers = list(captials.values())
        wrongAnswers.remove(correctAnswer)
        wrongAnswers = random.sample(wrongAnswers,3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)
        
        quizFiled.write('{}、 {}的省会是？ \n'.format(questionNum + 1, provinces[questionNum]))

        for i in range(4):
            quizFiled.write('{}. {}\n'.format('ABCD'[i],answerOptions[i]))


        answerKeyFiled.write('{}. {}\n'.format(questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))

quizFiled.close()
answerKeyFiled.close()