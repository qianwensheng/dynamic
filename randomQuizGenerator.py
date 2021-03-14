# Creates quizzes with questions and answers in 
# random order ,along with the answer key
# my first upload file on github

import random

# 测试数据，keys是省，values是省会

capitals = {'冀': '石家庄', '辽': '沈阳','黑':'哈尔滨','浙':'杭州','闽':'福州',
'鲁':'济南','粤':'广州','鄂':'武汉','川':'成都','云':'昆明','甘':'兰州','台':'台北',
'宁':'银川'}

# 产生10个测试文件

for quizNum in range(10) :
    #创建测试文件
    quizFile = open('capitalsquiz%s.txt' % (quizNum + 1), 'w')
    ansewrKeyFile = open('capitalsquiz_answers%s.txt' % (quizNum + 1), 'w')

    #写下测验的标题
    quizFile.write('姓名:\n\n学号:\n\n班级:\n\n')
    quizFile.write((' ' * 20) + '各省省会测试(Form %s)' %(quizNum + 1))
    quizFile.write('\n\n')

    #各省顺序洗牌
    states = list(capitals.keys())
    random.shuffle(states)

    #遍历所有13个省，对每个省提出一个问题
    for questionNum in range(10) :
        #得到正确和错误的答案
        correctAnswer = capitals[states[questionNum]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers,3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)

        #把问题和答案选项写入到测试文件
        quizFile.write('%s. %s的省会是什么？\n' % (questionNum + 1,states[questionNum]))
        for i in range(4) :
            quizFile.write('%s. %s\n' % ('ABCD'[i],answerOptions[i]))
        quizFile.write('\n')

        #把答案写入文件
        ansewrKeyFile.write('%s. %s\n' % (questionNum + 1,'ABCD'[
            answerOptions.index(correctAnswer)]))
    
    quizFile.close()
    ansewrKeyFile.close()



