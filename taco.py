def get_quote():

    # Add a list of fortunes to the empty fortune_list array
    fortune_list=[' All our dream can come true, if we have the courage to pursue them. – Walt Disney', 
    'Your attitude, not your aptitude, will determine your altitude. – Zig Ziglar', 
	'What the mind can conceive and believe, it can achieve.– Napoleon Hill',
	'For me, life is continuously being hungry. The meaning of life is not simply to exist, to survive, but to move ahead, to go up, to achieve, to conquer. – Arnold Schwarzenegger',
	'It is never too late to be what you might have been. —George Eliot',
	'Don’t worry about failure; you only have to be right once. —Drew Houston', 
	'The successful warrior is the average man, with laser-like focus. – Bruce Lee',
]
    # Use the random library to return a random element from the array
    # instead of "None"
    random_fortune 
    = random.choice(fortune_list)

    return random_fortune