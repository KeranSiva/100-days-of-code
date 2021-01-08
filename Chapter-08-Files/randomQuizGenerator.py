# randomQuizGenerator.py - Creates quizzes with questions and answers in
# random order, along with the answer key

import random

# TODO: Store Quiz Data in a dictionary

# Quiz data. Keys are states and values are the capitals

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}


# Generate 35 quiz files

for quizNum in range(35):
    # Create the quiz and answer key files
    quiz_file = open('capitalsquiz%s.txt' % (quizNum + 1), 'w')
    answer_keyfile = open('capitalquiz_answers%s.txt' % (quizNum +1), 'w')

    # Write out the header for the quiz
    quiz_file.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quiz_file.write((' ' * 20) + 'State Capitals Quiz (Form %s)' % (quizNum + 1))
    quiz_file.write('\n\n')

    # Shuffle the order of the states
    states = list(capitals.keys())
    random.shuffle(states)

    # Loop through all 50 states, making a question for each
    for questionNum in range(50):

        # Get right and wrong answers
        correct_answer = capitals[states[questionNum]]
        wrong_answer = list(capitals.values())
        del wrong_answer[wrong_answer.index(correct_answer)]
        del wrong_answer[wrong_answer.index(correct_answer)]
        wrong_answer = random.sample(wrong_answer, 3)
        answer_options = wrong_answer + [correct_answer]
        random.shuffle(answer_options)

        # Write the question and answer options to the quiz file
        quiz_file.write('%s. What is the capital of %s?\n' % (questionNum +1, states[questionNum]))
        for i in range(4):
            quiz_file.write('    %s. %s\n' %('ABCD'[i], answer_options[i]))
        quiz_file.write('\n')

        # Write the answer key to a file
        answer_keyfile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[answer_options.index(correct_answer)]))

    quiz_file.close()
    answer_keyfile.close()




