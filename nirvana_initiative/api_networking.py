""" Module used to connect to the LLM server."""

from openai import OpenAI


def llm_qa(llm_server_url: str, message: str, temperature: float = 0.0,
           max_tokens: int = 10) -> str:
    """ Query an LLM models based on a local server via the OpenAI API.

    Args:
      llm_server_url: Url of the local server hosting the url.
      message: The message you want to send to the LLm (your question)
      temperature: The temperature value that sets up the randommnes on the LLM's
        answer (defaults to 0.0) .
      max_tokens: The maximum number of tokens the model can have (defaults
        to 10).

    Returns:
      String representing the answer of the LLm.
    """
    # point to the local server
    client = OpenAI(base_url=llm_server_url, api_key="not-needed")

    completion = client.chat.completions.create(
      model="local-model",  # this field is currently unused
      messages=[
        {"role": "user", "content": message}
      ],
      temperature=temperature,
      max_tokens=max_tokens
    )

    # return the answer
    return completion.choices[0].message.content


def llm_isolate_answer(llm_server_url: str, aviation_question: str,
                       temperature: float = 0.0, max_tokens: int = 10) -> str:
    """ Query an LLM with a multiple choice question and isolate the
    corresponding answer.

    Args:
      llm_server_url: Url of the local server hosting the url.
      aviation_question: The message you want to send to the LLm (your
        question).
      temperature: The temperature value that sets up the randommnes on the
        LLM's answer (defaults to 0.0).
      max_tokens: The maximum number of tokens the model can have (defaults
        to 10).
    Returns:
      String representing the answer of the LLm.
    """

    # get the llm answer
    answer = llm_qa(llm_server_url=llm_server_url,
                    message=aviation_question,
                    temperature=temperature,
                    max_tokens=max_tokens)
    # check which answer is valid
    if 'A.' in answer:
        return 'A'
    if 'B.' in answer:
        return 'B'
    if 'C.' in answer:
        return 'C'
    else:
        return None


if __name__ == '__main__':
    from data_cleaning import return_question

    import os
    os.chdir('C:/Users/Dani/Documents/pythonProject/nirvanA Initiative/')

    # list of answers to questions
    answers = []

    # go through each question
    for i in range(100):
        question = return_question(data_path='Aviation Quiz.csv', index=i)

        # Point to the local server
        debug_answer = llm_isolate_answer(
            llm_server_url='http://localhost:1234/v1',
            aviation_question=question, temperature=0, max_tokens=10)

        # append the answer
        answers.append(debug_answer)
        print(i, '/99 ', answers)

