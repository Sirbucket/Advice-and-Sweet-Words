import random;

response_list = [
    "I have come to accept the feeling of not knowing where I am going. And I have trained myself to love it. Because it is only when we are suspended in mid-air with no landing in sight, that we force our wings to unravel and alas begin our flight. And as we fly, we still may not know where we are going to. But the miracle is in the unfolding of the wings. You may not know where you're going, but you know that so long as you spread your wings, the winds will carry you.",
    "Hope is important because it can make the present moment less difficult to bear. If we believe that tomorrow will be better, we can bear a hardship today.",
    "Next to trying and winning, the best thing is trying and failing.",
    "Soul mates' are fiction and an illusion; and while every young man and young woman will seek with all diligence and prayerfulness to find a mate with whom life can be most compatible and beautiful, yet it is certain that almost any good man and any good woman can have happiness and a successful marriage if both are willing to pay the price.",
    "If you always attach positive emotions to the things you want, and never attach negative emotions to the things you don't, then that which you desire most will invariably come your way.",
    "Love so joyfully and freely given can never be taken away. It is never truly gone.",
    "The devil's happy when the critics run you off.",
    "Everybody in this life has their challenges and difficulties. That is part of our mortal test. The reason for some of these trials cannot be readily understood except on the basis of faith and hope because there is often a larger purpose which we do not always understand. Peace comes through hope.",
    "It is only in our darkest hours that we may discover the true strength of the brilliant light within ourselves that can never, ever, be dimmed.",
    "Some of our struggles involve making decisions, while others are a result of the decisions we have made. Some of our struggles result from choices others make that affect our lives. We cannot always control everything that happens to us in this life, but we can control how we respond. Many struggles come as problems and pressures that sometimes cause pain. Others come as temptations, trials, and tribulations.",
    "Your partner should love you just the way you are, only if you love yourself.",
    "Believe in yourself. Stay in your own lane. There’s only one you.",
    "Experience is not what happens to you; it is what you do with what happens to you.",
    "People often say that beauty is in the eye of the beholder, and I say that the most liberating thing about beauty is realizing you are the beholder.",
    "Each day comes bearing its gifts. Untie the ribbon.",
    "Living is the art of getting used to what we didn’t expect.",
    "A person without regrets is a nincompoop.",
    "Love doesn’t make the world go round. Love is what makes the ride worthwhile.",
    "Kindness is one thing you can’t give away. It always comes back.",
    "Great opportunities to help others seldom come, but small ones surround us every day.",
    "Try to be a rainbow in someone else’s cloud.",
    "Success is falling nine times and getting up ten.",
    "The greatest mistake you can make is to be continually fearing that you’ll make one.",
    "Real courage is when you know you’re licked before you begin, but you begin anyway and see it through no matter what.",
    "The most sincere compliment we can pay is attention.",
    "A problem is a chance for you to do your best.",
    "The most important trip you may take in life is meeting people halfway.",
    "You deserve to be loved.",
    "Even in the toughest of times, you can persevere, no matter how insurmountable the odds are.",
    "Time you enjoy wasting was not wasted.",
    "What’s wrong with being sentimental? Sentimental means you like stuff.",
    "Having a young child explain something exciting he has seen is the finest example of communication you will ever hear or see.",
    "Memories are everyone’s second chance at happiness.",
    "Worry never robs tomorrow of its sorrow; it only saps today of its strength.",
    "If your ship doesn’t come in, swim out to it!",
    "Whatever you do, don’t wake up at 65 years old and think about what you should have done with your life.",
    "Pay no attention to what the critics say. A statue has never been erected in honor of a critic.",
    "The world is extremely interesting to a joyful soul.",
    "Don’t say you can’t until you prove you can’t.",
    "No day in which you learn something is a complete loss.",
    "It’s a whole lot more satisfying to reach for the stars, even if you end up landing only on the moon.",
    "Quiet minds cannot be perplexed or frightened, but go on in fortune or misfortune at their own private pace, like a clock during a thunderstorm.",
    "Love your friends like your family, and your family like you love yourself.",
    "There is more to be recieved in giving, than getting.",
    "You are powerful!",
    "Stop being a dreamer and go be a doer.",
    "Onions have layers, people are onions.",
    "Everyones life is different and can tell a story, isn't that incredible?",
];

def start_runtime():
    print(f"Hello, this applet has been written specifically to give you advice and improve your mood and knowledge of yourself! \n \n   __----__      __----__\n  /--------\    /--------\ \n /----------\  /----------\ \n|------------\/-----------|\n \-----------------------/\n  \---------------------/\n    \-----------------/\n      \-------------/\n       \-----------/\n        \---------/\n          \-----/\n           \---/\n            \-/\n");
    
    print("If you desire for your mood to stop improving, type close, otherwise continue pressing enter for wonderful messages! \o/");

def print_response(response):
    print(f"\n {response} \n");

def run_program():
    random.shuffle(response_list);
    start_runtime();
    close = input("Type enter for a wonderful message. (Type close to quit): ")
    for r in response_list:
        if close == "close":
            print("\n Have a wonderful day, go get em tiger!")
            return;
        if close == "Close":
            print("\n Have a wonderful day, go get em tiger!")
            return;
        print_response(r);
        close = input("Type enter for a wonderful message. (Type close to quit): ")
    print("\n Have a wonderful day, go get em tiger!")
    
run_program();