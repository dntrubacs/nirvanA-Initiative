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


if __name__ == '__main__':
    # Point to the local server
    debug_answer = llm_qa(llm_server_url='http://localhost:1234/v1',
                          message='Are you a robot?')
    print(debug_answer)
