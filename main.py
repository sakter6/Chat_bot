import json
# will get the closes matches answer
from difflib import get_close_matches

# load Brain
def load_brain(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        data: dict = json.load(file)
    return data
    # will load new information from the user

# This will save any new information bot learn in to brain(mamory).
def save_brain(file_path: str, data: dict):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)

# this will get the closest mach answer
def find_best_match(user_question: str, question: list[str]) -> str | None:# if we dont have any answer than will return none
    matches: list = get_close_matches(user_question, question, n=1, cutoff = 0.6) # n will get the number 1 best answer.
    return matches[0] if matches else None # return best answer or if we donthave any return none.

# Will return the answer to the question that is being asked.
def get_answer_for_question(question: str, brain: dict) -> str | None:
    for q in brain['questions']:
        if q['question'] == question:
            return q['answer']

def chat_bot():# this is the main script
    brain: dict = load_brain('brain.json')

    while True:# different function
        user_input: str = input('me:')
        if user_input . lower() == 'quit':# if the user no long want to chat then it will exit by using break
            break # loop will break

        best_match: str | None = find_best_match(user_input,[q['question'] for q in brain ['questions']])
        if best_match:#If the bot don't have the answer, than it will try to get the closeest match.
            answer: str = get_answer_for_question(best_match, brain)
            print(f'Bot:{answer}')
        else:
            print('Bot: I don\'t know the answer. can you teach me?')
            # if we don't have any close match, then the bot will ask the user to teach the bot.
            new_answer: str = input('Type the answer or "skip" to skip:')
            # an opion if the user don't want to teach the bot

            if new_answer.lower() != 'skip':
                brain['questions'].append({'question': user_input,'answer': new_answer})
                # this will add the answer in the brain
                save_brain('brain.json', brain)
                print('Bot: Thank you!')

if __name__=='__main__':
    chat_bot()
