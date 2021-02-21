pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today ?",]
    ],
    [
        r"say hello to (.*)|say hello (.*)",
        ["Hello %1, How are you today ?",]
    ],

    [
        r"what is your name ?",
        ["My name is Nougat and I'm a chatbot ?",]
    ],
    [
        r"sorry",
        ["Ihits alright","Its OK, never mind",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ],
        
    [
        r"quit|Quit|Bye|bye",
        ["BBye take care. See you soon :) ","It was nice talking to you. See you soon :)"]

    ],
    [
        r"how are you|how are you?|how are you ?",
        ["Im good thank you ! ",]
    ],

    [
        r"thank you|thanks?",
        ["you are welcome ! ",]
    ],

    [
        r"/help",
        [''' ``` To help us to improve our BOT, Please proceed as below :
        !user [Name] : to tell your name 
        !sat [score] : to give your score
        !imp [improvement_proposal] : to propose an improvement
        !date : to show the actual date&time ```
        ''',
        ]
    ],
]
