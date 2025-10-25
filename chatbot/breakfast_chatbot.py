import chainlit as cl
import dotenv
import os

from openai.types.responses import ResponseTextDeltaEvent

from agents import Runner, SQLiteSession, InputGuardrailTripwireTriggered
from nutrition_agent import breakfast_advisor, exa_search_mcp

dotenv.load_dotenv()


@cl.on_chat_start
async def on_chat_start():
    await exa_search_mcp.connect()
    
    session = SQLiteSession("conversation_history")
    cl.user_session.set("agent_session", session)


@cl.on_message
async def on_message(message: cl.Message):
    session = cl.user_session.get("agent_session")

    try:
        result = Runner.run_streamed(breakfast_advisor, message.content, session=session)

        msg = cl.Message(content="")
        async for event in result.stream_events():
            # Stream final message text to screen
            if event.type == "raw_response_event" and isinstance(
                event.data, ResponseTextDeltaEvent
            ):
                await msg.stream_token(token=event.data.delta)

            elif (
                event.type == "raw_response_event"
                and hasattr(event.data, "item")
                and hasattr(event.data.item, "type")
                and event.data.item.type == "function_call"
                and len(event.data.item.arguments) > 0
            ):
                with cl.Step(name=f"{event.data.item.name}", type="tool") as step:
                    step.input = event.data.item.arguments

        await msg.update()
    
    except InputGuardrailTripwireTriggered:
        # Handle when user asks about non-food topics
        await cl.Message(
            content="⚠️ I can only help with food-related questions. Please ask me about nutrition, calories, meals, or breakfast planning!"
        ).send()

@cl.password_auth_callback
def auth_callback(username: str, password: str):
    env_user = os.getenv("CHAINLIT_USERNAME")
    env_pass = os.getenv("CHAINLIT_PASSWORD")

    if (username, password) == (env_user, env_pass):
        return cl.User(identifier=username, metadata={"role": "student", "provider": "credentials"})
    return None