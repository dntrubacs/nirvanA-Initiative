
import api_networking


def ans_extract(answer):
    return "B"


def infr_many(question: str, infr_num: int):
    '''asks a set question to the LLM a set nuber of time and return the mode of the answers.

    Args:
        question: question for LLM (string)
        infr_num: number of times to ask the LLM

    Returns:
        Letter of mode of all LMM answers (string)
    '''
    URL = r'http://localhost:1234/v1'
    MAX_TOK = 10
    ANS_ARRAY = []
    for i in range(0, infr_num):
        ans = api_networking.llm_qa(llm_server_url=URL, message=question, max_tokens=MAX_TOK)
        ans_letter = api_networking.llm_isolate_answer(llm_server_url=URL, aviation_question=ans)
        # if (ans_letter is not "A") or (ans_letter is not "B") or (ans_letter is not "C"):
        #     continue
        if ans_letter is None:
            continue
        ANS_ARRAY.append(ans_letter)

    a_num = ANS_ARRAY.count("A")
    b_num = ANS_ARRAY.count("B")
    c_num = ANS_ARRAY.count("C")

    # temp = ["a","b","c"]

    if a_num > max(b_num, c_num):
        return "A"
    elif b_num > max(b_num, c_num):
        return "B"
    else:
        return "C"

