# 您可以在此編寫遊戲的腳本。

# image命令可用於定義一個圖像。
# eg. image eileen happy = "eileen_happy.png"

# define命令可定義遊戲中出現的角色名稱與對應文本顏色。
define player = Character('[player]', color="#c8ffc8")
define girl = Character('性感女郎', color="#c8ffc8")

image girl = "images/img_h01.png"
image bg = "images/img_bg3.jpg"

$ player_fist = " "
$ girl_fist = " "
$ g_fist=''
$ result = ''


# 遊戲從這裡開始。
label start:
    scene bg

    $ player = renpy.input('你叫什麼名字？')
    $ player = player.strip()
    $ player_score = 0
    $ girl_score = 0
    
    play music "music.mp3"
    player '酒保，給我一杯馬丁尼，用搖的，不要攪拌！'
    show girl at top
    with dissolve
    girl '你就是世界猜拳冠軍嗎？'
    player '是的，這位美女，你找我有什麼事嗎？'
    girl  '我想知道你有多會猜拳，來比一把吧！'
    player  '哈哈哈，有趣！如果你輸了願意陪我一晚的話，我就奉陪！'
    girl '如果你輸的話，那你就要退出江湖，永遠不得參加世界猜拳大賽！'
    player '好，就這麼說定了'
    jump s2

label s2:

    player "好....我來想想要出什麼？"
    jump s3 

label s3:
menu:
    "剪刀":
        $ player_fist = "剪刀"
        jump s4
    "石頭":
        $ player_fist = "石頭"
        jump s4
    "布":
        $ player_fist = "布"
        jump s4

label s4:
    player "剪刀、石頭、布..."
    player "[player_fist]！"

    $ girl_fist = renpy.random.choice(["剪刀","石頭", "布"])
    girl "嘿，[girl_fist]"

    if player_fist == "剪刀" and girl_fist == '石頭':
      $ girl_score=girl_score+1
      jump s_girlwin
    elif player_fist == "石頭" and girl_fist == '布':
      $ girl_score=girl_score+1
      jump s_girlwin
    elif player_fist == "布" and girl_fist == '剪刀':
      $ girl_score=girl_score+1
      jump s_girlwin
    elif player_fist == "剪刀" and girl_fist == '布':
      $ player_score=player_score+1
      jump s_playerwin
    elif player_fist == "布" and girl_fist == '石頭':
      $ player_score=player_score+1
      jump s_playerwin      
    elif player_fist == "石頭" and girl_fist == '剪刀':
      $ player_score=player_score+1
      jump s_playerwin
    else:
      jump s_nowin
    
label s_girlwin:
    girl '太好了'
    player '怎麼會！'
    if player_score >= 3:
      jump s6
    elif girl_score >= 3:
      jump s7
    else:
      jump s2

label s_playerwin:
    player '贏了！'
    girl '哼！'
    if player_score >= 3:
      jump s6
    elif girl_score >= 3:
      jump s7
    else:
      jump s2

label s_nowin:
    player '平手！'
    jump s2

label s6:
    player '哈哈哈，是我贏了，美女，乖乖跟我走吧'
    girl '可惡，這次是我輸了，給我記著'
    hide girl with dissolve
    player '怎麼跑走了，願賭服輸啊！'
    jump s8

label s7:
    player '是我輸了，你....我是不是在哪看過你'
    girl '10年前，你曾經用卑鄙的手段贏了世界猜拳大賽'
    player '啊，難道你是...'
    girl '沒錯，我就是你當時打敗的對手，為了靠近你，我不惜去泰國變性！'
    player '為了報仇，你付出這麼多...我認輸，我會依照約定，退出比賽'
    jump s8

label s8:
    '遊戲結束 可喜可賀'

    return
