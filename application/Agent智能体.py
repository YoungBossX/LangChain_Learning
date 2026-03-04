import os
import dotenv
import pathlib
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool

dotenv.load_dotenv(pathlib.Path(__file__).parent / ".env")

os.environ["OPENAI_API_KEY"] = os.getenv("LLM_API_KEY")
os.environ["OPENAI_API_BASE"] = os.getenv("LLM_BASE_URL")

@tool(description="查询价格")
def get_price(name: str) -> str:
    return f"股票 {name} 的价格是10000000000000元"

@tool(description="查询信息")
def get_info(name: str) -> str:
    return f"股票 {name} 是一家A股公司"

agent = create_agent(
    model=ChatOpenAI(model=os.getenv("LLM_MODEL_ID")),
    tools=[get_price, get_info],
    system_prompt="你是一个聊天助手，可以回答股票相关问题，记住告知我思考过程，让我知道你调用某个工具",
)

for chunk in agent.stream(
    {
        "messages": [
            {"role": "user", "content": "股票的价格是多少？介绍一下公司情况。"},
        ]
    },
    stream_mode="values"
    ):

    last_message = chunk['messages'][-1]

    if last_message.content:
        print(type(last_message).__name__, last_message.content)
    try:
        if last_message.tool_calls:
            print(f"工具调用: {[tool_call['name'] for tool_call in last_message.tool_calls]}")
    except AttributeError as e:
        pass